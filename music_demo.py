# -*- coding: utf-8 -*-
"""
Demo to write, visualize, and play tones and melodies with 
custom classes and functions

Uses functions from music_helper_functions.py 
and classes from music_class.py

Benjamin Walsh - September 2018
"""

#%% Import standard libraries

import numpy as np
import matplotlib.pyplot as plt

#%% Import custom classes/functions

from music_class import tone, melody
import music_helper_functions as mus

#%% Create and play tone

f0 = 500 # in Hz
tone1 = tone(f0)
tone1.playTone()
#---------------
# Can also write note
# Implement this next...
#-----------------

#%% Plot waveform

# Create array of time samples
t_array_len = tone1.time_len*tone1.fs
t_array = np.arange(t_array_len)

# Plot waveform over short time period to see sine
plt.plot(t_array/tone1.fs,tone1.sin_wave)
plt.show
plt.xlim(0 ,300/tone1.fs)
plt.xlabel('Time (s)')
plt.title('Sine wave at ' + str(tone1.f0) + ' hz')

#%% Fast Fourier Transform

# Take FFT of sine wave
sp = np.fft.fft(tone1.sin_wave)
freqs = np.fft.fftfreq(t_array.shape[-1])

# Plot FFT
plt.plot(freqs, sp.real)
plt.show

# Find dominant frequency
freq_from_func = mus.fundFreq(tone1.sin_wave,tone1.fs)
print('Frequency with highest amplitude = ' + str(freq_from_func))

#%% User input to play note
#   Example - Try C to play 261.63 Hz

note_to_play = input("Choose note to play: ")
tone2 = tone(mus.note_to_f(note_to_play))
tone2.playTone()

#%% Play beginning of Mary Had A Little Lamb

#---------------
# Should also put in rest... 0?
#-----------------

mel1 = melody([3,2,1,2,3,3,3,3,2,2,2,2,3,5,5,5],'c')
mel1.playMelody()





