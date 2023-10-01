from flask import Flask, render_template, redirect, request, url_for, session, flash
from  midigen import create_midi_song
from quantum import create_song

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
    return render_template('generate.html', midi=midi)

if __name__ == '__main__':
    app.run(debug=True)