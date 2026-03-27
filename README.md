Placement Prediction App

A simple web application to predict whether a student is likely to get placed based on CGPA, aptitude score, communication skills, and project experience.

Built with Flask (backend) and Streamlit (frontend) using a Logistic Regression model.

Features
Predict placement chances with a few inputs.
Interactive sliders for input values.
Returns instant prediction through a REST API.
Project Structure
├── app.py          # Flask backend API
├── frontend.py     # Streamlit frontend
├── model.pkl       # Trained Logistic Regression model
├── requirements.txt # Python dependencies
└── README.md       # Project description
How to Run
Install dependencies:
pip install -r requirements.txt
Run the backend:
python app.py
Run the frontend:
python -m streamlit run frontend.py
Open the Streamlit UI and adjust sliders to get placement prediction.
Dependencies
Flask
Streamlit
pandas
scikit-learn
requests
How It Works
User inputs values in the Streamlit frontend.
Frontend sends data to Flask API (/predict).
Flask API predicts using the pre-trained Logistic Regression model.
Prediction is displayed on the frontend.
