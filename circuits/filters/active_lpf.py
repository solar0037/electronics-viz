import streamlit as st
import schemdraw
from schemdraw import elements as elm
import matplotlib.pyplot as plt
import numpy as np
import math

@st.cache_data
def draw_plots():
    with schemdraw.Drawing() as d:
        op = elm.Opamp(leads=True)
        elm.Line().down(d.unit/4).at(op.in2)
        elm.Ground(lead=False)
        Ri = elm.Resistor().at(op.in1).left().label('$R_{i}$', loc='top').label('$v_{i}$', loc='left')
        elm.Line().up(d.unit/2).at(op.in1)
        Cf = elm.Capacitor().right(d.unit*1.125).label('$C_f$')
        elm.Line().up(d.unit/2).at(Cf.start)
        Rf = elm.Resistor().tox(op.out).label('$R_f$')
        elm.Line().toy(op.out)
        elm.Line().right(d.unit/4).at(op.out).label('$v_{o}$', loc='right')

    d.draw()
    st.pyplot(plt.gcf())

    cols = st.columns(2)

    frequencies = np.logspace(0, 6, 1000)
    omega = 2 * np.pi * frequencies

    V_in = 1
    Ri = 1e2
    Rf = 1e3
    C = 10e-9
    Z_C = 1 / (1j*omega*C)
    f_c = 1/(2*math.pi*Rf*C)

    H = -(Rf / Ri) * Z_C / (Rf + Z_C)
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
    plt.clf()

    plt.semilogx(frequencies, phase, label=r'$θ$')
    plt.axvline(f_c, color='r', linestyle='--', label='Cutoff Frequency')
    plt.title("Phase Angle (θ)")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("θ (˚)")
    plt.legend()

    cols[1].pyplot(plt.gcf())


def transfer_function(f: int | float) -> list[float, float]:
    V_in = 1
    Ri = 1e2
    Rf = 1e3
    C = 10e-9
    Z_C = 1 / (1j*2*math.pi*f*C)

    H = -(Rf / Ri) * Z_C / (Rf + Z_C)
    magnitude = abs(H) / V_in
    phase = np.angle(H, deg=True)
    return magnitude, phase


def draw_sliders():
    f = st.select_slider(r'$f (\mathrm Hz)$', [1, 10, 1e2, 1e3, 1e4, 15.92e3, 1e5, 1e6])
    res = transfer_function(f)
    st.write(f'#### Signal Attenuation: {'Yes' if f>1e3 else 'No'}')
    st.write(r'$H(f) = ' + f'{res[0]:.2f}' + r' \mathrm V/\mathrm V$')
    st.write(r'$\theta = ' + f'{int(res[1])}' + r' \mathrm \degree$')
    st.write(r'$K = 10$')
    st.write('### Parameters')
    st.write(r'$R_i = 100\mathrm \Omega$')
    st.write(r'$R_f = 1\mathrm k \Omega$')
    st.write(r'$C_f = 10 \mathrm n \mathrm F$')
    st.write(r'$f_c = 15.92\mathrm{kHz}$')
