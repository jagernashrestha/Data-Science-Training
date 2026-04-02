import streamlit as st
import requests
# uv run streamlit run app.py OR uv run streamlit run app.py --server.port 8501
# uv venv 
st.set_page_config(
    page_title = "Our Streamlit App",
    page_icon = ":heart:"
)

st.write("I'M Jagerna Shova Shrestha and this is my first web page using streamlit!")
st.markdown("<h1> Welcome to my web page </h1>", unsafe_allow_html=True)
st.markdown("""
<style>
button{
    color:white;
    background: red;
    border: 1px solid #ccc;
    border-radius:12x;
    padding:10px;
    width:100px;
    }
</style>
<button> Click </button>
""",unsafe_allow_html=True)
name  = st.text_input("Enter your name")
st.number_input("Enter your age",min_value = 0, max_value = 100, value = 25 , step = 1)
st.markdown("---")
if st.button("Submit"):
    st.success("Thank you for submitting!")
    st.write("success")
    st.error("error")
r = requests.get("http://localhost:8000/items")
r.status_code
st.write(r.json())
for items in r.json():
    st.write(items["name"])
# 