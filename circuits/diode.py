import streamlit as st
import schemdraw
from schemdraw import elements as elm
import matplotlib.pyplot as plt
import math

st.title("Diodes")
st.write("""A diode is a two-terminal electronic component that conducts the current primarily in one direction.
It has low (ideally zero) resistance in one direction and high (ideally infinite) resistance in the other.
-- [Wikipedia](https://en.wikipedia.org/wiki/Diode)""")

@st.cache_data
def draw_circuit():
    with schemdraw.Drawing() as d:
        V1 = elm.SourceV().label('$V_{DD}$')
        elm.Line().right(d.unit*.5)
        R = elm.Resistor().right().label('R')
        elm.Line().right(d.unit*.5).at(R.end)
        elm.Diode().down().label(['+','$v_D$','-'])
        elm.Line().to(V1.start)


    d.draw()
    st.pyplot(plt.gcf())

draw_circuit()

v_DD = st.slider(r'$v_i (\mathrm V)$', 0.0, 10.0, 1.0)
R = st.slider(r'$R (\Omega)$', 1.0, 1e3, 10.0)

I_D = (v_DD-0.7)/R
I_S = I_D*math.exp(-0.7/0.025)
st.write('#### Diode Current:')
st.write(f'$I_D = {I_D:.2f}' + r'\mathrm A$')
st.write('#### Reverse-bias Saturation Current:')
st.write(f'$I_S = {I_S}' + r'\mu\mathrm{A}$')

st.header('Description')
st.latex(r'''
        I_D=I_S e^{(V_D/V_T)}
        ''')
st.latex(r'''
        I_D=\frac{V_{DD}-V_D}{R}
        ''')
