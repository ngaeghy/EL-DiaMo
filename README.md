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
3. On MacOS, create a new directory (whatever name) under ELAN_{VERSION_#}.app/Contents/app/extensions and copy the files in this repo there
4. Launch ELAN and open the corresponding audio and annotation files
5. Go to the **Recognizer** tab and choose **STREAMLInED Diarization** from the drop down menu
6. Paste the Hugging Face access token
7. Choose model parameters and click **Start**
8. When the run finishes, follow the pop up window to load the result as tiers

***\*Only tested with Python 3.10, ELAN 6.8, on MacOS 14.6\****

## Acknowledgements
Part of the code is built on top of the work by Sam Michel. The code also draws inspiration from the many ELAN recognizers written by Christopher Cox. Additionally, thanks to Prof Gina-Anne Levow for the directions and advices to the task.

## Contact
Ghau Yan Ngae - ngaeghy [at] uw [dot] edu
