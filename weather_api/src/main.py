from fastapi import FastAPI

app = FastAPI()   

@app.get('/data_epic/api') 
def hello_api():   
  return {     
    'message': 'Welcome to Data Epic weather API Service',     
    'status': 200   
  } 