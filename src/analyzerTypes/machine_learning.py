import time
import pandas as pd
from functools import reduce
# import matplotlib.pyplot as plt
#import matplotlib.ticker as mtcker
#import matplotlib.dates as mdates

#totalStart = time.time()

patForRec = []

patternAr = []
performanceAr = []

lenOfPattern = 30
_path = './Data_Set/'



def percentChange(startPoint, currentPoint):
  try:
    x = ((float(currentPoint) - startPoint) / abs(startPoint)) * 100
    if x == 0.0:
      return 0.0000000001
    else:
      return x
  except:
    return 0.0000000001



####################################



def preparePatterns(avgLine):

  def save_patterns(patternAr, performanceAr):
    print(f'Saving in {_path}...')
    _patternAr = pd.DataFrame(patternAr)    
    _patternAr.to_pickle(f'{_path}Patterns.pkl')

    _performanceAr = pd.DataFrame(performanceAr)    
    _performanceAr.to_pickle(f'{_path}Pattern_per.pkl')
    print('... Successfully Patterns Saved ...')

  def patternStorge(avgLine):
    print('Storge Pattern Process...')

    patternAr = []
    performanceAr = []
    
    patStartTime = time.time()

    x = len(avgLine)-60
    y = 31

    while y < x:
      pattern = []
      
      p1 = percentChange(avgLine[y-30], avgLine[y-29])
      p2 = percentChange(avgLine[y-30], avgLine[y-28])
      p3 = percentChange(avgLine[y-30], avgLine[y-27])
      p4 = percentChange(avgLine[y-30], avgLine[y-26])
      p5 = percentChange(avgLine[y-30], avgLine[y-25])
      p6 = percentChange(avgLine[y-30], avgLine[y-24])
      p7 = percentChange(avgLine[y-30], avgLine[y-23])
      p8 = percentChange(avgLine[y-30], avgLine[y-22])
      p9 = percentChange(avgLine[y-30], avgLine[y-21])
      p10 = percentChange(avgLine[y-30], avgLine[y-20])

      p11 = percentChange(avgLine[y-30], avgLine[y-19])
      p12 = percentChange(avgLine[y-30], avgLine[y-18])
      p13 = percentChange(avgLine[y-30], avgLine[y-17])
      p14 = percentChange(avgLine[y-30], avgLine[y-16])
      p15 = percentChange(avgLine[y-30], avgLine[y-15])
      p16 = percentChange(avgLine[y-30], avgLine[y-14])
      p17 = percentChange(avgLine[y-30], avgLine[y-13])
      p18 = percentChange(avgLine[y-30], avgLine[y-12])
      p19 = percentChange(avgLine[y-30], avgLine[y-11])
      p20 = percentChange(avgLine[y-30], avgLine[y-10])
      
      p21 = percentChange(avgLine[y-30], avgLine[y-9])
      p22 = percentChange(avgLine[y-30], avgLine[y-8])
      p23 = percentChange(avgLine[y-30], avgLine[y-7])
      p24 = percentChange(avgLine[y-30], avgLine[y-6])
      p25 = percentChange(avgLine[y-30], avgLine[y-5])
      p26 = percentChange(avgLine[y-30], avgLine[y-4])
      p27 = percentChange(avgLine[y-30], avgLine[y-3])
      p28 = percentChange(avgLine[y-30], avgLine[y-2])
      p29 = percentChange(avgLine[y-30], avgLine[y-1])
      p30 = percentChange(avgLine[y-30], avgLine[y])
      
      outcomeRange = avgLine[y + 10: y + 30]
      currentPoint = avgLine[y]
      
      try:
          avgOutcome = reduce(lambda x, y: x+y, outcomeRange) / len(outcomeRange)
      except Exception as e:
          print(str(e))
          avgOutcome = 0
          
      futureOutcome = percentChange(currentPoint, avgOutcome)

      pattern.append(p1)
      pattern.append(p2)
      pattern.append(p3)
      pattern.append(p4)
      pattern.append(p5)
      pattern.append(p6)
      pattern.append(p7)
      pattern.append(p8)
      pattern.append(p9)
      pattern.append(p10)

      pattern.append(p11)
      pattern.append(p12)
      pattern.append(p13)
      pattern.append(p14)
      pattern.append(p15)
      pattern.append(p16)
      pattern.append(p17)
      pattern.append(p18)
      pattern.append(p19)
      pattern.append(p20)

      pattern.append(p21)
      pattern.append(p22)
      pattern.append(p23)
      pattern.append(p24)
      pattern.append(p25)
      pattern.append(p26)
      pattern.append(p27)
      pattern.append(p28)
      pattern.append(p29)
      pattern.append(p30)
      
      patternAr.append(pattern)
      performanceAr.append(futureOutcome)
      
      y +=1
      
      '''
      print(currentPoint)
      print('-----')
      print(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10)
      '''
          
    patEndTime = time.time()

    print('patternAr', len(patternAr))
    print('performanceAr', len(performanceAr))
    print('pattern storge took:', patEndTime - patStartTime, 'second')
    
    # save pattern into pkl file for loading speedly when needed
    save_patterns(patternAr, performanceAr)

  patternStorge(avgLine)



