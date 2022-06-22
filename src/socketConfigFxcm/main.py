from datetime import datetime
import json
import fxcmpy

from .configData import configData

con = None

def get_data (data):
# pairs, period = 'm15', number = 300, start = None, stop = None):
  global con
  data = json.loads(data)

  if con is None: return 'No connection with Fxcm server'
  if data is None:
    data = {
      'pairs': 'USD/TRY',
      "period": "m15",
      "number": 150,
      "start": None,
      "stop": None
    }
  # print(data)

  lists = []
  if data['start'] and data['stop']:
    print('Get data by date')
    lists = con.get_candles(str(data['pairs']), period = str(data['period']),
      start = data['start'], stop = data['stop'])
  else:
    print('Get data by number of moving')
    lists = con.get_candles(str(data['pairs']), period = str(data['period']), number = int(data['number']))
  # print(str(lists))
  return lists

def main():  
  global con
  
  if con:
    print('...Connected...')
    return

  print('Connecting to fxcm...')
  con = fxcmpy.fxcmpy( access_token = configData['token'], log_level = 'error', log_file = None )
  print('Connection done')
  
  # print(get_data('EUR/USD'))

  #The server is demo by default. THe options below are also available for usage.
  #con = fxcmpy.fxcmpy(config_file='fxcm.cfg', server='demo')

  #Connect to the API with a real account. Do not forget to change the access token in the config file.
  #con = fxcmpy.fxcmpy(config_file='fxcm.cfg', server='real')

  # print(con.get_instruments())
