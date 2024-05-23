from flask import Blueprint, request, jsonify
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import os
from config import Config

prediction_bp = Blueprint('prediction', __name__)

@prediction_bp.route("/result", methods=["POST"])
def result():
    if request.method == 'POST':
        try:
            data_path = Config.DATA_PATH
            data = pd.read_csv(data_path)

            data = data.drop(['date', 'street', 'city', 'statezip', 'country'], axis=1)

            X = data.drop('price', axis=1)
            Y = data['price']

            X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.30, random_state=42)

            model = LinearRegression()
            model.fit(X_train, Y_train)

            request_data = request.json

            required_keys = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'waterfront',
                                'view', 'condition', 'sqft_above', 'sqft_basement', 'yr_built', 'yr_renovated']

            for key in required_keys:
                if key not in request_data:
                    raise KeyError(f'Missing key: {key}')
                

            feature_vector = np.array([
                float(request_data['bedrooms']),
                float(request_data['bathrooms']),
                float(request_data['sqft_living']),
                float(request_data['sqft_lot']),
                float(request_data['floors']),
                float(request_data['waterfront']),
                float(request_data['view']),
                float(request_data['condition']),
                float(request_data['sqft_above']),
                float(request_data['sqft_basement']),
                float(request_data['yr_built']),
                float(request_data['yr_renovated'])
            ]).reshape(1, -1)

            pred = model.predict(feature_vector)
            pred = round(pred[0], 2)

            response = {
                'predicted_price': pred
            }

            return jsonify(response)
    
        except KeyError as e:
            return jsonify({'error': f'Missing key in request JSON: {e}'}), 400

        except ValueError as e:
            return jsonify({'error': f'Invalid value in request JSON: {e}'}), 400

        except Exception as e:
            return jsonify({'error': f'An unexpected error occurred: {e}'}), 500
    
    return jsonify({'error': 'Invalid HTTP method'}), 405
