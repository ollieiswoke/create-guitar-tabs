NOTEORDERFLATS = ["C","Db","D","Eb","E","F","Gb","G","Ab","A","Bb","B"]
NOTEORDERSHARPS = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]


def findClosestString(note):
    "Given a note, figure out which of the 6 guitar strings it's closest to"
    #calclate distance to each fret...
    strings = "E2 A2 D3 G3 B3 E4".split(" ")
    index2dist = {}
    for i in range(len(strings)):
        string = strings[i]
        dist = findDistanceBetweenNotes(string,note)
        #distance needs to positive ie. note is higher than fret
        if dist == 0:
            return string
        if dist > 0:
            index2dist[i] = dist
    if len(index2dist) == 0:
        return None
    #see which fret is the min distance    
    indexOfClosestDist = min(index2dist, key=index2dist.get)
    return strings[indexOfClosestDist]

def findDistanceBetweenNotes(note1, note2):
    #return how much higher / lower note2 is compared to note1
    NUM_KEYS_IN_OCTAVE = 12
    octavesHigher = int(note2[-1:]) - int(note1[-1:])
    notesHigherInScale = getNoteNumber(note2) - getNoteNumber(note1)
    notesHigher = octavesHigher*NUM_KEYS_IN_OCTAVE + notesHigherInScale
    return notesHigher

def getNoteNumber(note):
    # Converts note name to it's index in the global list NOTEORDERSHARPS
    # This allows notes to be compared to other notes
    global NOTEORDERFLATS
    for i in range(len(NOTEORDERFLATS)):
        if NOTEORDERFLATS[i] == note[:-1] or NOTEORDERSHARPS[i] == note[:-1]:
            return i
    raise NameError

def print_instruction(file):
    for note in file.split(" "):
        string = findClosestString(note)
        dist = findDistanceBetweenNotes(string, note)
        if dist == None:
            print(f"{note}    [not possible]")
        else:
            if len(note) == 3:
                print(f"{note}   {string} on {findDistanceBetweenNotes(string, note)} fret")
            else:
                print(f"{note}    {string} on {findDistanceBetweenNotes(string, note)} fret")

def demo():
    "prints out how to play AbMaj7 on guitar"
    file = "G#3 C4 D#4 G4"
    print_instruction(file)