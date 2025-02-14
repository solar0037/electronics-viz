import streamlit as st
from circuits.filters import passive_lpf, passive_hpf, passive_bpf, passive_bsf

def init_session():
    st.title("Passive Filters")
    st.write("""In signal processing, a filter is a device that removes some unwanted components or features from a signal.
    -- [Wikipedia](https://en.wikipedia.org/wiki/Filter_(signal_processing))""")
    st.write("""A passive filter is a kind of electronic filter that is made only from passive components - in contrast to an active filter, it does not require an external power source.
    -- [Wikipedia](https://en.wikipedia.org/wiki/Passivity_(engineering)#Passive_filter)""")
    if 'filter_type' not in st.session_state.keys():
        st.session_state['filter_type'] = 0

def draw_buttons():
    buttons = st.columns(4)
    titles = ['Low-Pass Filter',
              'High-Pass Filter',
              'Band-Pass Filter',
              'Band-Stop Filter']
    keys = ['lpf', 'hpf', 'bpf', 'bsf']
    current_filter_type = st.session_state['filter_type']
    if current_filter_type == 0:
        passive_lpf.draw_plots()
        passive_lpf.draw_sliders()
    elif current_filter_type == 1:
        passive_hpf.draw_plots()
        passive_hpf.draw_sliders()
    elif current_filter_type == 2:
        passive_bpf.draw_plots()
        passive_bpf.draw_sliders()
    elif current_filter_type == 3:
        passive_bsf.draw_plots()
        passive_bsf.draw_sliders()
    for i in range(4):
        buttons[i].button(titles[i], key=keys[i], on_click=on_click_button, args=(i,))

def on_click_button(i):
    st.session_state['filter_type'] = i

init_session()
draw_buttons()
