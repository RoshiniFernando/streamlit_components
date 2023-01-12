# Important libraries
import streamlit as st
import pandas as pd
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report

# Header text
st.header('**Streamlit Components**')
st.write("Components are third-party Python modules that extend what's possible with Streamlit")
st.write("Let's look at about, ")

# About the selected component
st.header('`streamlit_pandas_profiling`')
st.write("This provides a one-line Exploratory Data Analysis (EDA) experience in a consistent and fast solution")

# Creating dataframe
df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')

# About the dataset that used here
st.write('Here you can see a detailed report about the dataset https://github.com/dataprofessor/data/blob/master/penguins_cleaned.csv')

# Generate and Display Report
st.subheader('Report')
pr = df.profile_report()
st_profile_report(pr)