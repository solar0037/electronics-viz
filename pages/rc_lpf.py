import streamlit as st
import schemdraw
from schemdraw import elements as elm
import matplotlib.pyplot as plt
import numpy as np
import math

st.title("RC LPF")

with schemdraw.Drawing() as d:
    V = elm.SourceV().label('$v_{i}$')
    Res = elm.Resistor().right().label('R')
    Cap = elm.Capacitor().down(d.unit).at(Res.end).label('C')
    elm.Line().to(V.start)
    plus = elm.Line().right(d.unit/2).at(Res.end).dot(open=True)
    elm.Gap().down().label(['+','$v_C$','-']).at(plus.end)
    elm.Line().right(d.unit/2).at(Cap.end).dot(open=True)

d.draw()
st.pyplot(plt.gcf())

cols = st.columns(2)

frequencies = np.logspace(0, 6, 1000)
omega = 2 * np.pi * frequencies

V_in = 1
R = 1e3
C = 10e-9
Z_C = 1 / (1j*omega*C)
f_c = 1/(2*math.pi*R*C)

H = Z_C / (R + Z_C)
magnitude = np.abs(H)
phase = np.angle(H, deg=True)

plt.clf()
plt.semilogx(frequencies, magnitude, label=r'$|H|$')
plt.axvline(f_c, color='r', linestyle='--', label='Cutoff Frequency')
plt.title("Transfer Function ($|H|$)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("|H| (V/V)")
plt.legend()

cols[0].pyplot(plt.gcf())

plt.figure(2)
plt.semilogx(frequencies, phase, label=r'$θ$')
plt.axvline(f_c, color='r', linestyle='--', label='Cutoff Frequency')
plt.title("Phase Angle (θ)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("θ (˚)")
plt.legend()

cols[1].pyplot(plt.gcf())
