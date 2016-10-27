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
    
    return np.mean(ret)

def RSI(price, time):
    gain=[]
    loss=[]
    i=0
    if(len(price) < time):
        print("Error")
        sys.exit()
    i=  len(price) - time
  
    while i < len(price)-1:
        
        if price[i] - price[i+1] < 0:
            gain.append(price[i])
        else:
            loss.append(price[i])
        i=i+1
        print(gain)
        print(loss)
    return   100 - 100/(1+(np.mean(gain)/np.mean(loss)))


def MACD(price):
        
        MaCD_line=sma(price,12,0)- sma(price,26,0)
        macd.append(MaCD_line)
        if len(macd)==9:
            signal= sma(MaCD_line,9,0)
            macd=macd[1:9]
        MACD_histogram= MaCD_line - signal
        print(len(macd))
        b=[signal,MACD_histogram]
        return b
def vwap(price,volume, time):
    vol=0;
    vwp=0
    while time > 0:
       vwp=vwp+price[time]*volume[time]
       vol=vol+volume[time]
       time=time-1
    return vwp/vol
def roc(price,time):
    return price[len(price)-1]/price[len(price)-time-1] - 1

def  linReg_train(y,x, t):
    b=0
    c=0
    d=0
    a=0;
    w=0
    if t <=0:
        sys.exit()
    while t > 1:
         b=b+y[t]*x[t]
         c=c+x[t]
         d=d+x[t]
         a=a+ x[t]**2
         w=w+y[t]    
         t=t-1

    m=(t*b- c*d)/(t*a- c**2)
    slope=(w-m*c)/t
    return m*x[t] +c
         
    
    
