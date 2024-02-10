import numpy as np
import matplotlib.pyplot as plt

# Parameters
frequency = 5  # Frequency of the sinusoidal signal in Hz
amplitude = 1  # Amplitude of the sinusoidal signal
gain = 2  # Amplification factor

# Time vector
fs = 1000  # Sampling frequency in Hz
t = np.arange(0, 1, 1/fs)  # Time vector from 0 to 1 second

# Generate sinusoidal signal
sinusoidal_signal = amplitude * np.sin(2 * np.pi * frequency * t)

# Amplify the signal
amplified_signal = gain * sinusoidal_signal

# Plot original and amplified signals on a single graph
plt.figure(figsize=(10, 6))

plt.plot(t, sinusoidal_signal, 'b', label='Original Signal')
plt.plot(t, amplified_signal, 'r', label='Amplified Signal')
plt.title('Sinusoidal Signal and Amplified Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)

plt.show()
