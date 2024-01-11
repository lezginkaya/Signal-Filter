import pandas as pd
from scipy import signal
import  matplotlib.pyplot as plt

data=pd.read_csv("od.csv", skiprows=6) #bearing vibration data
a=data.head(10)
time=data["Time"]
acc=data["Acc"]

#filtering process - low pass filter
x=signal.butter(5,90,"lp",fs=750, output="sos") # fs= sample rate, Hz
#50 = desired cutoff frequency , Hz
filtered_data=signal.sosfilt(x,acc)

plt.figure(figsize=(10,7))
plt.title("Lowpass Filter")
plt.xlabel("Time")
plt.ylabel("Acceleration")
plt.plot(time,acc , label="Original Data" , alpha=0.5)
plt.plot(time,filtered_data, label="Filtered Data")
plt.legend()
plt.show()