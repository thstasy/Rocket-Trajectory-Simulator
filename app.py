from flask import Flask, request, jsonify
from simulator import simulate_trajectory_multi_stage

app = Flask(__name__)

@app.route('/')
def home():
    """
    A simple home page to guide users on using the API.
    """
    return """
    <h1>Welcome to the Rocket Trajectory Simulator API!</h1>
    <p>This API allows you to simulate the trajectory of a multi-stage rocket. To use the API:</p>
    <ul>
        <li>Send a <strong>POST</strong> request to the <code>/simulate</code> endpoint.</li>
        <li>The request body must be a JSON object with the following format:</li>
    </ul>
    <pre>
    {
        "stages": [
            {"mass": 500, "thrust": 15000, "burn_time": 30},
            {"mass": 300, "thrust": 12000, "burn_time": 20},
            {"mass": 100, "thrust": 8000, "burn_time": 15}
        ]
    }
    </pre>
    <p>Example curl command to test the endpoint:</p>
    <pre>
    curl -X POST http://127.0.0.1:5000/simulate \\
    -H "Content-Type: application/json" \\
    -d '{"stages": [{"mass": 500, "thrust": 15000, "burn_time": 30}, {"mass": 300, "thrust": 12000, "burn_time": 20}, {"mass": 100, "thrust": 8000, "burn_time": 15}]}'
    </pre>
    <p>You can also use tools like Postman to send a POST request with the above JSON payload.</p>
    """

@app.route('/simulate', methods=['POST'])
def simulate():
    """
    Endpoint to simulate a rocket trajectory.
    Expects JSON input with rocket stages.
    """
    data = request.json
    trajectory = simulate_trajectory_multi_stage(data['stages'])
    return jsonify(trajectory.tolist())

if __name__ == '__main__':
    app.run(debug=True)