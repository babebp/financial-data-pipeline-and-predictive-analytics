from typing import *
import logging

import requests

# Set log to appear in Airflow
logger = logging.getLogger('airflow.task')


class BinanceClient:
    """A client for interacting with Binance API.

    This class provides methods to retrieve historical price data
    """

    def __init__(self):
        """Initialize the BinanceClient with base URL and retrieves all 
        available symbols in Binance."""

        self._base_url = "https://api.binance.com"

        self.symbols = self._get_symbols()

    def _make_request(self, endpoint: str, query_parameters: Dict):
        """Make a dynamic request to the Binance API
        
        Args:
            endpoint (str): The API endpoint to call.
            query_parameters (Dict): Additional parameters for API request.

        Returns:
            response: The JSON response from the API or None if an error occurs.
        """

        try:
            response = requests.get(self._base_url + endpoint, params=query_parameters)
        except Exception as e:
            logger.error("Connection error while making request to %s: %s", endpoint, e)
            return None

        if response.status_code == 200:
            return response.json()
        else:
            logger.error("Error while making request to %s: %s (status code = %s)",
                         endpoint, response.json(), response.status_code)
            return None

    def _get_symbols(self) -> List[str]:

        params = dict()

        endpoint = "/api/v3/exchangeInfo"
        data = self._make_request(endpoint, params)

        symbols = [x["symbol"] for x in data["symbols"]]

        return symbols

    def get_historical_data(self, symbol: str, start_time: Optional[int] = None, end_time: Optional[int] = None):

        params = dict()

        params["symbol"] = symbol
        params["interval"] = "1m"
        params["limit"] = 1500

        if start_time is not None:
            params["startTime"] = start_time
        if end_time is not None:
            params["endTime"] = end_time

        endpoint = "/api/v3/klines"
        raw_candles = self._make_request(endpoint, params)

        candles = []

        if raw_candles is not None:
            for c in raw_candles:
                candles.append((float(c[0]), float(c[1]), float(c[2]), float(c[3]), float(c[4]), float(c[5]),))
            return candles
        else:
            return None








