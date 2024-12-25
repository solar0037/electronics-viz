import streamlit as st
import schemdraw
from schemdraw import elements as elm
import matplotlib.pyplot as plt
import math

st.title("MOSFET")

cols = st.columns(2)

with schemdraw.Drawing() as d:
    NMOS = elm.AnalogNFet().reverse()
    elm.Label('G').at(NMOS.gate)
    elm.Label('S').at(NMOS.source)
    elm.Label('D').at(NMOS.drain)

d.draw()
cols[0].pyplot(plt.gcf())

v_GS = cols[1].slider('$v_{GS}$ (V)', 0.0, 5.0, 0.1)
v_DS = cols[1].slider('$v_{DS}$ (V)', 0.0, 5.0, 0.1)
V_t = 0.5
k_n = 2e-3
v_OV = v_GS - V_t
cols[1].latex('V_{t} = 0.5\mathrm{V}')
cols[1].latex('k_{n} = k\'_{n}(W/L) = 2\mathrm{mA/V^2}')
if v_GS<V_t:
    cols[1].write('MOSFET Operation: Cutoff Region')
    cols[1].write('Drain Current($i_{D}$) = 0mA')
else:
    if v_DS<v_OV:
        i_D = k_n*(v_OV*v_DS-0.5*v_DS**2)
        cols[1].write('MOSFET Operation: Triode Region')
    else:
        i_D = 0.5*k_n*v_OV**2
        cols[1].write('MOSFET Operation: Saturation Region')
    cols[1].write('Drain Current($i_{D}$) = ' + f'{i_D*1e3:.3f}mA')

with schemdraw.Drawing() as d:
    G = elm.Line().dot(open=True)
    elm.Label('G').at(G.start)
    elm.Dot(open=True).at(G.start)
    elm.Gap().down().label(['+','$v_{GS}$','-']).at(G.end)
    S = elm.Line().at((G.start[0], G.start[1]-d.unit)).right(d.unit*3).dot(open=True)
    Ss = elm.Line().down(d.unit/2).at((S.start[0]+d.unit*1.5, S.start[1]))
    elm.Label('S').at(Ss.end)
    elm.Dot(open=True).at(S.start)
    elm.Dot(open=True).at(Ss.end)
    VCCS = elm.SourceControlledI().at((S.end[0]-d.unit, S.end[1]+d.unit)).down().label(r'$\frac{1}{2}k_n v_{OV}^2$')
    D = elm.Line().right().at(VCCS.start).dot(open=True)
    elm.Label('D').at(D.end)

d.draw()
st.header('Equivalent Circuit')
st.pyplot(plt.gcf())

st.header('MOSFET Operation')
st.write('Triode Region ($v_{DS} < v_{OV}$)')
st.latex(r'''
i_{D}=k_{n}(v_{OV}v_{DS}-\frac{1}{2}v_{DS}^2)
''')
st.write('Saturation Region ($v_{DS} \ge v_{OV}$)')
st.latex(r'''
i_{D}=\frac{1}{2}k_{n}v_{OV}^2
''')
st.write('where')
st.latex(r'v_{OV}=v_{GS}-V_{t}')
st.latex(r"k_{n}=k^{'}_{n}(W/L)=\mu_{n}C_{ox}(W/L)")
