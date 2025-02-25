from typing import Dict, List

from fastapi import FastAPI

from .app.get_weather_api import weather_api_connect
from .config import api_url

app = FastAPI()   

@app.get('/data_epic/api') 
def hello_api():   
  return {     
    'message': 'Welcome to Data Epic weather API Service',     
    'status': 200   
  } 

@app.get('/data_epic/api/get_weather')
def get_weather_data(state_1:str='',state_2:str='',
                     state_3:str='')-> Dict:
  
  weather_url:str = api_url

  states:List[str] = [state_1, state_2, state_3]

  # Check if all values are None
  if all(state == '' for state in states):
    return {
        'error': 'Please provide at least one state name (eg. Owerri)',
        'status': 400
    }
  else:
    # Strip spaces from all values
    state_values = [state.strip() for state in states]

    normalized_values = [state for state in state_values if state]

    ## fetch data from API    
    weather_for_states = weather_api_connect(weather_url, normalized_values)

  return {
    'data': weather_for_states
  }