####################################
####################################
####################################



def findPattern(data, amount):

  def load_patterns():
    print(f'Loading Patterns from {_path}...')

    patternArray = pd.read_pickle(f'{_path}Patterns.pkl').values.tolist()
    # patternArray = patternArray.values.tolist()

    performanceArray = pd.read_pickle(f'{_path}Pattern_per.pkl').values.tolist()
    # performanceArray = performanceArray.values.tolist()

    print('... Successfully Loading Patterns ...')
    return patternArray, performanceArray

  # النمط الحالي 
  # Generate current pattern
  def currentPatternGenerator(data):    
    currentPattern = []
    
    for x in range(lenOfPattern, 0, -1):
      cp = percentChange(data.values[-(lenOfPattern + 1)], data.values[-x])
      currentPattern.append(cp)
      
    '''
    cp1 = percentChange(set_pattern.values[-31], set_pattern.values[-30])
    cp2 = percentChange(set_pattern.values[-31], set_pattern.values[-29])
    cp3 = percentChange(set_pattern.values[-31], set_pattern.values[-28])
    cp4 = percentChange(set_pattern.values[-31], set_pattern.values[-27])
    cp5 = percentChange(set_pattern.values[-31], set_pattern.values[-26])
    cp6 = percentChange(set_pattern.values[-31], set_pattern.values[-25])
    cp7 = percentChange(set_pattern.values[-31], set_pattern.values[-24])
    cp8 = percentChange(set_pattern.values[-31], set_pattern.values[-23])
    cp9 = percentChange(set_pattern.values[-31], set_pattern.values[-22])
    cp10 = percentChange(set_pattern.values[-31], set_pattern.values[-21])

    cp11 = percentChange(set_pattern.values[-31], set_pattern.values[-20])
    cp12 = percentChange(set_pattern.values[-31], set_pattern.values[-19])
    cp13 = percentChange(set_pattern.values[-31], set_pattern.values[-18])
    cp14 = percentChange(set_pattern.values[-31], set_pattern.values[-17])
    cp15 = percentChange(set_pattern.values[-31], set_pattern.values[-16])
    cp16 = percentChange(set_pattern.values[-31], set_pattern.values[-15])
    cp17 = percentChange(set_pattern.values[-31], set_pattern.values[-14])
    cp18 = percentChange(set_pattern.values[-31], set_pattern.values[-13])
    cp19 = percentChange(set_pattern.values[-31], set_pattern.values[-12])
    cp20 = percentChange(set_pattern.values[-31], set_pattern.values[-11])

    cp21 = percentChange(set_pattern.values[-31], set_pattern.values[-10])
    cp22 = percentChange(set_pattern.values[-31], set_pattern.values[-9])
    cp23 = percentChange(set_pattern.values[-31], set_pattern.values[-8])
    cp24 = percentChange(set_pattern.values[-31], set_pattern.values[-7])
    cp25 = percentChange(set_pattern.values[-31], set_pattern.values[-6])
    cp26 = percentChange(set_pattern.values[-31], set_pattern.values[-5])
    cp27 = percentChange(set_pattern.values[-31], set_pattern.values[-4])
    cp28 = percentChange(set_pattern.values[-31], set_pattern.values[-3])
    cp29 = percentChange(set_pattern.values[-31], set_pattern.values[-2])
    cp30 = percentChange(set_pattern.values[-31], set_pattern.values[-1])
    
    patForRec.append(cp1)
    patForRec.append(cp2)
    patForRec.append(cp3)
    patForRec.append(cp4)
    patForRec.append(cp5)
    patForRec.append(cp6)
    patForRec.append(cp7)
    patForRec.append(cp8)
    patForRec.append(cp9)
    patForRec.append(cp10)

    patForRec.append(cp11)
    patForRec.append(cp12)
    patForRec.append(cp13)
    patForRec.append(cp14)
    patForRec.append(cp15)
    patForRec.append(cp16)
    patForRec.append(cp17)
    patForRec.append(cp18)
    patForRec.append(cp19)
    patForRec.append(cp20)

    patForRec.append(cp21)
    patForRec.append(cp22)
    patForRec.append(cp23)
    patForRec.append(cp24)
    patForRec.append(cp25)
    patForRec.append(cp26)
    patForRec.append(cp27)
    patForRec.append(cp28)
    patForRec.append(cp29)
    patForRec.append(cp30)
    '''
    
    # print('current Pattern is:  ', currentPattern)
    return currentPattern
    
  # التعرف على النمط
  # Recognition current patter with old patterns that created
  def patternsRecognitor(amount, currentPattern):
    global patternAr, performanceAr

    patternsArr = []
    xp = []
    predictedAvg = []
    
    if not patternAr or not performanceAr:
      patternAr, performanceAr = load_patterns()
  
    for eachPattern in patternAr:
      _sum = []
      for x in range(0, lenOfPattern):
        _sum.append(100.00 - abs(percentChange(eachPattern[x], currentPattern[x])))

      howsim = sum(_sum)/30.00

      '''
      sim1 = 100.00 - abs(percentChange(eachPattern[0], patForRec[0]))
      sim2 = 100.00 - abs(percentChange(eachPattern[1], patForRec[1]))
      sim3 = 100.00 - abs(percentChange(eachPattern[2], patForRec[2]))
      sim4 = 100.00 - abs(percentChange(eachPattern[3], patForRec[3]))
      sim5 = 100.00 - abs(percentChange(eachPattern[4], patForRec[4]))
      sim6 = 100.00 - abs(percentChange(eachPattern[5], patForRec[5]))
      sim7 = 100.00 - abs(percentChange(eachPattern[6], patForRec[6]))
      sim8 = 100.00 - abs(percentChange(eachPattern[7], patForRec[7]))
      sim9 = 100.00 - abs(percentChange(eachPattern[8], patForRec[8]))
      sim10 = 100.00 - abs(percentChange(eachPattern[9], patForRec[9]))

      sim11 = 100.00 - abs(percentChange(eachPattern[10], patForRec[10]))
      sim12 = 100.00 - abs(percentChange(eachPattern[11], patForRec[11]))
      sim13 = 100.00 - abs(percentChange(eachPattern[12], patForRec[12]))
      sim14 = 100.00 - abs(percentChange(eachPattern[13], patForRec[13]))
      sim15 = 100.00 - abs(percentChange(eachPattern[14], patForRec[14]))
      sim16 = 100.00 - abs(percentChange(eachPattern[15], patForRec[15]))
      sim17 = 100.00 - abs(percentChange(eachPattern[16], patForRec[16]))
      sim18 = 100.00 - abs(percentChange(eachPattern[17], patForRec[17]))
      sim19 = 100.00 - abs(percentChange(eachPattern[18], patForRec[18]))
      sim20 = 100.00 - abs(percentChange(eachPattern[19], patForRec[19]))

      sim21 = 100.00 - abs(percentChange(eachPattern[20], patForRec[20]))
      sim22 = 100.00 - abs(percentChange(eachPattern[21], patForRec[21]))
      sim23 = 100.00 - abs(percentChange(eachPattern[22], patForRec[22]))
      sim24 = 100.00 - abs(percentChange(eachPattern[23], patForRec[23]))
      sim25 = 100.00 - abs(percentChange(eachPattern[24], patForRec[24]))
      sim26 = 100.00 - abs(percentChange(eachPattern[25], patForRec[25]))
      sim27 = 100.00 - abs(percentChange(eachPattern[26], patForRec[26]))
      sim28 = 100.00 - abs(percentChange(eachPattern[27], patForRec[27]))
      sim29 = 100.00 - abs(percentChange(eachPattern[28], patForRec[28]))
      sim30 = 100.00 - abs(percentChange(eachPattern[29], patForRec[29]))
      
      howsim = (sim1+sim2+sim3+sim4+sim5+sim6+sim7+sim8+sim9+sim10+
                sim11+sim12+sim13+sim14+sim15+sim16+sim17+sim18+sim19+sim20+
                sim21+sim22+sim23+sim24+sim25+sim26+sim27+sim28+sim29+sim30)/30.00
      '''        
      
      if howsim > amount and not [v for v in patternsArr if not set(v) & set(eachPattern)]:
        '''
        patdex = patternAr.index(eachPattern)
        print('#################')
        print('#################')
        print(currentPattern)
        print('=================')
        print('=================')
        print(eachPattern)
        print('predicted outcome', performanceAr[patdex])
        '''
        xp = [*range(1, lenOfPattern + 1)]
        # xp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
        patternsArr.append(eachPattern)
        indexOfPattern = patternAr.index(eachPattern)
        predictedAvg.append(performanceAr[indexOfPattern])



    if patternsArr:
      print('There are some patterns')
      predictedAvg = reduce(lambda x, y: x+y, predictedAvg[0]) / len(predictedAvg)
      return patternsArr, xp, predictedAvg
    else:
      print('No Patterns Found')
      return [], [], []

      '''
      fig = plt.figure(figsize = (10, 6))
      
      for eachPattern in patternsArr:
          futurePoints = patternAr.index(eachPattern)
          
          if performanceAr[futurePoints] > currentPattern[29]:
              pcolor = '#24bc00'
          else:
              pcolor = '#d40000'
              
      # النمط المشابه للنمط الحالي            
          plt.plot(xp, eachPattern)
          predictedAvgOutcome.append(performanceAr[futurePoints])
          #plt.plot(xp, avgLine.values[-31:-1])       
  # الحركة المتوقعة            
          plt.scatter(35, performanceAr[futurePoints], c = pcolor, alpha = .3)
      
      realOutcomeRange = allData[toWhat + 20: toWhat + 30]
      realAvgOutcome = reduce(lambda x, y: x+y, realOutcomeRange) / len(realOutcomeRange)
      realMovement = percentChange(allData[toWhat], realAvgOutcome)
      
      #print(predictedAvgOutcome)
      #print(type(predictedAvgOutcome))
      #print(len(predictedAvgOutcome))
      
      predictedAvgOutcome = reduce(lambda x, y: x+y, predictedAvgOutcome[0]) / len(predictedAvgOutcome)
      # الحركة التالية للنمط لون نقطة ازرق فاتح                 
      plt.scatter(40, realMovement, c = '#54fff7', s = 25)
      # الحركة التالية المتوفعة لون نقطة ازرق غامق                
      plt.scatter(40, predictedAvgOutcome, c = 'b', s = 25)
                
                      # شكل للنمط الحالي لون الخط ازرق فاتح                
      plt.plot(xp, currentPat, '#54fff7', linewidth = 3)
      plt.grid(True)
      plt.title('Pattern Regntanation')       
      #plt.plot(xp, eachPattern)
      plt.show()
      '''

  currentPattern = currentPatternGenerator(data)
  patternsArr, xp, predictedAvg = patternsRecognitor(amount, currentPattern)
  return patternsArr, xp, predictedAvg, currentPattern



