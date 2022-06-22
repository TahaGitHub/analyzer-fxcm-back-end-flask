import pandas as pd
import numpy as np
from scipy.signal import argrelextrema
from sqlalchemy import column
from tqdm import tqdm

class Pattern_controller():
    def peak_detect(price, order = 1):
        #price = start_live_data.open.values[:300]
        max_idx = list(argrelextrema(price, np.greater, order = order)[0])
        min_idx = list(argrelextrema(price, np.less, order = order)[0])
    
        idx = max_idx + min_idx + [len(price) - 1]
        
        #idx.sort(key=lambda x:x[0],reverse=True)
        idx.sort()
        
        current_idx = idx[-5:]
    
        start = min(current_idx)
        end = max(current_idx)
        
        current_pat = price[current_idx]
    
        return current_idx, current_pat, start, end
    
    def walk_forward(price, sign, slippage = 4, stop = 10):
        slippage = float(slippage)/float(10000)
        stop_amount = float(stop)/float(10000)
        
        if sign == 1:
            initial_stop_loos = price[0] - stop_amount
            
            stop_loss = initial_stop_loos
            
            for i in range(1, len(price)):
                move = price[i] - price[i-1]
                
                if move > 0 and (price[i] - stop_amount) > initial_stop_loos:
                    stop_loss = price[i] - stop_amount
                
                elif price[i] < stop_loss:
                    
                    return stop_loss - price[0] - slippage
                
        elif sign == -1:
            initial_stop_loos = price[0] + stop_amount
            stop_loss = initial_stop_loos
            
            for i in range(1, len(price)):
                move = price[i] - price[i - 1]
                if move < 0 and (price[i] + stop_amount) < initial_stop_loos:
                    stop_loss = price[i] - stop_amount
                    
                elif price[i] < stop_loss:
                    return stop_loss - price[0] - slippage

class Pattern_types():
    def is_gratley(moves, err_allowed):
        XA = moves[0]
        AB = moves[1]
        BC = moves[2]
        CD = moves[3]
        
        AB_range = np.array([0.618 - err_allowed, 0.618 + err_allowed]) * abs(XA)
        BC_range = np.array([0.382 - err_allowed, 0.886 + err_allowed]) * abs(AB)
        CD_range = np.array([1.27 - err_allowed, 1.618 + err_allowed]) * abs(BC)
    
        # find any Bullish guard
        if XA > 0 and AB < 0 and BC > 0 and CD < 0:
            
            if AB_range[0] < abs(AB) < AB_range[1] and \
                BC_range[0] < abs(BC) < BC_range[1] and \
                 CD_range[0] < abs(CD) < CD_range[1]:
                return 1
            else:
                return np.NAN
    
        # find any bearish guard
        elif XA < 0 and AB > 0 and BC < 0 and CD > 0:
    
            if AB_range[0] < abs(AB) < AB_range[1] and \
                BC_range[0] < abs(BC) < BC_range[1] and \
                 CD_range[0] < abs(CD) < CD_range[1]:
                return -1
            else:
                return np.NAN
            
        else:
            return np.NAN
    
    def is_butterfly(moves, err_allowed):
        XA = moves[0]
        AB = moves[1]
        BC = moves[2]
        CD = moves[3]
        
        AB_range = np.array([0.786 - err_allowed, 0.786 + err_allowed]) * abs(XA)
        BC_range = np.array([0.382 - err_allowed, 0.886 + err_allowed]) * abs(AB)
        CD_range = np.array([1.618 - err_allowed, 2.618 + err_allowed]) * abs(BC)
    
        # find any Bullish guard
        if XA > 0 and AB < 0 and BC > 0 and CD < 0:
            
            if AB_range[0] < abs(AB) < AB_range[1] and \
                BC_range[0] < abs(BC) < BC_range[1] and \
                 CD_range[0] < abs(CD) < CD_range[1]:
                return 1
            else:
                return np.NAN
    
        # find any bearish guard
        elif XA < 0 and AB > 0 and BC < 0 and CD > 0:
    
            if AB_range[0] < abs(AB) < AB_range[1] and \
                BC_range[0] < abs(BC) < BC_range[1] and \
                 CD_range[0] < abs(CD) < CD_range[1]:
                return -1
            else:
                return np.NAN
            
        else:
            return np.NAN
    
    def is_bat(moves, err_allowed):
        XA = moves[0]
        AB = moves[1]
        BC = moves[2]
        CD = moves[3]
        
        AB_range = np.array([0.382 - err_allowed, 0.5 + err_allowed]) * abs(XA)
        BC_range = np.array([0.382 - err_allowed, 0.886 + err_allowed]) * abs(AB)
        CD_range = np.array([1.618 - err_allowed, 2.618 + err_allowed]) * abs(BC)
    
        # find any Bullish guard
        if XA > 0 and AB < 0 and BC > 0 and CD < 0:
            
            if AB_range[0] < abs(AB) < AB_range[1] and \
                BC_range[0] < abs(BC) < BC_range[1] and \
                 CD_range[0] < abs(CD) < CD_range[1]:
                return 1
            else:
                return np.NAN
            
        # find any bearish guard
        elif XA < 0 and AB > 0 and BC < 0 and CD > 0:
    
            if AB_range[0] < abs(AB) < AB_range[1] and \
                BC_range[0] < abs(BC) < BC_range[1] and \
                 CD_range[0] < abs(CD) < CD_range[1]:
                return -1
            else:
                return np.NAN
        else:
            return np.NAN
        
    def is_crab(moves, err_allowed):
        XA = moves[0]
        AB = moves[1]
        BC = moves[2]
        CD = moves[3]
        
        AB_range = np.array([0.382 - err_allowed, 0.618 + err_allowed]) * abs(XA)
        BC_range = np.array([0.382 - err_allowed, 0.886 + err_allowed]) * abs(AB)
        CD_range = np.array([2.24 - err_allowed, 3.618 + err_allowed]) * abs(BC)
    
        # find any Bullish guard
        if XA > 0 and AB < 0 and BC > 0 and CD < 0:
            
            if AB_range[0] < abs(AB) < AB_range[1] and \
                BC_range[0] < abs(BC) < BC_range[1] and \
                 CD_range[0] < abs(CD) < CD_range[1]:
                return 1
            else:
                return np.NAN
    
        # find any bearish guard
        elif XA < 0 and AB > 0 and BC < 0 and CD > 0:
    
            if AB_range[0] < abs(AB) < AB_range[1] and \
                BC_range[0] < abs(BC) < BC_range[1] and \
                 CD_range[0] < abs(CD) < CD_range[1]:
                return -1
            else:
                return np.NAN
        else:
            return np.NAN

