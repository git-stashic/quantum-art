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

n = 36
note_to_pitch_bass = {
    'C': 60-n,
    'Cis': 61-n,
    'D': 62-n,
    'Dis': 63-n,
    'E': 64-n,
    'F': 65-n,
    'Fis': 66-n,
    'G': 67-n,
    'Gis': 68-n,
    'A': 69-n,
    'Ais': 70-n,
    'B': 71-n,
}


def create_midi_song(song: list[list[str]]):
    mf = MIDIFile(2)  # only 1 track
    track = 0         # the only track

    time = 0          # start at the beginning
    mf.addTrackName(track, time, "Sample Track")
    mf.addTempo(track, time, 240)

    # add some notes
    channel = 0
    volume = 100

    bass = False

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
            if bass:
                pitch = note_to_pitch_bass[note]
            else:
                pitch = note_to_pitch[note]
            mf.addNote(track, channel, pitch, time, duration, volume)
            time += duration

    time = 0
    track = 1
    bass = True
    mf.addTrackName(track, time, "Quantum Music")
    mf.addTempo(track, time, 240)
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
            if bass:
                pitch = note_to_pitch_bass[note]
            else:
                pitch = note_to_pitch[note]
            mf.addNote(track, channel, pitch, time, duration, volume)
            time += duration

    return mf
