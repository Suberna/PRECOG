#include <ESP8266WiFi.h>

const char* ssid = "your_wifi_ssid";
const char* password = "your_wifi_password";
const char* serverAddress = "your_server_address";
const int serverPort = 80;

void setup() {
    Serial.begin(9600);
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
        delay(1000);
        Serial.println("Connecting to WiFi...");
    }
    Serial.println("Connected to WiFi");
}

void loop() {
    // Read sensor data
    int sensorValue = analogRead(A0);

    // Connect to server and send data
    WiFiClient client;
    if (client.connect(serverAddress, serverPort)) {
        client.print("GET /sensor-data?value=");
        client.print(sensorValue);
        client.println(" HTTP/1.1");
        client.println("Host: your_server_address");
        client.println("Connection: close");
        client.println();
        delay(1000); // Wait for server response
        client.stop();
    }
    delay(5000); // Wait before sending next data
}
