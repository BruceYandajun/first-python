import streamlit as st


st.markdown('#Streamlit is **_really_ cool**.')

st.title("Title")
st.header("Header")
st.subheader("Sub header")
st.caption("Caption")
code = '''def hello():
     print("Hello, Streamlit!")'''
st.code(code, language='python')
st.text("This is some text")
