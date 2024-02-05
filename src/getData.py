from datetime import datetime, timedelta
import time
import requests

import json


class API:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.headers = {"x-apikey": token}

    def fetchSchedule(self):
        now = datetime.now()
        lastWeek = now - timedelta(days=8)

        fullData = []

        print("Fetching data...")

        res = requests.get(
            self.base_url + "/aeroapi/operators/TSC/flights",
            headers=self.headers,
            params={
                "start": lastWeek.isoformat(timespec="seconds"),
                "end": now.isoformat(timespec="seconds"),
                "max_pages": 10,
            },
        )

        data = res.json()

        if data["links"] == None:
            return data

        for i in data["arrivals"]:
            fullData.append(i)

        print("First batch of data received, waiting on another")
        time.sleep(60)

        while True:
            res = requests.get(
                self.base_url + "/aeroapi" + data["links"]["next"],
                headers=self.headers,
            )

            data = res.json()

            for i in data["arrivals"]:
                fullData.append(i)

            if not data.get("links"):
                break

            print("Another batch of data received, waiting on another")
            time.sleep(60)

        # Backing it up because the operation above is expensive
        with open("results/data.json", "w") as f:
            json.dump(fullData, f)

        print(
            "Data has been successfully fetched and written to data.json. Processing now..."
        )

        return fullData

    def getSchedule(self):
        with open("results/data.json", "r") as f:
            data = json.load(f)

        return data


if __name__ == "__main__":
    print("Do not run this file, run newSkyExportSchedule.py instead.")
