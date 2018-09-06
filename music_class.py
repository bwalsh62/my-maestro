# -*- coding: utf-8 -*-
"""
Classes to instantiate a tone, with a default
length of time = 1 second, sampling
frequency of 44.1kHz and an input
fundamental frequency

# Usage:
    from music_class import tone
    f0 = 400
    tone1 = tone(f0)
# To hear the tone:
    tone1.playTone()

Future Work:
    Align melody and tone class

Created on Tue Aug 14 22:22:37 2018
Last updated: September 5, 2018

Author: Benjamin Walsh
"""

#%% Import standard libraries

from scipy.io.wavfile import write
import numpy as np
import winsound as ws

#%% Import custom libraries

import music_helper_functions as mus

#%% Tone class

class tone:
    
    fs = 44100  # Sampling frequency in Hz
    
    def __init__(self, f0):        
        self.f0 = f0 # frequency in Hz
        self.time_len = 1 # time in seconds
        t_array = np.arange(self.time_len*self.fs)
        self.sin_wave = 5*np.sin(2*np.pi*self.f0*t_array/self.fs)
    
    def playTone(self):
        write('tone.wav',self.fs,np.int16(self.sin_wave)*1000)
        ws.PlaySound('tone.wav',0)
    
    def changeLength(self, new_time_len):
        self.time_len = new_time_len
        t_array = np.arange(self.time_len*self.fs)
        self.sin_wave = 5*np.sin(2*np.pi*self.f0*t_array/self.fs)
    
    def makeFlat(self):
        self.f0 = self.f0*(2**(-1/12))
        t_array = np.arange(self.time_len*self.fs)
        self.sin_wave = 5*np.sin(2*np.pi*self.f0*t_array/self.fs)
        
    def makeSharp(self):
        self.f0 = self.f0*(2**(1/12))
        t_array = np.arange(self.time_len*self.fs)
        self.sin_wave = 5*np.sin(2*np.pi*self.f0*t_array/self.fs)

#%% Melody class
        
class melody:
    
    #----------------------------------------
    # Eventually align with tone class
    #----------------------------------------
    
    fs = 44100  # Sampling frequency in Hz
    
    def __init__(self, note_list, key):        
        self.note_list = note_list # note array
        self.time_lens = 1 #np.ones(len(note_list)) # time array in seconds
        t_array = np.arange(self.time_lens*self.fs)
        
        # Convert notes (#s) to frequencies
        fc = 261.63 # assume C for now
        tone_step_list = mus.notes_to_step(note_list)
        freq_list = fc*np.power(2,(np.array(tone_step_list)-1)/12)
        
        # Initialize sin_wave
        self.sin_wave = list(5*np.sin(2*np.pi*freq_list[0]*t_array/self.fs))
        for f_idx in range(1,freq_list.shape[0]):
            self.sin_wave = np.concatenate((self.sin_wave, 5*np.sin(2*np.pi*freq_list[f_idx]*t_array/self.fs)),axis=0)
    
    def playMelody(self):
        write('melody.wav',self.fs,np.int16(self.sin_wave)*1000)
        ws.PlaySound('melody.wav',0)
    