import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data={"Month":        ["Jan","Feb","Mar","Apr","May","Jun"],
"Electronics":  [12000,15000,17000,16000,18000,20000],
"Clothing":     [8000,9000,8500,9500,10000,11000],
"Groceries":    [6000,6500,7000,7200,7500,8000],
"Region":       ["North","South","East","West","North","South"]
}
df=pd.DataFrame(data)
df["total_revenue"]=df[["Electronics","Clothing","Groceries"]].sum(axis=1)
overall_revenue=df["total_revenue"].sum()

sales_df=df.melt(
    id_vars=["Month","Region"],
    value_vars=["Electronics","Clothing","Groceries"],
    var_name="Categories",
    value_name="Revenue"
)

plt.figure(figsize=(12,8))
sns.set_style("whitegrid")
plt.subplot(2,2,1)
sns.lineplot(data=df,x="Month",y="total_revenue",color="red")
plt.title("Total Monthly Revenue Trend")


plt.subplot(2,2,2)
sns.barplot(data=sales_df,x="Categories",y="Revenue",palette="Set2")
plt.title("Average Revenue by Category")



plt.subplot(2,2,3)
sns.boxplot(data=sales_df,x="Categories",y="Revenue",hue="Region")
plt.title("Revenue Distribution by Category and Region")



plt.subplot(2,2,4)
sns.lineplot(data=sales_df,x="Month",y="Revenue",hue="Categories",marker="o")
plt.title("Category-wise Revenue Trend")


plt.tight_layout()
plt.show()
