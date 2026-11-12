
import asyncio
import json
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from flask import Flask, jsonify

app = Flask(__name__)

API_URL = (
    "https://vpic.nhtsa.dot.gov/api/vehicles/"
    "GetVehicleVariableList?format=json"
)

TARGET_GROUP = "Active Safety System"


def get_external_data():
    """Retrieve JSON from the NHTSA API."""
    with urlopen(API_URL, timeout=20) as response:
        return json.load(response)


async def fetch_and_filter():
    """Fetch external data without blocking the event loop."""
    data = await asyncio.to_thread(get_external_data)

    results = data.get("Results", [])

    filtered = [
        item for item in results
        if item.get("GroupName") == TARGET_GROUP
    ]

    return filtered


@app.route("/items", methods=["GET"])
def get_items():
    """Return filtered NHTSA data as JSON."""
    try:
        filtered = asyncio.run(fetch_and_filter())

        return jsonify(filtered), 200

    except HTTPError as error:
        return jsonify({
            "error": f"External API HTTP error: {error.code}"
        }), 502

    except (URLError, TimeoutError):
        return jsonify({
            "error": "Unable to reach the NHTSA API"
        }), 503

    except (ValueError, TypeError, KeyError):
        return jsonify({
            "error": "Invalid data returned by NHTSA"
        }), 502


if __name__ == "__main__":
    app.run(debug=True, port=5000)
