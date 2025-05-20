import requests
import random
import datetime
import time

base_url = "http://localhost:1026/v2/entities/"
sensor_id = "Sensor_CalidadAgua_01"

start_date = datetime.datetime(2025, 3, 1)
end_date = datetime.datetime(2025, 4, 30)
interval = (end_date - start_date) / 400

current_time = start_date
headers = {"Content-Type": "application/json"}

for i in range(400):
    timestamp_str = current_time.isoformat() + "Z"
    data = {
        "PH": {"value": round(random.uniform(15, 30), 2), "type": "Number"},
        "temperatura": {"value": round(random.uniform(30, 70), 2), "type": "Number"},
        "cloro": {"value": round(random.uniform(45, 110), 2), "type": "Number"},
        "dateObserved": {
            "value": timestamp_str,
            "type": "DateTime"
        }
    }
    response = requests.patch(f"{base_url}{sensor_id}/attrs", json=data, headers=headers)
    print(f"Registro {i+1}: {response.status_code}")
    current_time += interval
