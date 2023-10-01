# quantum-art

**Requires a linux machine to run**

## How to run
 - Ensure that `python3` is installed
 - In the project root directory run `pip3 install -r requirement.txt`
 - Run `python3 main.py`
 - Navigate to `localhost:5000` in the browser

## Quantune

We have decided to use quantum circuits to create music, our favorite form of art! 

### How is the music created?
We divide the music into bars of a 4/4 tempo. Then each of the bars is represented by a separate quantum circuit that evolves over time (this way if only one circuit corresponds to one bar, we make sure the music is more melodic and showcases the diversity of the measurements better).
For each bar we create a quantum circuit of four qubits, where each measured state represents a different operation (musical notes, but also note timing changes that change the default quarter note of 4/4 and pauses). We then iteratively add random one- or two- qubit gates to the quantum circuit for a given bar and measure that circuit every 5 operations until the bar is filled (e.g. with 4 quarter notes). For simulating measurements, we do not use Monte Carlo (multiple shots) for each of these bars, but rather leverage and show the beauty of indeterminism in quantum circuit measurements. This way, we are able to observe patterns in the quantum circuits, while having some randomness.
Having translated the quantum states into musical operations, we construct the bars and combine multiple of them to form a song, which is then passed to a midi constructor, which in turn generates the sound file. 
Lastly, we play this generated song in the frontend of the webapp, where a user can choose which instruments they want the song to be formed from (piano or kalimba). They also have the option to see the notes and quantum circuits for each of the bars, helping them understand what is happening!

With this project we wanted to capture probably one of the most approachable forms of art and show that quantum circuits are more explainable and fun then is often expected! We hope this project will inspire more people to interact with quantum!

