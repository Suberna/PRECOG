import serial
import time

def send_sms_alert(message, phone_number):
    # Configure the serial connection to the GSM modem
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=5)  # Adjust port and baud rate as needed
    time.sleep(1)  # Allow time for the serial connection to initialize
    
    # Enter AT command mode
    ser.write(b'AT\r\n')
    response = ser.readline().decode('utf-8').strip()
    if response != 'OK':
        print("Error entering AT command mode:", response)
        return
    
    # Set SMS text mode
    ser.write(b'AT+CMGF=1\r\n')
    response = ser.readline().decode('utf-8').strip()
    if response != 'OK':
        print("Error setting SMS text mode:", response)
        return
    
    # Specify recipient phone number
    ser.write(f'AT+CMGS="{phone_number}"\r\n'.encode('utf-8'))
    response = ser.readline().decode('utf-8').strip()
    if response != '>':
        print("Error specifying recipient phone number:", response)
        return
    
    # Send SMS message
    ser.write(f'{message}\r\n'.encode('utf-8'))
    ser.write(bytes([26]))  # Send Ctrl+Z to indicate end of message
    response = ser.readlines()
    if b'OK' not in response:
        print("Error sending SMS:", response)
    else:
        print("SMS sent successfully")

    # Close serial connection
    ser.close()
