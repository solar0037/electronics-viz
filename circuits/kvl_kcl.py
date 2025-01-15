import streamlit as st
import schemdraw
from schemdraw import elements as elm
import matplotlib.pyplot as plt

st.title("KVL/KCL (Kirchhoff's Voltage/Current Law)")
st.write("""Kirchhoff's circuit laws are two equalities that deal with the current and voltage in electrical circuits.
Kirchhoff's voltage law states that the algebraic sum of all voltages around a closed path (or loop) is zero.
Kirchhoff's current law states that the algebraic sum of all currents around a node (or a closed boundary) is zero.
-- [Wikipedia](https://en.wikipedia.org/wiki/Kirchhoff%27s_circuit_laws)""")

st.write(r'KVL: $\sum{V} = 0$')
st.write(r'KCL: $\sum{I} = 0$')

@st.cache_data
def draw_kvl_circuit():
    with schemdraw.Drawing() as d:
        elm.SourceV().label(['-','$V$','+'])
        elm.Resistor().right(d.unit*1.5).label(['+','$V_1$','-'])
        elm.Resistor().down().label(['+','$V_2$','-'], loc='bot')
        elm.Line().left(d.unit*1.5)
    st.pyplot(plt.gcf())


@st.cache_data
def draw_kcl_circuit():
    with schemdraw.Drawing() as d:
        elm.SourceV()
        L1 = elm.Line().right()
        elm.CurrentLabel().right().at(L1).label('$I_1$')
        R1 = elm.Resistor()
        elm.CurrentLabel().right().at(R1).label('$I_2$')
        elm.Line().down()
        elm.Line().left()
        R2 = elm.Resistor().down().at(L1.end)
        elm.CurrentLabel().down().at(R2).label('$I_3$')
        elm.Line().left()
    st.pyplot(plt.gcf())

st.header('KVL (Kirchhoff\'s Voltage Law)')
draw_kvl_circuit()
st.write(r'$V = 5\mathrm{V}$')
st.write('$V = V_1 + V_2$')
V_1 = st.slider(r'$V_1 (\mathrm{V})$', 0.0, 5.0, 1.0)
st.write('$V_2 = ' + f'{5-V_1:.2f}' + r'\mathrm{V}$')

st.header('KCL (Kirchhoff\'s Current Law)')
draw_kcl_circuit()
st.write(r'$I_1 = 0.1\mathrm{mA}$')
st.write('$I_1 = I_2 + I_3$')
I_2 = st.slider(r'$I_2 (\mathrm{mA})$', 0.0, 0.1, 0.01)
st.write('$I_3 = ' + f'{0.1-I_2:.2f}' + r'\mathrm{mA}$')
