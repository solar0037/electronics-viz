import streamlit as st
import schemdraw
from schemdraw import elements as elm
import matplotlib.pyplot as plt
import numpy as np
import math

@st.cache_data
def draw_plots():
    with schemdraw.Drawing() as d:
        op1 = elm.Opamp(leads=True)
        elm.Line().down(d.unit/4).at(op1.in2)
        elm.Ground(lead=False)
        R1 = elm.Resistor().at(op1.in1).left().label('$R$', loc='top').label('$v_{i}$', loc='left')
        elm.Line().up(d.unit/2).at(op1.in1)
        C1 = elm.Capacitor().right(d.unit*1.125).label('$C_1$')
        elm.Line().up(d.unit/2).at(C1.start)
        R2 = elm.Resistor().tox(op1.out).label('$R$')
        elm.Line().toy(op1.out)
        Line1 = elm.Line().right(d.unit/4).at(op1.out)

        R3 = elm.Resistor().right(d.unit*0.5).label('$R$')
        C2 = elm.Capacitor().right(d.unit*0.5).label('$C_2$')
        op2 = elm.Opamp(leads=True).anchor('in1')
        elm.Line().down(d.unit/4).at(op2.in2)
        elm.Ground(lead=False)
        elm.Line().up(d.unit/2).at(C2.end)
        R4 = elm.Resistor().tox(op2.out).label('$R$')
        elm.Line().toy(op2.out)

        Ri = elm.Resistor().right(d.unit).at(op2.out).label('$R_i$')
        op3 = elm.Opamp(leads=True).anchor('in1')
        elm.Line().down(d.unit/4).at(op3.in2)
        elm.Ground(lead=False)
        elm.Line().up(d.unit/2).at(op3.in1)
        Rf = elm.Resistor().tox(op3.out).label('$R_f$')
        elm.Line().toy(op3.out)
        elm.Line().right(d.unit/4).at(op3.out).label('$v_{o}$', loc='right')

    d.draw()
    st.pyplot(plt.gcf())

    cols = st.columns(2)

    frequencies = np.logspace(0, 6, 1000)
    omega = 2 * np.pi * frequencies

    V_in = 1
    R = 1e3
    Ri = 1e2
    Rf = 1e3
    C1 = 10e-9
    C2 = 10e-9
    f_1 = 1 / (2*math.pi*R*C1)
    f_2 = 1 / (2*math.pi*R*C2)
    f_0 = math.sqrt(f_1*f_2)

    H = (-1 / (1 + 1j*omega*C1*R)) * (-1j*omega*C2*R / (1 + 1j*omega*C2*R)) * (-Rf / Ri)
    magnitude = np.abs(H)
    phase = np.angle(H, deg=True)

    plt.clf()
    plt.semilogx(frequencies, magnitude, label=r'$|H|$')
    plt.axvline(f_0, color='r', linestyle='--', label='Center Frequency')
    plt.title("Transfer Function ($|H|$)")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("|H| (V/V)")
    plt.legend()

    cols[0].pyplot(plt.gcf())
    plt.clf()

    plt.semilogx(frequencies, phase, label=r'$θ$')
    plt.axvline(f_0, color='r', linestyle='--', label='Center Frequency')
    plt.title("Phase Angle (θ)")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("θ (˚)")
    plt.legend()

    cols[1].pyplot(plt.gcf())


def transfer_function(f: int | float) -> list[float, float]:
    V_in = 1
    R = 1e3
    Ri = 1e2
    Rf = 1e3
    C1 = 10e-9
    C2 = 10e-9
    f_1 = 1 / (2*math.pi*R*C1)
    f_2 = 1 / (2*math.pi*R*C2)
    f_0 = math.sqrt(f_1*f_2)
    omega = 2*math.pi*f

    H = (-1 / (1 + 1j*omega*C1*R)) * (-1j*omega*C2*R / (1 + 1j*omega*C2*R)) * (-Rf / Ri)
    magnitude = np.abs(H)
    phase = np.angle(H, deg=True)
    return magnitude, phase


def draw_sliders():
    f = st.select_slider(r'$f (\mathrm Hz)$', [1, 10, 1e2, 1e3, 1e4, 15.92e3, 1e5, 1e6])
    res = transfer_function(f)
    st.write(f'#### Signal Attenuation: {'Yes' if f!=15.92e3 else 'No'}')
    st.write(r'$H(f) = ' + f'{res[0]:.2f}' + r' \mathrm V/\mathrm V$')
    st.write(r'$\theta = ' + f'{int(res[1])}' + r' \mathrm \degree$')
    st.write('### Parameters')
    st.write(r'$R = 1\mathrm k \Omega$')
    st.write(r'$R_i = 100\mathrm \Omega$')
    st.write(r'$R_f = 1\mathrm k \Omega$')
    st.write(r'$C_1 = 10 \mathrm n \mathrm F$')
    st.write(r'$C_2 = 10 \mathrm n \mathrm F$')
    st.write(r'$f_c = 15.92\mathrm{kHz}$')
