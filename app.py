import asyncio
import json
from urllib.request import urlopen
from urllib.error import HTTPError, URLError

API_URL = (
    "https://vpic.nhtsa.dot.gov/api/vehicles/" "GetVehicleVariableList?format=json"
)


def get_data():
    with urlopen(API_URL, timeout=20) as response:
        return json.load(response)


async def fetch_vehicle_data():
    print("Loading vehicle data from NHTSA...")

    try:
        # Run the blocking HTTP request in a separate thread
        data = await asyncio.to_thread(get_data)

        # Filter the JSON results
        filtered = [
            item
            for item in data.get("Results", [])
            if item.get("GroupName") == "Active Safety System"
        ]

        print(f"\nFound {len(filtered)} matching records.\n")

        for item in filtered:
            print(f"ID: {item.get('ID')}")
            print(f"Name: {item.get('Name')}")
            print(f"Group: {item.get('GroupName')}")
            print("-" * 40)

    except (HTTPError, URLError) as error:
        print(f"Network error: {error}")
    except TimeoutError:
        print("The request timed out.")
    except (ValueError, TypeError) as error:
        print(f"Invalid API data: {error}")


if __name__ == "__main__":
    asyncio.run(fetch_vehicle_data())
