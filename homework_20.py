import matplotlib
import pandas as pd

matplotlib.use("Agg")
import matplotlib.pyplot as plt

df = pd.read_csv("sales_clean.csv")

by_seller = df.groupby("seller")["total"].sum().sort_values(ascending=False)
by_seller.to_csv("sellers.csv", header=True)

by_seller.plot(kind="bar", title="Дохід за продавцями", rot=0)
plt.ylabel("грн")
plt.tight_layout()
plt.savefig("sellers.png")
plt.close()

print("Збережено sellers.csv та sellers.png")