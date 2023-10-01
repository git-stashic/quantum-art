from flask import Flask, render_template, redirect, request, url_for, session, flash, send_from_directory
from midigen import INSTRUMENTS, create_midi_song, convert_midi_to_mp3
from quantum import create_song
import os
import uuid
import matplotlib


def get_save_dir():
    return os.environ.get('SAVE_DIR', '/tmp/quantum-music/')


app = Flask(__name__)
app.secret_key = "squishystick"


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == "POST":
        if 'generate' in request.form:
            return redirect(url_for("generate"))
    return render_template('index.html', INSTRUMENTS=INSTRUMENTS)


@app.route('/generate')
def generate():
    song_length = 30
    sf, channel = INSTRUMENTS[request.args.get('instrument', 'piano')]

    song_id = uuid.uuid4()
    notes, qc = create_song(song_length, song_id)
    midi = create_midi_song(notes, channel)

    filepath = get_save_dir() + str(song_id) + ".mid"
    with open(filepath, 'wb') as outf:
        midi.writeFile(outf)
    convert_midi_to_mp3(str(song_id), sf)

    return render_template('generate.html', song_id=str(song_id), length=song_length)


@app.route('/songs/<string:song_id>')
def serve_song(song_id):
    return send_from_directory(get_save_dir(), song_id + ".mid")


@app.route('/circuits/<string:song_id>/<string:circuit_id>')
def serve_circuits(song_id, circuit_id):
    return send_from_directory(get_save_dir() + song_id + '/', circuit_id + ".png")


if __name__ == '__main__':
    os.makedirs(get_save_dir(), exist_ok=True)
    app.run(debug=True)
