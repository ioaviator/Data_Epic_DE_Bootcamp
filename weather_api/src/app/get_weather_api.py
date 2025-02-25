from typing import List

import requests

from .load_to_gsheet import load_to_sheet
from .scrape_weather_api import scrape_api


def weather_api_connect(url:str, states:List, g_sheet_url)->List[dict]:

  weather_data = []
  api_response = []

  for state_ in states:

    state:str = state_.lower().replace(" ", "-")
    
    BASE_URL:str = f"{url}/{state}"
    
    try:
      response = requests.get(BASE_URL)
    except Exception as e:
      print(f"Error fetching {state}: {e}")
      raise e
    
    if response.status_code != 200:
        api_response.append({
           'error':f'Invalid state value -- {state}'
        })
    else:
      scraped_data = scrape_api(response, state)

      weather_data.append(scraped_data)
    

  if weather_data:
    return load_to_sheet(weather_data, g_sheet_url)
  else:
      return api_response


