from simulator import simulate_trajectory_multi_stage
from plotter import plot_trajectory_realtime, save_trajectory_plot

stages = [
    {'mass': 500, 'thrust': 15000, 'burn_time': 30},
    {'mass': 300, 'thrust': 12000, 'burn_time': 20},
    {'mass': 100, 'thrust': 8000, 'burn_time': 15}
]

# Simulate the rocket trajectory
trajectory = simulate_trajectory_multi_stage(stages)
print("Trajectory Data:")
print(trajectory)

# Real-time visualization
plot_trajectory_realtime(trajectory)

# Save the final plot
save_trajectory_plot(trajectory, "final_trajectory_plot.png")

save_trajectory_animation(trajectory, "trajectory_animation.mp4")