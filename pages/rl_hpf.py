import streamlit as st
import schemdraw
from schemdraw import elements as elm
import matplotlib.pyplot as plt
import numpy as np
import math

st.title("RL HPF")

with schemdraw.Drawing() as d:
    V = elm.SourceV().label('$v_{i}$')
    Res = elm.Resistor().right().label('R')
    Ind = elm.Inductor().down(d.unit).at(Res.end).label('L')
    elm.Line().to(V.start)
    plus = elm.Line().right(d.unit/2).at(Res.end).dot(open=True)
    elm.Gap().down().label(['+','$v_L$','-']).at(plus.end)
    elm.Line().right(d.unit/2).at(Ind.end).dot(open=True)

d.draw()
st.pyplot(plt.gcf())

cols = st.columns(2)

frequencies = np.logspace(0, 6, 1000)
omega = 2 * np.pi * frequencies

V_in = 1
R = 1e3
L = 10e-3
Z_L = 1j*omega*L
f_c = 1/(2*math.pi*(L/R))

H = Z_L / (R + Z_L)
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
