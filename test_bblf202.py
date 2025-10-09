#!/usr/bin/env python3
"""
Tests for Big Black Line Follower 202
"""

import unittest
from bblf202 import PIDController, LineSensor, MotorController, LineFollower


class TestPIDController(unittest.TestCase):
    """Test PID controller functionality."""
    
    def test_initialization(self):
        """Test PID controller initialization."""
        pid = PIDController(kp=1.0, ki=0.5, kd=0.1)
        self.assertEqual(pid.kp, 1.0)
        self.assertEqual(pid.ki, 0.5)
        self.assertEqual(pid.kd, 0.1)
        self.assertEqual(pid.prev_error, 0.0)
        self.assertEqual(pid.integral, 0.0)
    
    def test_proportional_only(self):
        """Test proportional control only."""
        pid = PIDController(kp=1.0, ki=0.0, kd=0.0)
        output = pid.calculate(error=0.5, dt=0.01)
        self.assertEqual(output, 0.5)
    
    def test_reset(self):
        """Test PID reset functionality."""
        pid = PIDController(kp=1.0, ki=0.5, kd=0.1)
        pid.calculate(error=0.5, dt=0.01)
        pid.reset()
        self.assertEqual(pid.prev_error, 0.0)
        self.assertEqual(pid.integral, 0.0)


class TestLineSensor(unittest.TestCase):
    """Test line sensor functionality."""
    
    def test_initialization(self):
        """Test sensor initialization."""
        sensor = LineSensor(num_sensors=5)
        self.assertEqual(sensor.num_sensors, 5)
    
    def test_read(self):
        """Test sensor reading."""
        sensor = LineSensor(num_sensors=5)
        readings = sensor.read()
        self.assertEqual(len(readings), 5)
        self.assertTrue(all(r in [0, 1] for r in readings))
    
    def test_position_centered(self):
        """Test position calculation when centered."""
        sensor = LineSensor(num_sensors=5)
        position = sensor.get_position()
        self.assertIsInstance(position, float)
        self.assertGreaterEqual(position, -1.0)
        self.assertLessEqual(position, 1.0)


class TestMotorController(unittest.TestCase):
    """Test motor controller functionality."""
    
    def test_initialization(self):
        """Test motor controller initialization."""
        motor = MotorController(base_speed=100)
        self.assertEqual(motor.base_speed, 100)
        self.assertEqual(motor.left_speed, 0)
        self.assertEqual(motor.right_speed, 0)
    
    def test_set_motors(self):
        """Test setting motor speeds."""
        motor = MotorController()
        motor.set_motors(100, 150)
        self.assertEqual(motor.left_speed, 100)
        self.assertEqual(motor.right_speed, 150)
    
    def test_motor_clamping(self):
        """Test motor speed clamping."""
        motor = MotorController()
        motor.set_motors(300, -300)
        self.assertEqual(motor.left_speed, 255)
        self.assertEqual(motor.right_speed, -255)
    
    def test_stop(self):
        """Test motor stop."""
        motor = MotorController()
        motor.set_motors(100, 100)
        motor.stop()
        self.assertEqual(motor.left_speed, 0)
        self.assertEqual(motor.right_speed, 0)


class TestLineFollower(unittest.TestCase):
    """Test line follower robot."""
    
    def test_initialization(self):
        """Test robot initialization."""
        robot = LineFollower(kp=0.5, ki=0.0, kd=0.1, base_speed=100, num_sensors=5)
        self.assertIsNotNone(robot.pid)
        self.assertIsNotNone(robot.sensor)
        self.assertIsNotNone(robot.motor)
        self.assertFalse(robot.running)
    
    def test_start_stop(self):
        """Test robot start and stop."""
        robot = LineFollower()
        robot.start()
        self.assertTrue(robot.running)
        robot.stop()
        self.assertFalse(robot.running)
    
    def test_update(self):
        """Test robot update cycle."""
        robot = LineFollower()
        robot.start()
        robot.update()  # Should not raise any exceptions
        robot.stop()


if __name__ == "__main__":
    unittest.main()
