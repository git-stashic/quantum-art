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
    'X': 72,
}

example = [
    ['Fis', 'Ais', 'E', 'E'], ['F', 'A', 'Ais*'], ['B', 'F', 'D', 'F'],
    ['D', 'A', '/', 'Ais', 'E/'], ['Gis/', 'Cis', 'Ais', 'D', '/'],
    ['Gis', 'Cis', 'F', 'C'], ['G', 'Cis', 'Gis', 'X'],
    ['E', 'Dis', 'Fis', 'F'], ['D', 'G', 'G', 'A'],
    ['A/', 'F', 'G', 'Dis', 'X/']
]
# create your MIDI object
mf = MIDIFile(1)     # only 1 track
track = 0   # the only track

time = 0    # start at the beginning
mf.addTrackName(track, time, "Sample Track")
mf.addTempo(track, time, 240)

# add some notes
channel = 0
volume = 100

for bar in example:
    for note in bar:
        duration = 2
        if note[-1] == '*':
            duration = 4
            note = note[:-1]
        elif note[-1] == '/':
            duration = 1
            note = note[:-1]
        if note == 'X' or note == "":
            time += duration
            continue
        pitch = note_to_pitch[note]
        mf.addNote(track, channel, pitch, time, duration, volume)
        time += duration

# pitch = 60           # C4 (middle C)
# time = 0             # start on beat 0
# duration = 1         # 1 beat long
# mf.addNote(track, channel, pitch, time, duration, volume)
#
# pitch = 64           # E4
# time = 2             # start on beat 2
# duration = 1         # 1 beat long
# mf.addNote(track, channel, pitch, time, duration, volume)
#
# pitch = 67           # G4
# time = 4             # start on beat 4
# duration = 1         # 1 beat long
# mf.addNote(track, channel, pitch, time, duration, volume)

# write it to disk
with open("output.mid", 'wb') as outf:
    mf.writeFile(outf)
