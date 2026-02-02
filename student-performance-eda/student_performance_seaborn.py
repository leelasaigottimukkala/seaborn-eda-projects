import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data={"Student_ID":   [101,102,103,104,105,106,107],
"Math":         [78,85,90,60,72,88,95],
"Science":      [82,80,88,65,70,90,92],
"English":      [75,78,85,58,68,86,90],
"Attendance":   [85,90,95,70,80,92,98],
"Gender":       ["M","F","M","F","M","F","M"]
}
df=pd.DataFrame(data)
math_avg=np.average(df["Math"])
sci_avg=np.average(df["Science"])
eng_avg=np.average(df["English"])
att_avg=np.average(df["Attendance"])
print(math_avg,sci_avg,eng_avg,att_avg)


columns=["Math","Science","English","Attendance"]
plt.figure(figsize=(12,8))
plt.subplot(2,2,1)
plt.title("Heatmap")
sns.set_style("whitegrid")
sns.heatmap(data=df[columns].corr(),annot=True,cmap="Blues",linewidth="0.2",linecolor="black")


score_df = df.melt(
    id_vars=["Student_ID", "Gender"],
    value_vars=["Math", "Science", "English"],
    var_name="Subject",
    value_name="Score"
)


plt.subplot(2,2,2)
sns.boxplot(data=score_df,x="Subject",y="Score",hue="Gender")
plt.title("Boxplot")


plt.subplot(2,2,3)
sns.scatterplot(data=df,x="Attendance",y="Science",hue="Gender")
plt.title("Scatterplot")

plt.tight_layout()
plt.show()
