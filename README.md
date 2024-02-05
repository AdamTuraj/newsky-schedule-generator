# Newsky Schedule Generator

Generates a CSV file which can be imported into Newsky based on data fetched from Flightaware API

## Requirements

- You will need to create a Flightaware account. This can easily be done by following the steps here: https://www.flightaware.com/aeroapi/signup/personal
- A version of Python 3

## Installation

Create a virtual environment and activate it:

```
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```
pip install requests
```

Now just run `newSkyExportSchedule.py` and the magic will be done!
