"""
Big Black Line Follower 202

A modular line-following robot implementation with PID control.
"""

from bblf202 import (
    PIDController,
    LineSensor,
    MotorController,
    LineFollower
)

__version__ = "1.0.0"
__all__ = ["PIDController", "LineSensor", "MotorController", "LineFollower"]
