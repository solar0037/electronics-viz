import streamlit as st


def main():
    home_page = st.Page("circuits/home.py", title="Home", icon=":material/home:")
    rc_lpf_page = st.Page("circuits/rc_lpf.py", title="RC LPF")
    rl_hpf_page = st.Page("circuits/rl_hpf.py", title="RL HPF")
    op_amp_page = st.Page("circuits/op_amp.py", title="Op Amp")
    diode_page = st.Page("circuits/diode.py", title="Diodes")
    mosfet_page = st.Page("circuits/mosfet.py", title="MOSFET")
    common_source_amp_page = st.Page("circuits/common_source_amp.py", title="Common Source Amplifier")
    pg = st.navigation([home_page, rc_lpf_page, rl_hpf_page, op_amp_page, diode_page, mosfet_page, common_source_amp_page])
    pg.run()


if __name__ == '__main__':
    main()
