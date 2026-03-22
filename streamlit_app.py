import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Job Data Visualization Dashboard")


file_path = "dataset/show_visualization_data.csv"
# Load filtered data
df = pd.read_csv(file_path)

st.write("### Data Preview")
st.dataframe(df)

# Graph 1: Company vs job count
st.write("### company vs job count")
st.bar_chart(df,x="company",y="jobs",color="#ffaa00")

# Graph 2: Company vs Rating
st.write("### Company vs Ratings")
st.bar_chart(df,x="company",y="ratings",color="#0f713b")

# Graph 3: Rating Distribution (Histogram)
st.write("### Rating Distribution (Histogram)")

fig, ax = plt.subplots()
ax.hist(df['ratings'],color="#ffaa00")
plt.xlabel("Rating")
plt.ylabel("Frequency")
st.pyplot(fig)

# Graph 4: Company vs Reviews
st.write("### Company vs Reviews")
st.bar_chart(df,x="company",y="reviews",color="#670956")

# Graph 5: Company vs Salary
st.write("### Company vs Salary")
st.bar_chart(df,x="company",y="salaries",color="#BA1717")

# Graph 6: Reviews Distribution (Histogram)
st.write("### Reviews Distribution (Histogram)")

fig, ax = plt.subplots()
ax.hist(df['reviews'],color="#DA5DC3")
plt.xlabel("Reviews")
plt.ylabel("Frequency")
st.pyplot(fig)

# Graph 6: Salary Distribution (Histogram)
st.write("### Salary Distribution (Histogram)")

fig, ax = plt.subplots()
ax.hist(df['salaries'],color="#BA1717")
plt.xlabel("Salary")
plt.ylabel("Frequency")
st.pyplot(fig)
