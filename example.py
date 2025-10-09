#!/usr/bin/env python3
"""
Example usage of the Big Black Line Follower 202
"""

from bblf202 import LineFollower


def main():
    """Run the line follower with custom settings."""
    
    # Create robot with custom PID values
    robot = LineFollower(
        kp=0.6,      # Adjust for your robot
        ki=0.01,     # Small integral to reduce steady-state error
        kd=0.15,     # Derivative to reduce oscillation
        base_speed=120,
        num_sensors=5
    )
    
    # Run for 30 seconds
    print("Running line follower for 30 seconds...")
    robot.run(duration=30)


if __name__ == "__main__":
    main()
