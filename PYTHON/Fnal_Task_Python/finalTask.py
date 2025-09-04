import pandas as pd
import numpy as np
df = pd.read_csv("orders.csv")

df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
df["returned"] = df["returned"].astype(bool)
df["discount"] = df["discount"].astype(float)
df["quantity"] = df["quantity"].astype(int)
df["shipping_cost"] = df["shipping_cost"].astype(float)
df["unit_price"] = df["unit_price"].astype(float)


if (df["quantity"] < 1).any():
    raise ValueError("Ошибка: количество должно быть ≥ 1")

if (df["unit_price"] <= 0).any():
    raise ValueError("Ошибка: цена должна быть > 0")

if ((df["discount"] < 0) | (df["discount"] > 0.8)).any():
    raise ValueError("Ошибка: скидка должна быть в пределах [0, 0.8]")

print("Все проверки пройдены успешно")
df["order_month"] = df["order_date"].dt.strftime("%B")
df['gross'] = df["quantity"] * df["unit_price"]
df["net"] = df["gross"] * (1 - df["discount"]) + df["shipping_cost"]
df.loc[df["returned"], "net"] = 0
print(df)

