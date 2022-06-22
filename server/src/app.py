import os
from flask import Flask, make_response, request, redirect
import json
from flask_cors import CORS
from numpy import empty

# import requests
# from .socketConfigFxcm.main import *

from analyzerTypes.Fibonacci_Sequence import main_pat
from analyzerTypes.machine_learning import main_ml

_redirectURl = 'https://www.tahaalmokahel.com/projects/analyzer'

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
  return redirect(_redirectURl)
  

@app.route('/projects/analyzer/fibonacci', methods=['POST'])
def analyzer_fibonacci():
  # print(request.args) # Url Parameter Data
  print(request.data) # Body Data
  # print(request.headers) # Header Data

  if not request.data:
    return make_response("No data sent", 200)
    
  # body = None
  # if request.data:
  #   d = json.loads(str(request.data, encoding='utf-8'))
  #   body = {
  #     'pairs': d['pairs'],
  #     "period": d['period'],
  #     "number": d['number'],
  #     "start": d['stop'],
  #     "stop": d['end']
  #   }
  # print(body)
  # data = main_pat(get_data(json.dumps(body)))

  data = main_pat(json.loads(str(request.data, encoding='utf-8')))

  # Get history data immediately without fxcm connection
  # Just need Authorization token
  # data = requests.get(
  #   'https://api-demo.fxcm.com:443/candles/83/m15',
  #   params={'num': 100},
  #   headers={
  #     'Accept': 'application/json',
  #     "Authorization": "Bearer rNvTT_xtiTWXnySMACUqc7654d35f7e7e967d0d68759fe8e365c1553299e"
  #   })
  # data = main_pat(data.json()['candles'])

  # print(data.json())
  # print(data.json()['instrument_id'])
  # print(data.json()['candles'])

  print(data)
  if type(data) is not bool and not data.empty:
    return make_response(data.to_json(), 200)
  else:
    return make_response("False", 200)

@app.route('/projects/analyzer/ml', methods=['POST'])
def analyzer_ml():
  print(request.data) # Body Data

  if not request.data:
    return make_response("No data sent", 200)

  # Get history data immediately without fxcm connection
  # Just need Authorization token
  # data = requests.get(
  #   'https://api-demo.fxcm.com:443/candles/83/m15',
  #   params={'num': 100},
  #   headers={
  #     'Accept': 'application/json',
  #     "Authorization": "Bearer rNvTT_xtiTWXnySMACUqc7654d35f7e7e967d0d68759fe8e365c1553299e"
  #   })
  # data = main_ml(data.json()['candles'])

  data = main_ml(json.loads(str(request.data, encoding='utf-8')))
  print(data)

  if data:
    return make_response(data, 200)
  else:
    return make_response("False", 200)


###############################


@app.errorhandler(404)
def page_not_found(error):
  return redirect(_redirectURl)

@app.errorhandler(405)
def page_not_found(error):
  return redirect(_redirectURl)


###############################


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
  # app.run(debug=True)
  # main()
  # app.run()
