import streamlit as st
from circuits.filters import active_lpf, active_hpf, active_bpf, active_bsf

def init_session():
    st.title("First-Order Active Filters")
    st.write("""An active filter is a type of analog circuit implementing an electronic filter using active components, typically an amplifier.
    Amplifiers included in a filter design can be used to improve the cost, performance and predictability of a filter.
    -- [Wikipedia](https://en.wikipedia.org/wiki/Active_filter)""")
    if 'first_order_active_filter_type' not in st.session_state.keys():
        st.session_state['first_order_active_filter_type'] = 0

def draw_buttons():
    buttons = st.columns(4)
    titles = ['Low-Pass Filter',
              'High-Pass Filter',
              'Band-Pass Filter',
              'Band-Stop Filter']
    keys = ['lpf', 'hpf', 'bpf', 'bsf']
    current_filter_type = st.session_state['first_order_active_filter_type']
    if current_filter_type == 0:
        active_lpf.draw_plots()
        active_lpf.draw_sliders()
    elif current_filter_type == 1:
        active_hpf.draw_plots()
        active_hpf.draw_sliders()
    elif current_filter_type == 2:
        active_bpf.draw_plots()
        active_bpf.draw_sliders()
    elif current_filter_type == 3:
        active_bsf.draw_plots()
        active_bsf.draw_sliders()
    for i in range(4):
        buttons[i].button(titles[i], key=keys[i], on_click=on_click_button, args=(i,))

def on_click_button(i):
    st.session_state['first_order_active_filter_type'] = i

init_session()
draw_buttons()
