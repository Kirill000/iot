# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def f(t, v):
    return np.sin(v*np.cos(2*np.pi*t))

inp = int(input())

t = np.linspace(0, inp, 1)
v_values = np.linspace(1, 10, 100)
spectral_weights = []

for v in v_values:
    signal = f(t, v)
    spectrum = np.abs(np.fft.fft(signal))
    spectral_weights.append(np.max(spectrum))

max_weight_index = np.argmax(spectral_weights)
max_weight_freq = v_values[max_weight_index]

print(round(max_weight_freq, 0))