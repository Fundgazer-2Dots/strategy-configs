import requests
import os

input_dir = "pattern_backtest/converted"

headers = {
    "accept": "application/json",
}

for filename in os.listdir(input_dir):
    f = os.path.join(input_dir, filename)

    if not os.path.isfile(f):
        continue

    files = {
        "patternFile": (filename,open(f, "rb")),
        "indicatorFile": ("indicator_params1.json",open("pattern_backtest/single/indicator_params1.json", "rb")),
    }

    try :

        response = requests.post(
            "http://198.71.60.195:8081/submit-job", headers=headers, files=files
        )
        print(response.text)
    except:
        print(response.text)
        
