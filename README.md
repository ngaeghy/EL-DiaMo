# ELAN-Diar
ELAN Integration for speaker diarization models

## Prerequisites

* Python 3
* [ELAN](https://archive.mpi.nl/tla/elan)

## Models

* [pyannote](https://huggingface.co/pyannote/speaker-diarization)
* VBx (TBD)
* Kaldi (TBD)

## Steps to run

1. For pyannote, follow the [instructions](https://github.com/pyannote/pyannote-audio?tab=readme-ov-file#tldr) to install the dependencies, accept the user conditions, and create a Hugging Face access token
2. Change the PYTHON variable in `streamlined_diar.sh` to the path of your local python binary
3. Launch ELAN and open the corresponding audio and annotation files
4. Go to the **Recognizer** tab and choose **STREAMLInED Diarization** from the drop down menu
5. Paste the Hugging Face access token
6. Choose model parameters and click **Start**
7. When the run finishes, follow the pop up window to load the result as tiers

***\*Only tested with Python 3.10, ELAN 6.8, on MacOS 14.6\****

## Contact
ngaeghy [at] uw [dot] edu

