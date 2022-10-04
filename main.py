import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

import varenv
import csv_writer


# URL:
# Sandbox domain: "https://sandbox-api.coinmarketcap.com"
# Production domain: "https://pro-api.coinmarketcap.com"
_URL = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

# Parameters:
# Each endpoint has its own parameter
# https://coinmarketcap.com/api/documentation/v1/#section/Endpoint-Overview
_PARAMETERS = {"start": 1, "limit": 100, "convert": "USD"}

# Headers:
_HEADERS = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": varenv.API_KEY,
}


def main(url, parameters):

    # Prepare a Session with Header
    with requests.Session() as session:
        session.headers.update(_HEADERS)

        try:
            # Get response and returns the json-encoded content.
            response = session.get(url, params=parameters)
            json_data = response.json()["data"]

            # Save API data to a csv file
            csv_writer.json_to_csv(json_data)

        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)


if __name__ == "__main__":
    main(_URL, _PARAMETERS)
