Rocket Trajectory Simulator

Project Description

The Rocket Trajectory Simulator is a Python-based application that simulates the trajectory of a multi-stage rocket using basic physics principles. It features:
	•	Real-time Visualization: Dynamically plots the altitude of the rocket during its flight.
	•	Static Plot and Data Recording: Saves trajectory plots and logs simulation data for analysis.
	•	Interactive API: A Flask-based web server that allows users to simulate custom rocket configurations by sending requests to the /simulate endpoint.

This tool is ideal for students, educators, and developers interested in rocket physics.

Installation
	1.	Clone the Repository

git clone <your-repo-url>
cd rocket_simulator


	2.	Set Up the Virtual Environment

python3 -m venv rocket_env
source rocket_env/bin/activate  # On Windows, use rocket_env\Scripts\activate


	3.	Install Dependencies

pip install -r requirements.txt

Usage

1. Running the Simulation Locally

Run the simulation directly from the command line:

python main.py

What to Expect:
	•	Real-Time Graph: A Plotly window dynamically shows the rocket’s altitude during the simulation.
	•	Static Plot: A plot of the trajectory saved as final_trajectory_plot.png.
	•	Trajectory Data: Logs of time, altitude, and velocity printed to the console.

2. Running the Flask API

Start the Flask server:

python app.py

Expected Output:
	•	The server runs on http://127.0.0.1:5000/.
	•	Navigate to http://127.0.0.1:5000/ for instructions.

Simulating a Trajectory via API

Send a POST request to the /simulate endpoint:

curl -X POST http://127.0.0.1:5000/simulate \
-H "Content-Type: application/json" \
-d '{"stages": [{"mass": 500, "thrust": 15000, "burn_time": 30}, {"mass": 300, "thrust": 12000, "burn_time": 20}, {"mass": 100, "thrust": 8000, "burn_time": 15}]}'

Expected Response:
A JSON array containing the trajectory data:

[
    [0, 0, 0],
    [0.1, 10.5, 105],
    [0.2, 21.8, 108],
    ...
]

3. Common Issues and Fixes

Port 5000 Already in Use

Start the Flask server on a different port:

python app.py --port=8000

Access the server at http://127.0.0.1:8000.

kaleido Not Installed

To save images using Plotly, install the kaleido package:

pip install kaleido

GitHub Setup

1. Push Your Code to GitHub
	1.	Initialize a new Git repository:

git init


	2.	Add and commit your files:

git add .
git commit -m "Initial commit"


	3.	Add your GitHub repository as a remote:

git remote add origin <your-repo-url>


	4.	Push your code:

git branch -M main
git push -u origin main

Future Improvements
	•	Enhanced Real-Time Visualization: Smooth animations with better interactivity.
	•	Deployment: Host the API on a cloud service like Render or PythonAnywhere.
	•	Unit Tests: Add tests to verify physics calculations and API functionality.

Let me know if you need help with pushing to GitHub or additional changes! 🚀