from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)
model = joblib.load('house_price_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input values from form
        average_rooms = float(request.form['average_rooms'])
        population = float(request.form['population'])
        latitude = float(request.form['latitude'])
        longitude = float(request.form['longitude'])
        median_income = float(request.form['median_income'])
        housing_median_age = float(request.form['housing_median_age'])
        total_bedrooms = float(request.form['total_bedrooms'])
        households = float(request.form['households'])

        # Get ocean proximity from form and one-hot encode it
        ocean_prox = request.form['ocean_proximity']
        ocean_labels = ['INLAND', 'NEAR BAY', 'NEAR OCEAN', 'ISLAND', '<1H OCEAN']
        ocean_one_hot = [1 if ocean_prox == label else 0 for label in ocean_labels]

        # Final input: 13 features
        input_features = np.array([[average_rooms, population, latitude, longitude,
                                    median_income, housing_median_age, total_bedrooms,
                                    households] + ocean_one_hot])

        # Predict
        prediction = model.predict(input_features)
        output = round(prediction[0], 2)

        return render_template('index.html', prediction_text=f'Predicted House Price: ${output}')
    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == '__main__':
    app.run(debug=True)
