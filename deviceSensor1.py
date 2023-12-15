import json
import random
import time
import subprocess

while True:
    previous_height = 0
    height = 0

    while height < 100:
        height = random.randint(previous_height + 1, 100)
        temperature = random.randint(20, 40)

        data = {
            "Height": height,
            "Temperature": temperature
        }

        json_data = json.dumps(data)
        curl_command = f'curl -v -X POST http://185.167.96.79:8080/api/v1/bN3MBQvKg0CTZuIs30DX/telemetry --header Content-Type: application/json --data \'{json_data}\''
        subprocess.run(curl_command, shell=True)
        print(json_data)
        
        time.sleep(1800)
