# -*- coding: utf-8 -*-
"""
Classes to instantiate a tone, with a default
length of time = 1 second, sampling
frequency of 44.1kHz and an input
fundamental frequency

# Usage:
    from musicClass import tone
    f0 = 400
    tone1 = tone(f0)
# To hear the tone:
    tone1.playTone()

Future Work:
    Add melody class based on tone
    Add time length modification method

Created on Tue Aug 14 22:22:37 2018
Last updated: August 14, 2018

Author: Benjamin Walsh
"""

from scipy.io.wavfile import write
import numpy as np
import winsound as ws

class tone:
    
    time_len = 1 # time of tone in seconds
    fs = 44100  # Sampling frequency in Hz
    
    def __init__(self, f0):        
        self.f0 = f0 # frequency in Hz

    
    def playTone(self):
        t_array = np.arange(self.time_len*self.fs)
        # sine wave at f0
        sinWave = 5*np.sin(2*np.pi*self.f0*t_array/self.fs)

        write('tone.wav',self.fs,np.int16(sinWave)*1000)
        ws.PlaySound('tone.wav',0)
    
    