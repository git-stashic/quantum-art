from flask import Flask, render_template, redirect, request, url_for, session, flash, send_from_directory
from midigen import create_midi_song
from quantum import create_song
import uuid

app = Flask(__name__)
app.secret_key = "squishystick"


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == "POST":
        if 'generate' in request.form:
            return redirect(url_for("generate"))
    return render_template('index.html')


@app.route('/generate')
def generate():
    notes = create_song(30)
    midi = create_midi_song(notes)
    filename = str(uuid.uuid4())
    filepath = "/tmp/quantum-music/" + filename + ".mid"
    with open(filepath, 'wb') as outf:
        midi.writeFile(outf)
    return render_template('generate.html', midi=filename + ".mid")

    app.run(debug=True)


@app.route('/songs/<path:path>')
def send_report(path):
    return send_from_directory('/tmp/quantum-music/', path)


if __name__ == '__main__':
    app.run(debug=True)
