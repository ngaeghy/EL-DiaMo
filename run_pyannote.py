import sys
import re
from collections import defaultdict
from pyannote.audio import Pipeline

params = {}
for line in sys.stdin:
    match = re.search(r'<param name="(.*?)".*?>(.*?)</param>', line)
    if match:
        params[match.group(1)] = match.group(2).strip()
input_file_path = params["source"]
access_token = params["hf_access_token"]
is_supervised = False
if params["supervision"] == "Supervised":
    min_speakers = int(params["min_speakers"])
    max_speakers = int(params["max_speakers"])
    if min_speakers > 0 and max_speakers > 0:
        is_supervised = True

if is_supervised:
    print(f"PROGRESS: 0.2 Running supervised pyannote model: {min_speakers} to {max_speakers} speakers", flush = True)
else:
    print(f"PROGRESS: 0.2 Running unsupervised pyannote model", flush = True)
with open(input_file_path, "rb") as input_audio:
    pipeline = Pipeline.from_pretrained(
        "pyannote/speaker-diarization-3.1",
        use_auth_token=access_token)
    if not is_supervised:
        diarization = pipeline(input_audio)
    elif min_speakers == max_speakers:
        diarization = pipeline(input_audio, num_speakers=min_speakers)
    else:
        diarization = pipeline(input_audio, min_speakers=min_speakers, max_speakers=max_speakers)

print("PROGRESS: 0.9 Writing output tier", flush = True)
with open(params['output_tier'], 'w', encoding = 'utf-8') as output_tier:
    output_tier.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    output_tier.write(f'<TIERS xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="file:avatech-tiers.xsd">\n')
    
    turns_by_speaker = defaultdict(list)
    for turn, _, speaker in diarization.itertracks(yield_label=True):
        turns_by_speaker[speaker].append((turn.start, turn.end))
    for speaker, turns in turns_by_speaker.items():
        output_tier.write(f'<TIER columns="Diarized-{speaker}">\n')
        for turn in turns:
            output_tier.write(f'    <span start="{turn[0]:.1f}" end="{turn[1]:.1f}"><v>{speaker}</v></span>\n')
        output_tier.write('</TIER>\n')
    
    output_tier.write('</TIERS>\n')

print('RESULT: DONE.', flush = True)