####################################
####################################
####################################



def main_ml(data, amount = 50):
  # global avgLine
  # global patternAr
  # global performanceAr

  # global patForRec
  # global allData
  # global toWhat
  # global patternsArr
  
  # data = pd.read_csv('../Data_Set/DataSet 2015-2019.csv', parse_dates=['Date'])
  #dataLength = int(data.High.shape[0])
  #print('data length is', dataLength)
  
  #toWhat = 140000
  # toWhat = len(data) # - 60

  #allData = ((data.High + data.Low) / 2)
  # allData = data.open
  # return
  
  #while toWhat < dataLength:
  #avgLine = ((data.High + data.Low) / 2)

  #avgLine = allData[:toWhat]
  # avgLine = allData[toWhat:]
  # patternAr = []
  # performanceAr = []
  # patForRec = []
  
  #patternStorge()
  
  df = pd.DataFrame(data)
  # print(df.open)
  patternsArr, xp, predictedAvg, currentPattern = findPattern(df.open, amount)
  
  data = {
    'patternsArr': patternsArr,
    'xp': xp,
    'predictedAvg': predictedAvg,
    'currentPattern': currentPattern
  }
  # print(data)

  return data

  if patternsArr == 0:
      return 0, 0, 0, 0, 0, 0
  else:
      return patternsArr, xp, patForRec, performanceAr, patternAr, toWhat

  #totalTime = time.time() - totalStart
  
  #print('Entire processing time took:', totalTime, 'second')
      
  #moveOn = input('press inter to cuntinue...')
      
  #toWhat += 1
    

#data = pd.read_csv('../Data_Set/DataSet 2015-2019.csv', parse_dates=['Date'])
#if __name__ == '__main__':
#    main(data, 40)       
