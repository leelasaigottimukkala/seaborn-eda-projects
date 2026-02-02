import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data={
    "Day":        [1,2,3,4,5,6,7],
"Open":       [100,102,101,103,105,104,106],
"Close":      [102,101,103,105,104,106,108],
"Volume":     [2000,2200,2100,2300,2500,2400,2600]
}

df=pd.DataFrame(data)
df["daily_change"]=df["Close"]-df["Open"]
print(df["daily_change"])

plt.figure(figsize=(12,8))
sns.set_style("whitegrid")
plt.subplot(1,2,1)
sns.lineplot(data=df,x="Day",y="Open",label="Open")
sns.lineplot(data=df,x="Day",y="Close",label="Close")
plt.xlabel("Day")
plt.ylabel("Price")
plt.title("Open and Close Price Trend")




plt.subplot(1,2,2)
sns.lineplot(data=df,x="Day",y="Volume")
plt.title("Trading Volume Trend")
plt.xlabel("Day")
plt.ylabel("Volume")
plt.tight_layout()
plt.show()




sns.jointplot(data=df,x="Open",y="Close",kind="kde")
plt.show()
