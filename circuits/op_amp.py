import streamlit as st
import schemdraw
import schemdraw.elements as elm
import matplotlib.pyplot as plt

st.title("Operational Amplifier")
st.write("""An operational amplifier (often op amp or opamp) is a DC-coupled electronic voltage amplifier with a differential input, a (usually) single-ended output, and an extremely high gain. Its name comes from original use of performing mathematical operations in analog computers.
-- [Wikipedia](https://en.wikipedia.org/wiki/Operational_amplifier)""")

@st.cache_data
def draw_circuit():
    with schemdraw.Drawing() as d:
        op = elm.Opamp(leads=True)
        elm.Line().down(d.unit/4).at(op.in2)
        elm.Ground(lead=False)
        Rin = elm.Resistor().at(op.in1).left().idot().label('$R_{1}$', loc='top').label('$v_{I}$', loc='left')
        elm.Line().up(d.unit/2).at(op.in1)
        elm.Resistor().tox(op.out).label('$R_2$')
        elm.Line().toy(op.out).dot()
        elm.Line().right(d.unit/4).at(op.out).label('$v_{o}$', loc='right')

    d.draw()
    st.pyplot(plt.gcf())

draw_circuit()

v_in = st.slider(r'$v_i (\mathrm V)$', -10.0, 10.0, 1.0)
r1 = st.slider(r'$R_1 (\Omega)$', 1, 10000, 1000)
r2 = st.slider(r'$R_2 (\Omega)$', 1, 10000, 1000)

v_out = (r2 / r1) * v_in
gain = r2 / r1
st.write('#### Output Voltage:')
st.write(r'$v_o = ' + f'{v_out:.2f}' + r'\mathrm V$')
st.write('#### Overal Voltage Gain:')
st.write(r'$G = ' + f'{gain:.2f}' + r'\mathrm V$')

st.header('Description')
st.latex(r'''
        v_{o}=-\frac{R_2}{R_1} v_i
        ''')
st.latex(r'''
        G\equiv\frac{v_o}{v_i}=-\frac{R_2}{R_1}
        ''')
