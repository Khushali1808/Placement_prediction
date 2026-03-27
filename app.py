from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load model safely
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return "Placement Prediction API is Running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        features = [[
            data.get('cgpa', 0),
            data.get('aptitude', 0),
            data.get('communication', 0),
            data.get('projects', 0)
        ]]

        prediction = model.predict(features)[0]

        return jsonify({
            "prediction": int(prediction)
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        })

if __name__ == "__main__":
    app.run(debug=True)