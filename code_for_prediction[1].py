{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ApLtriS5t9Y1",
        "outputId": "82afdc16-baea-4a19-b638-655bb1f1f75c"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Predicted building collapse: [1]\n"
          ]
        }
      ],
      "source": [
        "import pandas as pd\n",
        "import joblib\n",
        "\n",
        "# Load pre-trained model and scaler\n",
        "model = joblib.load('/content/building_collapse_model.pkl')\n",
        "scaler = joblib.load('/content/scaler.pkl')\n",
        "\n",
        "# Function to preprocess sensor data\n",
        "def preprocess_sensor_data(data):\n",
        "    # Convert data to DataFrame\n",
        "    df = pd.DataFrame([data], columns=[\"Thermal (°C)\", \"Humidity (%)\", \"Vibratory (Hz)\"])\n",
        "\n",
        "    # Perform any necessary data preprocessing (e.g., scaling)\n",
        "    # Use the same scaler used during model training\n",
        "    df_scaled = scaler.transform(df)\n",
        "\n",
        "    return df_scaled\n",
        "\n",
        "# Function to make predictions\n",
        "def predict_building_collapse(data):\n",
        "    # Preprocess sensor data\n",
        "    processed_data = preprocess_sensor_data(data)\n",
        "\n",
        "    # Predict using pre-trained model\n",
        "    prediction = model.predict(processed_data)\n",
        "\n",
        "    return prediction\n",
        "\n",
        "# Test with sample sensor data\n",
        "sample_sensor_data = [25.5, 60.0, 0.75]  # Example sensor readings\n",
        "prediction = predict_building_collapse(sample_sensor_data)\n",
        "\n",
        "print(\"Predicted building collapse:\", prediction)\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import smtplib\n",
        "from email.mime.text import MIMEText\n",
        "\n",
        "def send_email_alert(recipient_email, subject, message):\n",
        "    sender_email = 'subernasrajaram@email.com'\n",
        "    sender_password = '26012005#Rd'\n",
        "\n",
        "    msg = MIMEText(message)\n",
        "    msg['Subject'] = subject\n",
        "    msg['From'] = sender_email\n",
        "    msg['To'] = recipient_email\n",
        "\n",
        "    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)\n",
        "    server.login(sender_email, sender_password)\n",
        "    server.sendmail(sender_email, recipient_email, msg.as_string())\n",
        "    server.quit()\n",
        "\n",
        "# Example usage\n",
        "recipient_email = '2k22aids47@kiot.ac.in'\n",
        "subject = 'ALERT: Disaster Prediction'\n",
        "message = 'ALERT: A disaster has been predicted! Please take immediate action.'\n",
        "send_email_alert(recipient_email, subject, message)\n"
      ],
      "metadata": {
        "id": "jB_pWuIgXM_C",
        "outputId": "8384f4d9-e4de-40e6-f807-8ec43c0eb9e1",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 339
        }
      },
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "error",
          "ename": "SMTPAuthenticationError",
          "evalue": "(535, b'5.7.8 Username and Password not accepted. For more information, go to\\n5.7.8  https://support.google.com/mail/?p=BadCredentials i17-20020a17090332d100b001dd7a97a266sm15108188plr.282 - gsmtp')",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mSMTPAuthenticationError\u001b[0m                   Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-23-b046c1eea505>\u001b[0m in \u001b[0;36m<cell line: 22>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     20\u001b[0m \u001b[0msubject\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m'ALERT: Disaster Prediction'\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     21\u001b[0m \u001b[0mmessage\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m'ALERT: A disaster has been predicted! Please take immediate action.'\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 22\u001b[0;31m \u001b[0msend_email_alert\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mrecipient_email\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0msubject\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mmessage\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;32m<ipython-input-23-b046c1eea505>\u001b[0m in \u001b[0;36msend_email_alert\u001b[0;34m(recipient_email, subject, message)\u001b[0m\n\u001b[1;32m     12\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     13\u001b[0m     \u001b[0mserver\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0msmtplib\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mSMTP_SSL\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'smtp.gmail.com'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m465\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 14\u001b[0;31m     \u001b[0mserver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlogin\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0msender_email\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0msender_password\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     15\u001b[0m     \u001b[0mserver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msendmail\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0msender_email\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mrecipient_email\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mmsg\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mas_string\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     16\u001b[0m     \u001b[0mserver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mquit\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/lib/python3.10/smtplib.py\u001b[0m in \u001b[0;36mlogin\u001b[0;34m(self, user, password, initial_response_ok)\u001b[0m\n\u001b[1;32m    748\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    749\u001b[0m         \u001b[0;31m# We could not login successfully.  Return result of last attempt.\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 750\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0mlast_exception\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    751\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    752\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mstarttls\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mkeyfile\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mNone\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcertfile\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mNone\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcontext\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mNone\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/lib/python3.10/smtplib.py\u001b[0m in \u001b[0;36mlogin\u001b[0;34m(self, user, password, initial_response_ok)\u001b[0m\n\u001b[1;32m    737\u001b[0m             \u001b[0mmethod_name\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m'auth_'\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0mauthmethod\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlower\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mreplace\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'-'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'_'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    738\u001b[0m             \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 739\u001b[0;31m                 (code, resp) = self.auth(\n\u001b[0m\u001b[1;32m    740\u001b[0m                     \u001b[0mauthmethod\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mgetattr\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mmethod_name\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    741\u001b[0m                     initial_response_ok=initial_response_ok)\n",
            "\u001b[0;32m/usr/lib/python3.10/smtplib.py\u001b[0m in \u001b[0;36mauth\u001b[0;34m(self, mechanism, authobject, initial_response_ok)\u001b[0m\n\u001b[1;32m    660\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mcode\u001b[0m \u001b[0;32min\u001b[0m \u001b[0;34m(\u001b[0m\u001b[0;36m235\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m503\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    661\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0;34m(\u001b[0m\u001b[0mcode\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mresp\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 662\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0mSMTPAuthenticationError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcode\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mresp\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    663\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    664\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mauth_cram_md5\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mchallenge\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mNone\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mSMTPAuthenticationError\u001b[0m: (535, b'5.7.8 Username and Password not accepted. For more information, go to\\n5.7.8  https://support.google.com/mail/?p=BadCredentials i17-20020a17090332d100b001dd7a97a266sm15108188plr.282 - gsmtp')"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "9QTn2LJtYot3"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}