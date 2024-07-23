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

# 전열교환기 패킷
HEAT_EXCHANGER_ON = bytearray([0xC0, 0x13, 0x44, 0x01, 0x06, 0x10, 0x00, 0x07, 0x08, 0x00, 0x00, 0x4F, 0xC0, 0x2C, 0x44, 0x01, 0x00, 0x69])
HEAT_EXCHANGER_OFF = bytearray([0xC0, 0x13, 0x44, 0x01, 0x06, 0x10, 0x00, 0x04, 0x1C, 0x00, 0x00, 0x58, 0xC0, 0x2C, 0x44, 0x01, 0x00, 0x69])

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("homeassistant/gwellcity1/command")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    payload = json.loads(msg.payload.decode())
    if payload.get('device') == 'heat_exchanger':
        control_heat_exchanger(payload.get('state'))

def control_heat_exchanger(state):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((GWELLCITY1_HOST, GWELLCITY1_PORT))
        if state == 'on':
            s.send(HEAT_EXCHANGER_ON)
        elif state == 'off':
            s.send(HEAT_EXCHANGER_OFF)
        # 응답 처리 로직 추가 필요

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

if MQTT_USERNAME and MQTT_PASSWORD:
    client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)

client.connect(MQTT_HOST, MQTT_PORT, 60)

client.loop_start()

while True:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((GWELLCITY1_HOST, GWELLCITY1_PORT))
            while True:
                data = s.recv(1024)
                if not data:
                    break
                # 여기에 데이터 처리 로직 추가
                client.publish("homeassistant/gwellcity1/state", json.dumps({"data": data.hex()}))
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(5)

client.loop_stop()