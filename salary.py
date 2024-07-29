import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

st.set_page_config(page_title="salary", page_icon=None, layout="wide")

# Sidebar header and image
st.sidebar.header("Salaries in Some Jobs")
st.sidebar.write(" ")
st.sidebar.image("salary.jpeg")

info_filter = st.sidebar.selectbox("information for all charts", [None , "Company Name", "Rating", "Employment Status", "Salaries Reported"])
st.sidebar.write("")

raw_filter = st.sidebar.selectbox("raw filter for scatter chart", [None, "Rating", "Employment Status", "Salaries Reported"])
col_filter = st.sidebar.selectbox("col filter for scatter chart", [None, "Rating", "Employment Status", "Salaries Reported"])
st.sidebar.write("")
st.sidebar.write("made with :heart_eyes: by Eng. [Tasneem Ismail](https://github.com/dashboard) :sparkles:")

# Reading the dataset
df = pd.read_csv("Salary_Dataset_with_Extra_Features.csv")
df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')
df.dropna(subset=['Salary'], inplace=True)

df2 = df.copy()

# Creating columns for metrics
a1, a2, a3 = st.columns(3)

# Grouping by 'Job Title' and getting the maximum salary
grouped_max = df2.groupby('Job Title')['Salary'].max()

# Displaying metrics
a1.metric("Maximum Salary in Advanced Python Developer", grouped_max.get("Advanced Python Developer", "N/A"))
#a2.metric("Maximum Salary in AVP-Java Developer", grouped_max.get("AVP-Java Developer", "N/A"))
#a3.metric("Maximum Salary in Advanced Database Administrator", grouped_max.get("Advanced Database Administrator", "N/A"))

df = df.sample(n=20)
st.header("some information about random samples")
st.write(" ")
st.write(df)

st.subheader("Salary Vs Job Title")

# Creating the scatter plot
fig = px.scatter(df, x='Job Title', y='Salary', color=info_filter, facet_row=raw_filter, facet_col=col_filter)
# Rotating x-axis labels
fig.update_layout(xaxis_tickangle=90, height=800)
if (raw_filter=="Rating"):
    fig.update_layout(xaxis_tickangle=90, height=1400)
# if (raw_filter=="Company Name"):
#     fig.update_layout(xaxis_tickangle=90, height=3600)
# Setting a new range for y-axis dynamically based on the data

fig.update_yaxes(range=[1000, 450000])
st.plotly_chart(fig, use_container_width=True)

st.write("")
st.subheader("Rating Vs Salary")
fig1 = px.pie(df, names='Rating', values='Salary', color=info_filter)
st.plotly_chart(fig1, use_container_width=True)

st.write("")

c1, c2 = st.columns((5, 5))
with c1:
    st.subheader("Employment Status vs. Salary")
    fig = px.pie(df, names="Employment Status", values="Salary", color=info_filter, hole=.3)
    st.plotly_chart(fig, use_container_width=True)

with c2:
    st.subheader("Company Name vs. Salary")
    fig = px.bar(df, x="Company Name", y="Salary", color=info_filter)
    st.plotly_chart(fig, use_container_width=True)



