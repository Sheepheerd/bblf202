#!/usr/bin/env python3
"""
Big Black Line Follower 202 - Main Robot Controller

This module implements the main controller for a line-following robot
using sensor input and motor control with PID feedback.
"""

import time
from typing import List, Tuple


class PIDController:
    """PID Controller for smooth line following."""
    
    def __init__(self, kp: float = 1.0, ki: float = 0.0, kd: float = 0.0):
        """
        Initialize PID controller.
        
        Args:
            kp: Proportional gain
            ki: Integral gain
            kd: Derivative gain
        """
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.prev_error = 0.0
        self.integral = 0.0
    
    def calculate(self, error: float, dt: float = 0.01) -> float:
        """
        Calculate PID output.
        
        Args:
            error: Current error value
            dt: Time delta since last calculation
            
        Returns:
            PID control output
        """
        self.integral += error * dt
        derivative = (error - self.prev_error) / dt if dt > 0 else 0.0
        output = (self.kp * error) + (self.ki * self.integral) + (self.kd * derivative)
        self.prev_error = error
        return output
    
    def reset(self):
        """Reset PID controller state."""
        self.prev_error = 0.0
        self.integral = 0.0


class LineSensor:
    """Interface for line sensor array."""
    
    def __init__(self, num_sensors: int = 5):
        """
        Initialize line sensor array.
        
        Args:
            num_sensors: Number of sensors in the array
        """
        self.num_sensors = num_sensors
    
    def read(self) -> List[int]:
        """
        Read sensor values.
        
        Returns:
            List of sensor values (0 for white, 1 for black)
        """
        # Placeholder implementation - in real robot, read from hardware
        return [0] * self.num_sensors
    
    def get_position(self) -> float:
        """
        Calculate line position from sensor readings.
        
        Returns:
            Position value (-1.0 to 1.0, 0 is center)
        """
        sensors = self.read()
        weighted_sum = 0.0
        total = 0.0
        
        for i, value in enumerate(sensors):
            position = (i - (self.num_sensors - 1) / 2.0) / ((self.num_sensors - 1) / 2.0)
            weighted_sum += position * value
            total += value
        
        if total == 0:
            return 0.0
        
        return weighted_sum / total


class MotorController:
    """Motor controller for differential drive robot."""
    
    def __init__(self, base_speed: int = 100):
        """
        Initialize motor controller.
        
        Args:
            base_speed: Base speed for motors (0-255)
        """
        self.base_speed = base_speed
        self.left_speed = 0
        self.right_speed = 0
    
    def set_motors(self, left: int, right: int):
        """
        Set motor speeds.
        
        Args:
            left: Left motor speed (-255 to 255)
            right: Right motor speed (-255 to 255)
        """
        self.left_speed = max(-255, min(255, left))
        self.right_speed = max(-255, min(255, right))
        # Placeholder - in real robot, write to hardware
    
    def drive(self, speed: int, turn: float):
        """
        Drive robot with speed and turn rate.
        
        Args:
            speed: Forward speed (0-255)
            turn: Turn rate (-1.0 to 1.0, negative is left)
        """
        left = int(speed + (turn * speed))
        right = int(speed - (turn * speed))
        self.set_motors(left, right)
    
    def stop(self):
        """Stop all motors."""
        self.set_motors(0, 0)


class LineFollower:
    """Main line follower robot controller."""
    
    def __init__(self, kp: float = 0.5, ki: float = 0.0, kd: float = 0.1, 
                 base_speed: int = 100, num_sensors: int = 5):
        """
        Initialize line follower robot.
        
        Args:
            kp: PID proportional gain
            ki: PID integral gain
            kd: PID derivative gain
            base_speed: Base motor speed
            num_sensors: Number of line sensors
        """
        self.pid = PIDController(kp, ki, kd)
        self.sensor = LineSensor(num_sensors)
        self.motor = MotorController(base_speed)
        self.running = False
    
    def start(self):
        """Start the line follower."""
        self.running = True
        self.pid.reset()
        print("Big Black Line Follower 202 - Started")
    
    def stop(self):
        """Stop the line follower."""
        self.running = False
        self.motor.stop()
        print("Big Black Line Follower 202 - Stopped")
    
    def update(self):
        """Update robot control based on sensor input."""
        if not self.running:
            return
        
        # Get line position
        position = self.sensor.get_position()
        
        # Calculate PID correction
        correction = self.pid.calculate(position)
        
        # Apply correction to motors
        self.motor.drive(self.motor.base_speed, correction)
    
    def run(self, duration: float = None):
        """
        Run the line follower.
        
        Args:
            duration: How long to run (None for indefinite)
        """
        self.start()
        start_time = time.time()
        
        try:
            while self.running:
                self.update()
                time.sleep(0.01)  # 100Hz update rate
                
                if duration and (time.time() - start_time) > duration:
                    break
        except KeyboardInterrupt:
            print("\nInterrupted by user")
        finally:
            self.stop()


def main():
    """Main entry point."""
    print("=" * 50)
    print("Big Black Line Follower 202")
    print("=" * 50)
    
    # Create and configure robot
    robot = LineFollower(
        kp=0.5,
        ki=0.0,
        kd=0.1,
        base_speed=100,
        num_sensors=5
    )
    
    # Run robot
    robot.run()


if __name__ == "__main__":
    main()
