from typing import List

import requests


def weather_api(url:str, states:List)->List[dict]:
  
  for state in states:
    if state is None:
      continue
    
    state:str = state.lower().replace(" ", "-")
    
    BASE_URL:str = f"{url}/{state}"
    
    try:
      response = requests.get(BASE_URL)
      if response.status_code != 200:
        print(f'Invalid state value -- {state}')
        continue
    except Exception as e:
      print(f"Error fetching {state}: {e}")
      raise e
  
  return {
    'message': 'Connection successful',
    'status': 200
  }

