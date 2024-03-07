from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv(r"C:\Users\nathr\Documents\BIELSYS\IELS2001\ovinger\ovingesp3\potmeter.csv")

dataframe = pd.DataFrame(data, columns=["time", "data"])
dataframe["time"] = pd.to_datetime(dataframe["time"], unit="ms")
plt.plot(dataframe["time"], dataframe["data"])
plt.show()
#print(dataframe["time"])

