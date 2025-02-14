import streamlit as st


def main():
    home_page = st.Page("circuits/home.py", title="Home", icon=":material/home:")
    kvl_kcl_page = st.Page("circuits/kvl_kcl.py", title="Kirchhoff's Voltage/Current Law")
    passive_filter_page = st.Page("circuits/passive_filters.py", title="Passive Filters")
    first_order_active_filter_page = st.Page("circuits/first_order_active_filters.py", title="First-Order Active Filters")
    op_amp_page = st.Page("circuits/op_amp.py", title="Operational Amplifiers")
    diode_page = st.Page("circuits/diode.py", title="Diodes")
    mosfet_page = st.Page("circuits/mosfet.py", title="MOSFET")
    common_source_amp_page = st.Page("circuits/common_source_amp.py", title="Common Source Amplifier")
    pg = st.navigation([home_page,
                        kvl_kcl_page,
                        passive_filter_page,
                        first_order_active_filter_page,
                        op_amp_page,
                        diode_page,
                        mosfet_page,
                        common_source_amp_page])
    pg.run()


if __name__ == '__main__':
    main()
