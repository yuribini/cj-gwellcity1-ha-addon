import paho.mqtt.client as mqtt
import json
import socket
import time
import os

# MQTT 설정
MQTT_HOST = os.environ.get('MQTT_HOST', 'localhost')
MQTT_PORT = int(os.environ.get('MQTT_PORT', 1883))
MQTT_USERNAME = os.environ.get('MQTT_USERNAME', '')
MQTT_PASSWORD = os.environ.get('MQTT_PASSWORD', '')

# Gwellcity1 설정
GWELLCITY1_HOST = os.environ.get('GWELLCITY1_HOST', 'localhost')
GWELLCITY1_PORT = int(os.environ.get('GWELLCITY1_PORT', 8899))

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("homeassistant/gwellcity1/command")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    # 여기에 명령 처리 로직 추가

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

if MQTT_USERNAME and MQTT_PASSWORD:
    client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)

client.connect(MQTT_HOST, MQTT_PORT, 60)

while True:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((GWELLCITY1_HOST, GWELLCITY1_PORT))
            while True:
                data = s.recv(1024)
                if not data:
                    break
                # 여기에 데이터 처리 로직 추가
                client.publish("homeassistant/gwellcity1/state", json.dumps({"data": data.decode()}))
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(5)

client.loop_forever()
