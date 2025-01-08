import plotly.graph_objects as go
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def plot_trajectory_realtime(trajectory, interval=0.1):
    """
    Plots the rocket's trajectory in real-time using Plotly.

    Parameters:
        trajectory (np.array): Array of [time, altitude, velocity].
        interval (int): Time interval between updates in milliseconds.
    """
    time_data = trajectory[:, 0]
    altitude_data = trajectory[:, 1]

    # Create a figure with an empty trace
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[], y=[], mode='lines', name='Altitude'))

    fig.update_layout(
        title="Rocket Trajectory in Real-Time",
        xaxis_title="Time (s)",
        yaxis_title="Altitude (m)",
        xaxis=dict(range=[0, time_data[-1]]),
        yaxis=dict(range=[0, max(altitude_data)]),
        template="plotly_dark",
    )

    # Real-time update function
    for i in range(len(time_data)):
        fig.data[0].x = time_data[:i+1]
        fig.data[0].y = altitude_data[:i+1]
        fig.show()
        fig.write_image(f"frame_{i:03d}.png")  # Save each frame as an image if needed

    fig.show()

def save_trajectory_plot(trajectory, filename="trajectory_plot.png"):
    """
    Saves the trajectory plot as an image.

    Parameters:
        trajectory (np.array): Array of [time, altitude, velocity].
        filename (str): Name of the file to save the plot.
    """
    time = trajectory[:, 0]
    altitude = trajectory[:, 1]

    plt.figure(figsize=(10, 6))
    plt.plot(time, altitude, label="Altitude vs. Time")
    plt.xlabel("Time (s)")
    plt.ylabel("Altitude (m)")
    plt.title("Rocket Trajectory")
    plt.legend()
    plt.grid(True)
    plt.savefig(filename)
    print(f"Trajectory plot saved as {filename}")

def save_trajectory_animation(trajectory, filename="trajectory_animation.mp4"):
    time = trajectory[:, 0]
    altitude = trajectory[:, 1]

    fig, ax = plt.subplots()
    ax.set_xlim(0, max(time))
    ax.set_ylim(0, max(altitude))
    line, = ax.plot([], [], lw=2)

    def update(frame):
        line.set_data(time[:frame], altitude[:frame])
        return line,

    ani = FuncAnimation(fig, update, frames=len(time), blit=True, interval=50)
    ani.save(filename)
    print(f"Animation saved as {filename}")