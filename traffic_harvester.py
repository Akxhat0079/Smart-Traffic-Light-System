import requests
import pandas as pd
import time
from datetime import datetime
import os

# Configuration
API_KEY = "Pa9elix8s3wRfHp77S5D9W24Ej62tkt4"
CHOWKS = {
    "101": {"name": "ISBT", "coords": "30.2834,77.9944"},
    "102": {"name": "Clock_Tower", "coords": "30.3243,78.0411"},
    "103": {"name": "Dilaram_Chowk", "coords": "30.3385,78.0601"},
    "104": {"name": "Ballupur", "coords": "30.3344,78.0062"},
    "105": {"name": "Prince_Chowk", "coords": "30.3165,78.0392"},
    "106": {"name": "Balliwala", "coords": "30.3215,77.9998"}
}

RAW_FILE = "raw_traffic_pulses.csv"

def collect():
    pulses = []
    for c_id, info in CHOWKS.items():
        url = f"https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json?key={API_KEY}&point={info['coords']}"
        try:
            res = requests.get(url, timeout=15)
            if res.status_code == 200:
                data = res.json()['flowSegmentData']
                
                # Logic for Chapter 4 & 5 columns
                speed = data['currentSpeed']
                ff = data['freeFlowSpeed']
                ratio = speed / ff
                
                # Categorization logic
                level = "Heavy" if ratio < 0.4 else ("Moderate" if ratio < 0.7 else "Low")
                
                pulses.append({
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "chowk_id": c_id,
                    "chowk_name": info['name'],
                    "current_speed": speed,
                    "free_flow": ff,
                    "delay": data['currentTravelTime'] - data['currentTravelTime'],
                    "traffic_level": level,
                    "confidence": data['confidence'],
                    "road_closure": "Yes" if data.get('roadClosure') else "No",
                    "needs_cleaning": "False" if data['confidence'] > 0.7 else "True" #
                })
                print(f"✔️ Captured {info['name']} Pulse")
        except Exception as e:
            print(f"⚠️ Resuming... ({e})")
            time.sleep(5)
    return pulses

print("🚀 Starting Harvester. Press Ctrl+C to stop.")
while True:
    data_pulse = collect()
    if data_pulse:
        df = pd.DataFrame(data_pulse)
        df.to_csv(RAW_FILE, mode='a', header=not os.path.exists(RAW_FILE), index=False)
    time.sleep(60)