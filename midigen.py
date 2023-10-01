import subprocess
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

INSTRUMENTS = {
    'piano': ('soundfonts/TimGM6mb.sf2', 0),
    'kalimba': ('soundfonts/MultiKalimba.sf2', 9)
}

def create_midi_song(song: list[list[str]], channel = 0):
    mf = MIDIFile(2)  # only 1 track
    track = 0         # the only track

    time = 0          # start at the beginning
    mf.addTrackName(track, time, "Sample Track")
    mf.addTempo(track, time, 240)

    # add some notes
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


def convert_midi_to_mp3(id, soundfont):
    input_midi = f'/tmp/quantum-music/{id}.mid'
    raw_file = f'/tmp/quantum-music/{id}.raw'
    wav_file = f'/tmp/quantum-music/{id}.wav'
    mp3_file = f'/tmp/quantum-music/{id}.mp3'
    # Convert MIDI to raw audio using FluidSynth
    fluidsynth_cmd = f'fluidsynth -a alsa -g 1.0 -l -i -T raw -F {raw_file} {soundfont} {input_midi}'
    subprocess.run(fluidsynth_cmd, shell=True)

    # Convert raw audio to WAV using SoX
    sox_cmd = f'sox -r 44100 -e signed -b 16 -c 2 {raw_file} {wav_file}'
    subprocess.run(sox_cmd, shell=True)

    # Convert WAV to MP3 using LAME
    lame_cmd = f'lame -b 320 {wav_file} {mp3_file}'
    subprocess.run(lame_cmd, shell=True)

    # Clean up intermediate files (optional)
    subprocess.run(f'rm {raw_file} {wav_file}', shell=True)