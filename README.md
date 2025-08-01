# House Price Prediction App

This is a Flask-based web app that predicts house prices using a machine learning model trained on the California housing dataset.

## Features

- Predict house prices based on input features (rooms, location, population, etc.)
- Clean and responsive frontend
- Model trained using Jupyter Notebook and exported as `.pkl`, hosted on Hugging face

## Model

The trained model file (`house_price_model.pkl`) was too large for GitHub, so it is hosted externally:

**Download the model from Hugging Face**:  

[Download model.pkl](https://huggingface.co/datasets/hassaan14/house-price-model/resolve/main/house_price_model.pkl)

## How to Run Locally

1. Clone the repository:

```bash
git clone https://github.com/MuhammadHassaan14/house-price-predicting-app.git
cd house-price-predicting-app

## Install dependencies

pip install -r requirements.txt

> Place the downloaded `house_price_model.pkl` file in the project root directory before running the app.

## Run the Flask app

python app.py

> visit the link in your cmd