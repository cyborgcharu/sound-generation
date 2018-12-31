# Sound Generation
## Overview
Synthesizes sound stimuli for brain-computer interface studies @BrainLab

## Installation
Install requirements by running ```pip install -r requirements.txt```


## Inputs
In order to run this file, you need:
1. Input Audio File - This is a .wav file of a single sound; this file should be stripped of all metadata (if you use Audacity or other audio players, you must strip the metadata off)
2. Frequency - The frequency of the synthesized sound in Hz
3. Duration - The duration of the synthesized sound in sec
4. Output Audio Filename - The name of the output .wav file that the synthesized sound will be saved to

## Run
Run file by running ```python sound-generation.py INPUTFILE FREQUENCY DURATION OUTPUTFILENAME```
