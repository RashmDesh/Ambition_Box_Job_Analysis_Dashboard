import pandas as pd
from flask import Flask, redirect, render_template, request
import os


app = Flask(__name__)

# Load CSV
file_path = "dataset/Ambition_job_output.csv"
df = pd.read_csv(file_path)
print(df.head())

@app.route('/')
def index():
    # locations and industries for dropdowns
    locations = df['location'].value_counts().head(10).index.tolist()
    industries = df['Industry'].value_counts().head(10).index.tolist()
    return render_template('index.html', locations=locations, industries=industries)

@app.route('/results', methods=['POST'])
def results():
    location = request.form.get('location')
    industry = request.form.get('industry')
    rating = request.form.get('rating')
    view_type = request.form.get('view')

    copy_df = df.copy()

    if location != 'All':
        copy_df = copy_df[copy_df['location'] == location]

    if industry != 'All':
        copy_df = copy_df[copy_df['Industry'] == industry]

    if rating:
        copy_df = copy_df[copy_df['ratings'] >= float(rating)]

    print("Filtered DataFrame:")
    print(copy_df.head())

    # Save visualization data for Streamlit
    copy_df.to_csv('dataset/show_visualization_data.csv', index=False)
    print("data saved to ../dataset/show_visualization_data.csv")

    '''
    if view_type == 'table':
        data = copy_df.to_dict(orient='records')
        print(data)

        return render_template('table.html', data=data)
    else:
    '''
    return redirect("http://localhost:8501")  # Streamlit app URL
       
if __name__ == '__main__':
    app.run(debug=True)