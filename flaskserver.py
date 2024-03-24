from flask import Flask, request
import joblib
from sklearn.preprocessing import StandardScaler, LabelEncoder

app = Flask(__name__)

# Load the trained machine learning model
model = joblib.load("")

@app.route('/sensor-data', methods=['POST'])
def receive_sensor_data():
    data = request.json  # Assuming data is sent in JSON format
    # Preprocess the received data
    preprocessed_data = preprocess_data(data)
    # Predict disasters using the machine learning model
    prediction = predict_disaster(model, preprocessed_data)
    # Trigger alert system if disaster is predicted
    if prediction == 'disaster':
        trigger_alert_system()
    return 'Data received successfully'

def preprocess_data(data):
    # Extract features from the sensor data and preprocess them
    # Example: Scale numerical features, encode categorical features, etc.
    numerical_features = ['feature1', 'feature2', ...]  # Replace with actual numerical feature names
    categorical_features = ['category1', 'category2', ...]  # Replace with actual categorical feature names

    # Preprocess numerical features
    scaler = StandardScaler()
    numerical_data = data[numerical_features]
    numerical_data_scaled = scaler.fit_transform(numerical_data)

    # Preprocess categorical features (if any)
    categorical_data = data[categorical_features]
    encoded_categorical_data = encode_categorical_features(categorical_data)

    # Combine preprocessed numerical and categorical features
    preprocessed_data = np.concatenate((numerical_data_scaled, encoded_categorical_data), axis=1)

    return preprocessed_data

def encode_categorical_features(categorical_data):
    # Use LabelEncoder to encode categorical features
    encoder = LabelEncoder()
    encoded_categorical_data = categorical_data.apply(encoder.fit_transform)
    return encoded_categorical_data

def predict_disaster(model, preprocessed_data):
    # Use the trained model to make predictions
    prediction = model.predict(preprocessed_data)
    return prediction

def trigger_alert_system():
    # Implement alert system to send alerts via GSM SIM
    # Example: Call a function to send SMS alerts
    send_sms_alert()
    pass

def send_sms_alert():
    # Implement code to send SMS alert
    pass

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
