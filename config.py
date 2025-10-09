# Big Black Line Follower 202 - Configuration

# PID Controller Settings
PID_KP = 0.5  # Proportional gain
PID_KI = 0.0  # Integral gain
PID_KD = 0.1  # Derivative gain

# Motor Settings
BASE_SPEED = 100  # Base motor speed (0-255)
MAX_SPEED = 200   # Maximum motor speed
MIN_SPEED = 50    # Minimum motor speed

# Sensor Settings
NUM_SENSORS = 5   # Number of line sensors
SENSOR_THRESHOLD = 512  # Threshold for black/white detection (0-1023)

# Control Settings
UPDATE_RATE = 100  # Control loop update rate (Hz)
