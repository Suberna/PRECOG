from flask import Flask, request
import joblib

app = Flask(__name__)

# Load the pre-trained machine learning model
model = joblib.load('your_model_filename.pkl')

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
    # Implement preprocessing steps here
    # Example: Scale or normalize the data, handle missing values, etc.
    return preprocessed_data

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
