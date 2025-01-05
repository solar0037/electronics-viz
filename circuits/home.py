import streamlit as st

st.set_page_config("전자회로 설명서")
language_options = ['English', '한국어']
language = st.selectbox('Language', language_options)
if language == language_options[0]:
    st.title("Electronics Handbook")
    st.write("Visually interactive analog/digital circuits.")
    st.write("Tech Stack: Python, Streamlit, Schemdraw 등")
else:
    st.title("전자회로 설명서")
    st.write("아날로그/디지털 회로를 시각적으로 상호작용할 수 있게 만든 프로젝트입니다.")
    st.write("사용 기술: Python, Streamlit, Schemdraw 등")
st.link_button("GitHub", "https://github.com/solar0037/electronics-viz")
