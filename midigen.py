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
    mf = MIDIFile(1)  # only 1 track
    track = 0         # the only track

    time = 0          # start at the beginning
    mf.addTrackName(track, time, "Sample Track")
    mf.addTempo(track, time, 240)

    # add some notes
    channel = 0
    volume = 100

    for bar in song:
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
