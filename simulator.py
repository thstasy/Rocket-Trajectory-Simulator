import numpy as np

def simulate_trajectory_multi_stage(stages, drag_coeff=0.5, dt=0.1):
    """
    Simulates a multi-stage rocket's trajectory.

    Parameters:
        stages (list): List of dictionaries containing stage parameters.
        drag_coeff (float): Drag coefficient (dimensionless).
        dt (float): Time step for the simulation (seconds).

    Returns:
        np.array: Trajectory data as an array of [time, altitude, velocity].
    """
    g = 9.81  # Gravity in m/s^2
    air_density = 1.225  # kg/m^3
    cross_section_area = 1.0  # m^2 (assumed)

    # Initialize simulation variables
    trajectory = []
    velocity = 0
    altitude = 0
    time = 0

    # Total rocket mass (including all stages initially)
    total_mass = sum(stage['mass'] for stage in stages)

    for i, stage in enumerate(stages):
        stage_mass = stage['mass']
        thrust = stage['thrust']
        burn_time = stage['burn_time']

        print(f"Stage {i + 1}: Mass = {stage_mass}, Thrust = {thrust}, Burn Time = {burn_time}")

        while burn_time > 0 and altitude >= 0:
            # Forces calculation
            thrust_force = thrust
            drag_force = 0.5 * drag_coeff * air_density * velocity**2 * cross_section_area
            weight = total_mass * g
            net_force = thrust_force - drag_force - weight

            # Update physics
            acceleration = net_force / total_mass
            velocity += acceleration * dt
            altitude += velocity * dt

            # Store current state
            trajectory.append((time, altitude, velocity))

            # Debugging print: Per timestep
            print(f"Time: {time:.2f}, Altitude: {altitude:.2f}, Velocity: {velocity:.2f}")

            # Update time and burn time
            time += dt
            burn_time -= dt

        # After burn, drop stage mass
        if i < len(stages) - 1:  # If not the last stage
            print(f"Dropping Stage {i + 1}")
            total_mass -= stage_mass

    return np.array(trajectory)