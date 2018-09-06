# -*- coding: utf-8 -*-
"""
Fundamental functions to support composing and playing music

Used in music_demo.py

Benjamin Walsh - September 2018
"""
#%% External libraries to import

import numpy as np

#%% Function for returning frequency (Hz) from input note

def note_to_f(note):
    
    mus_dict = {
        'A': 220.00,
        'B': 246.94,
        'C': 261.63,
        'D': 293.66,
        'E': 329.63,
        'F': 349.23,
        'G': 392.00
    }
    
    if mus_dict.get(note.capitalize())==None:
        print('Invalid note input!')
        return 0
    else:
        return mus_dict.get(note.capitalize())
    
    
#%% Function for returning fundamental frequency from waveform
    
def fundFreq(waveform,fs):
    # Initial draft just take max of FFT
    sp = np.fft.fft(waveform)
    idx = np.argmax(np.abs(sp))
    freqs = np.fft.fftfreq(waveform.shape[-1])
    return abs(freqs[idx]*fs)

#%% Function for returning step/half-step corresponding to relative note
    
def notes_to_step(note_num_list):
    step_list = np.zeros(len(note_num_list))
    for note_num in range(len(note_num_list)):
        step_list[note_num] = note_to_step(note_num_list[note_num])
    return step_list.tolist()

def note_to_step(note_num):
    return {
        1: 0,
        2: 2,
        3: 4,
        4: 5,
        5: 7,
        6: 9,
        7: 11
    }[note_num]