def main_pat(data = None):
    # Local data for testing
    # data = pd.read_csv('./Data_Set/DataSet 2015-2019.csv', parse_dates=['date'])
    # data.columns = [['date','open','high','low','close', 'Vol']]

    # Convert data to DataFrame
    # Return 10 columns from fxcm server RestApi
    # Return 9 columns from fxcm package
    # print(type(data))
    if type(data) is list:
        print(str(type(data)) + ' 1 data type')
        data = pd.DataFrame (data, columns = ['time',
            'open', 'close', 'high', 'low',
            # 'askopen', 'askclose', 'askhigh', 'asklow',
            # 'tickqty'
        ])
    else:
        print(str(type(data)) + ' 2 data type')
        data = pd.DataFrame (data, columns = [
            'open', 'close', 'high', 'low',
            # 'askopen', 'askclose', 'askhigh', 'asklow',
            # 'tickqty'
        ])
        data = data.reset_index()
        
    # print(data.columns)
    data_pat = pd.DataFrame(index = [0], columns = ['time', 'current_idx', 'current_pat', 'start', 'price'])

    err_allowed = 70/100
    
    # print(data.tail(5)) # Get the last 10 element
    price = data.iloc[:]
    # print(price)
    current_idx = current_pat = start = end = None

    for i in tqdm(range(30, len(price.open.values))):
        current_idx, current_pat, start, end = Pattern_controller.peak_detect(price.open.values[:i])
        
        XA = current_pat[1] - current_pat[0]
        AB = current_pat[2] - current_pat[1]
        BC = current_pat[3] - current_pat[2]
        CD = current_pat[4] - current_pat[3]
        
        moves = [XA, AB, BC, CD]
        
        gart = Pattern_types.is_gratley(moves, err_allowed)
        
        but = Pattern_types.is_butterfly(moves, err_allowed)
        
        bat = Pattern_types.is_bat(moves, err_allowed)
        
        crab = Pattern_types.is_crab(moves, err_allowed)
        
        harmonics = np.array([gart, but, bat, crab])

        if np.any(harmonics == 1) or np.any(harmonics == -1):
            for j in range(0, len(harmonics)):
                # j = 0
                if harmonics[j] == 1 or harmonics[j] == -1:
                    data_pat.loc[len(data_pat), ['time', 'current_idx', 'current_pat', 'start', 'price']] = \
                                    [price['time'].values[start:i+15], current_idx, current_pat, 
                                        np.arange(start, i+15), price.open.values[start:i+15]]

    # print(data_pat)
    if np.any([current_idx, current_pat, start, end] == None) or data_pat.index.size <= 1: #  any(x is None for x in [current_idx, current_pat, start, end]):
        print('Nothing found')
        return False
    else:
        print('Found some Fibonacci')
        data_pat = data_pat.loc[data_pat.astype(str).drop_duplicates().index]
        data_pat = data_pat.reset_index(drop = True)  
        return data_pat.dropna()
