# Music Transcription

## Overview
The goal of this project is to automatically transcribe sheet music with
multiple voices given any piece of music formatted as an .mp3 file.
Specifically, the output format should be .xml files that can be rendered by
MuseScore.

## Specifics
For the initial stage of this project, the focus will be pieces written for a
single guitar.  An important part of this will be correctly identifying not only
which chords are being played in the instance that there are multiple notes
being played at a time, but also which voicing of each chord is being played. 

## Steps
1) Obtain a data set to train on.
   - Downloaded [IDMT-SMT-GUITAR_V2](https://zenodo.org/records/7544110)

2) TODO: Develop a testing framework (compare the resulting .xml files outputted
   by the model to the .xml files downloaded from dataset, and return accuracy
   measures).
   
3) TODO: Evaluate different types of models on the dataset to determine which 
   seem to be the best for each task.
   - Things to detect:
     1) TODO: How many notes are being played?
     2) TODO: What note values (1-12) are being played? (TODO: determine if the 
        strongest pitch values determined by Librosa chromagram are the same as
        the notes being played in all cases).
     3) TODO: What are the octaves of the notes being played?
     4) TODO: What are the lengths of the notes being played?
     5) TODO: What key is the music played in?
     6) TODO: What time signature is the music played in?
     7) TODO: What tuning is the guitar in?
     8) TODO: What are the fingerings being used in the recording?
     9) TODO: Detection of different voices.
     10) TODO: Detection of dynamics.

4) TODO: Render the results formally as sheet music.
