"""Standalone launcher for student-performance."""
import sys
from pathlib import Path
import streamlit as st

sys.path.insert(0, str(Path(__file__).resolve().parent))
from app import render_student_performance_page

if __name__ == "__main__":
    st.set_page_config(layout="wide")
    render_student_performance_page()
