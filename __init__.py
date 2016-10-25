import numpy as np
import sys


def  sma(price, lag, typee):
    ret=[]
    if  len(price) < lag:
      print "Error"
      sys.exit()
    while lag > 0:
        ret.append(price[lag-1])
        lag=lag -1
    print ret
    return np.mean(ret)

def RSI(price, time):
    gain=[]
    loss=[]
    i=0
    if(len(price) < time):
        print("Error")
        sys.exit()
    i=  len(price) - time
    print(i)
    while i < len(price)-1:
        
        if price[i] - price[i+1] < 0:
            gain.append(price[iprint(gain)])
        else:
            loss.append(price[i])
        i=i+1
        print(gain)
        print(loss)
    return   100 - 100/(1+(np.mean(gain)/np.mean(loss)))
        

    
