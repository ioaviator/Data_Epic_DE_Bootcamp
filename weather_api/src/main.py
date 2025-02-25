from typing import Dict, List

from fastapi import FastAPI

from .app.get_weather_api import weather_api
from .config import api_url

app = FastAPI()   

@app.get('/data_epic/api') 
def hello_api():   
  return {     
    'message': 'Welcome to Data Epic weather API Service',     
    'status': 200   
  } 

@app.get('/data_epic/api/get_weather')
def get_weather_data(state_1:str|None=None,state_2:str|None=None,
                     state_3:str|None=None)-> Dict:
  
  weather_url:str = api_url

  states:List[str] = [state_1, state_2, state_3]
  
  # Check if all values are None
  if all(state is None for state in states):
    return {
        'message': 'Please provide at least one state name (eg. Owerri)',
        'status': 400
    }
  else:
    ## fetch data from API
    weather_for_states:List[dict] = weather_api(weather_url, states)
  
  return {
    'data': weather_for_states
  }
