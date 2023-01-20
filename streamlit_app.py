import streamlit as st
from streamlit.components.v1 import html
import numpy as np
from model import Model

# Set wide display
st.set_page_config(layout="wide")

# Selection of visualization type and function
c1, c2, c3 = st.columns(3)
f_sel = c1.selectbox("Function:", ["cos(z)","exp(z)", "Custom"])
viz_sel = c2.selectbox("Visualization Type:", ["circles", "grid", ""])
do_viz = c3.button("Show me!")
if f_sel == "cos(z)":
    f_formula = "f = lambda z: np.cos(z)"
    f = lambda z: np.cos(z)
elif f_sel == "exp(z)":
    f_formula = "f = lambda z: np.exp(z)"
    f = lambda z: np.exp(z)
elif f_sel=="Custom":
    msg = """# Use standard python and numpy notation. Modify the example provided.
def f(z):
    f_z = 2*z
    return f_z"""
    f_formula = c1.text_area("Formula:", msg, height=200)
    eval(f_formula)

# Initialize
if do_viz:
    m = Model(f, "circle", {})
    #z = 1+2j
    #st.write(f(z))