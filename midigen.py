from midiutil.MidiFile import MIDIFile

note_to_pitch = {
    'C': 60,
    'Cis': 61,
    'D': 62,
    'Dis': 63,
    'E': 64,
    'F': 65,
    'Fis': 66,
    'G': 67,
    'Gis': 68,
    'A': 69,
    'Ais': 70,
    'B': 71,
}


def create_midi_song(song: list[list[str]]):
    mf = MIDIFile(1)     # only 1 track
    track = 0   # the only track

    time = 0    # start at the beginning
    mf.addTrackName(track, time, "Sample Track")
    mf.addTempo(track, time, 180)

    # add some notes
    channel = 0
    volume = 100

    for bar in example:
        for note in bar:
            duration = 1
            if note[-1] == '*':
                duration = 2
                note = note[:-1]
            elif note[-1] == '/':
                duration = 0.5
                note = note[:-1]
            if note == '_':
                time += duration
                continue
            pitch = note_to_pitch[note]
            mf.addNote(track, channel, pitch, time, duration, volume)
            time += duration

    return mf


example = [
    ['Fis', 'Ais', 'E', 'E'], ['F', 'A', 'Ais*'], ['B', 'F', 'D', 'F'],
    ['D', 'A', '_/', 'Ais', 'E/'], ['Gis/', 'Cis', 'Ais', 'D', '_/'],
    ['Gis', 'Cis', 'F', 'C'], ['G', 'Cis', 'Gis', '_'],
    ['E', 'Dis', 'Fis', 'F'], ['D', 'G', 'G', 'A'],
    ['A/', 'F', 'G', 'Dis', '_/']
]


# write it to disk
with open("output.mid", 'wb') as outf:
    create_midi_song(example).writeFile(outf)
