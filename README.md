# Big Black Line Follower 202

A modular and extensible line-following robot implementation with PID control.

## Overview

The Big Black Line Follower 202 (bblf202) is a line-following robot controller that uses:
- **PID Control**: Smooth and accurate line following with configurable gains
- **Modular Design**: Separate sensor, motor, and control modules
- **Flexible Configuration**: Easy to adapt to different hardware setups

## Features

- **PID Controller**: Proportional-Integral-Derivative control for smooth operation
- **Line Sensor Interface**: Support for multiple sensor arrays
- **Motor Control**: Differential drive motor control with speed limiting
- **Configurable Parameters**: Easy tuning of control parameters

## Quick Start

### Basic Usage

```python
from bblf202 import LineFollower

# Create robot with default settings
robot = LineFollower()

# Run the robot
robot.run()
```

### Custom Configuration

```python
from bblf202 import LineFollower

# Create robot with custom PID values
robot = LineFollower(
    kp=0.6,           # Proportional gain
    ki=0.01,          # Integral gain
    kd=0.15,          # Derivative gain
    base_speed=120,   # Base motor speed
    num_sensors=5     # Number of sensors
)

# Run for specific duration
robot.run(duration=30)  # Run for 30 seconds
```

## Architecture

### PIDController
Implements a PID feedback controller for line following:
- `kp`: Proportional gain - responds to current error
- `ki`: Integral gain - eliminates steady-state error
- `kd`: Derivative gain - dampens oscillations

### LineSensor
Interface for reading line sensor array:
- Supports configurable number of sensors
- Calculates line position (-1.0 to 1.0)
- Returns weighted position based on sensor readings

### MotorController
Controls differential drive motors:
- Set individual motor speeds
- Apply speed and turn rate
- Automatic speed clamping to safe limits

### LineFollower
Main robot controller:
- Integrates all components
- Runs control loop at 100Hz
- Handles start/stop operations

## Configuration

Edit `config.py` to adjust default settings:

```python
# PID Settings
PID_KP = 0.5
PID_KI = 0.0
PID_KD = 0.1

# Motor Settings
BASE_SPEED = 100
MAX_SPEED = 200

# Sensor Settings
NUM_SENSORS = 5
```

## Testing

Run the test suite:

```bash
python test_bblf202.py
```

## Examples

See `example.py` for a complete usage example.

## Hardware Integration

To integrate with real hardware:

1. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Modify `LineSensor.read()` to read from your sensor hardware
3. Modify `MotorController.set_motors()` to control your motors

## License

MIT License - See LICENSE file for details

## Contributing

Contributions welcome! Please submit pull requests or open issues for bugs and feature requests.
