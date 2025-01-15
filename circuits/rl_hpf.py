import streamlit as st
import schemdraw
from schemdraw import elements as elm
import matplotlib.pyplot as plt
import numpy as np
import math

st.title("RL High-pass Filter")
st.write("""A high-pass filter (HPF) is an filter that passes signals with a frequency higher than a certain cutoff frequency and attenuates signals with frequencies lower than the cutoff frequency.
A resistor and either a capacitor or an inductor can be configured as a first-order high-pass filter.
-- [Wikipedia](https://en.wikipedia.org/wiki/High-pass_filter)""")


@st.cache_data
def draw_plots():
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
    plt.clf()

    plt.semilogx(frequencies, phase, label=r'$θ$')
    plt.axvline(f_c, color='r', linestyle='--', label='Cutoff Frequency')
    plt.title("Phase Angle (θ)")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("θ (˚)")
    plt.legend()

    cols[1].pyplot(plt.gcf())


draw_plots()


def transfer_function(f: int | float) -> list[float, float]:
    V_in = 1
    R = 1e3
    L = 10e-3
    Z_L = 1j*2*math.pi*f*L

    H = Z_L / (R + Z_L)
    magnitude = abs(H) / V_in
    phase = np.angle(H, deg=True)
    return magnitude, phase


f = st.select_slider(r'$f (\mathrm Hz)$', [1, 10, 1e2, 1e3, 1e4, 15.92e3, 1e5, 1e6])
res = transfer_function(f)
st.write(f'#### Signal Attenuation: {'Yes' if f<1e5 else 'No'}')
st.write(r'$H(f) = ' + f'{res[0]:.2f}' + r' \mathrm V/\mathrm V$')
st.write(r'$\theta = ' + f'{int(res[1])}' + r' \mathrm \degree$')
st.write('### Parameters')
st.write(r'$R = 1\mathrm k \Omega$')
st.write(r'$L = 10 \mathrm m \mathrm H$')
st.write(r'$f_c = 15.92\mathrm{kHz}$')
