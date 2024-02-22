# create-guitar-tabs
Translates note data to guitar tabs

Sometimes I find it hard to translate what I play on piano to guitar. This program is a quick prototype that takes in note data and reccomends how to play it on guitar.

### Demo 
```
How to play a Abmaj7 chord on Guitar...
# Output 
G#3   G3 on 1 fret
C4    B3 on 1 fret
D#4   B3 on 4 fret
G4    E4 on 3 fret
```

### Behind the scenes
Notes at represented as a note name followed by octave (e.g. `G4`). Sharps and flats are accounted for. A sequence is a space separated string e.g. `'G3 C4 E4 G#3 E4 A3 C4 F4 Ab3 C4 F4'`.

Limitations: The guitar's upper range has not been accounted for. According to this program, you could play the 100th octave if you just went up enough frets. No rhythmic information is stored. No finger recommendations are given. It calculates ease of playing by finding out how to play a note with the minimum amount of fret raises, but different systems could be used to estimate physical distance from last note played.
Example:

### Future
Potential expansions could include inputting MIDI data and formatting output to resemble more traditional guitar tabs. e.g.
```
e|-----4-------4---|-----4-------4---|-----4-------4---|-0---0---0---0---|
B|-5-------5-------|-5-------5-------|-4-------4-------|-5---5p4-5---5-0-|
G|-----------------|-----------------|-----------------|-----------------|  x2
D|-----------------|-----------------|-----------------|-----------------|
A|-----------------|-----------------|-----------------|-----------------|
E|-----------------|-----------------|-----------------|-----------------|
```
