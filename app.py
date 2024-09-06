import streamlit as st
import warnings
from Topics.pure_math import quadratic_demo, transformation_demo

# Suppress warnings
warnings.filterwarnings('ignore')


st.set_page_config(page_title="Math Visualizations", layout="wide")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Set dark theme
st.markdown("""
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        background-color: #2E2E2E;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        background-color: #2E2E2E;
    }
    </style>
    """, unsafe_allow_html=True)

# Set the maximum width of the main content
st.markdown('''
    <style>
        .main .block-container {
            max-width: 1200px;  # Adjust this value as needed
        }
    </style>
''', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown('<p class="sidebar-title">TOPICS</p>', unsafe_allow_html=True)
    
    with st.expander("Pure Mathematics", expanded=True):
        demo_options = [
            "Quadratic Function",
            "Function Transformations",
        ]
        
        selected_demo = st.radio("placeholder", demo_options, label_visibility="hidden")

    # Add a separator
    st.markdown('<div class="sidebar-separator"></div>', unsafe_allow_html=True)

# Main content
if selected_demo == "Quadratic Function":
    st.markdown("<h1>Quadratic Function Visualization</h1>", unsafe_allow_html=True)
    quadratic_demo()
elif selected_demo == "Function Transformations":
    st.markdown("<h1>Function Transformations Visualization</h1>", unsafe_allow_html=True)
    transformation_demo()
else:
    st.header(f"{selected_demo} Demo")
    st.write("This demo is not implemented yet.")

