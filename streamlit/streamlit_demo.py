import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Job Data Visualization Dashboard")

file_path = "../dataset/Ambition_job_output.csv"

# Load filtered data
df = pd.read_csv(file_path)

st.write("### Data Preview")
st.dataframe(df)

# Graph 1: Jobs by Location
st.write("### Jobs by Location")
loc_counts = df['location'].value_counts()
st.bar_chart(loc_counts)

# Graph 2: Jobs by Industry
st.write("### Jobs by Industry")
ind_counts = df['Industry'].value_counts()
st.bar_chart(ind_counts)

# Graph 3: Company vs Rating Distribution
st.write("### Company vs Average Rating")

company_rating = df.groupby('company')['ratings'].mean().sort_values(ascending=False).head(10)
st.dataframe(company_rating)

fig, ax = plt.subplots()
company_rating.plot(kind='bar', ax=ax,color='red')
plt.xticks(rotation=45)
plt.ylabel("Average Rating")
plt.xlabel("Company")

st.pyplot(fig)

# Graph 4: Industry vs Average Rating
st.write("### Industry vs Average Rating")

industry_rating = df.groupby('Industry')['ratings'].mean().sort_values(ascending=False).head(10)
st.dataframe(industry_rating)

fig, ax = plt.subplots()
industry_rating.plot(kind='bar', ax=ax,color='red')
plt.xticks(rotation=45)
plt.ylabel("Average Rating")
plt.xlabel("Industry")

st.pyplot(fig)