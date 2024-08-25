# Notes on the IDMT-SMT-Guitar_V2 Dataset

## [IDMT-SMT-Guitar](https://zenodo.org/records/7544110)
### Dataset #1
- All introduced playing techniques (plucking styles: finger-style, muted, 
  picked; expression styles: normal, bending, slide, vibrato, harmonics, 
  dead-notes).
- Provided with a bit depth of 24 Bit.
- Recorded using three different guitars.
- Consists of ~4700 note events with monophonic and polyphonic struture.
- Recorded files contain realistic guitar licks ranging from monophonic to
  polyphonic instrument tracks.
- Parameter annotations stored in XML format.

### Dataset #2
- 400 monophonic and polyphonic note events.
- Recorded with two different guitars.
- No expression styles applied.
- Each note event recorded and stored in a separate with 16 Bit depth.
- Parameter annotations stored in XML format.

### Dataset #3
- Five short monophonic and polyphonic guitar recordings.
- All recorded with the same instrument.
- No expression styles applied.
- Files stored with 16 Bit depth.
- Each file is accompanied by a parameter annotation in XML format.

### Dataset #4
- Created for evaluation purposes in the context of chord recognition and
  rhythm style estimation tasks.
- 64 short musical pieces grouped by genre.
- At least two different tempos per piece.
- Recorded with three different guitars.
- Files stored with 16 Bit depth.
- Annotations regarding onset positions, chords, rhythmic pattern length, and
  texture (monophony/polyphony) are included in various file formats.

## Annotation Parsing
- Chord instances (as opposed to single notes) are denoted by events with
  overlapping onset/offset ranges.
- Need to determine how pitches map to notes/octaves.

