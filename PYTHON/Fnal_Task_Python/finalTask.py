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

rep_file = "/Users/Alyona_Arlova/Desktop/DE03-onl-Alyona-Arlova/PYTHON/Fnal_Task_Python/report_overview.csv"
rep_top = "/Users/Alyona_Arlova/Desktop/DE03-onl-Alyona-Arlova/PYTHON/Fnal_Task_Python/report_top_products.csv"
rep_month = "/Users/Alyona_Arlova/Desktop/DE03-onl-Alyona-Arlova/PYTHON/Fnal_Task_Python/report_monthly.csv"
rep_country = "/Users/Alyona_Arlova/Desktop/DE03-onl-Alyona-Arlova/PYTHON/Fnal_Task_Python/report_countries.csv"
try:
    with (open(rep_file, "w") as report_overview, open(rep_top, "w") as rep_topN,
          open(rep_month, "w") as rep_monthly, open(rep_country, "w") as rep_countries):
        gross_sum = df['gross'].sum()
        netto_sum = df['net'].sum()
        df['total_order'] = df['unit_price'] * df['quantity'] * (1 - df['discount'])
        avg_check = df['total_order'].mean()
        number_unique_customer = df['customer_id'].nunique()
        median_check = df['total_order'].median()
        return_shares = df["returned"].value_counts(normalize=True) * 100
        top_products_qty = df.groupby("product")["quantity"].sum().sort_values(ascending=False)
        country_stats = df.groupby("country").agg(
            orders_count=("country", "count"),  # number of orders
            total_sales=("total_order", "sum")  # sum of sales
        ).sort_values(by="total_sales", ascending=False)
        monthly_sales = df.groupby("order_month")["total_order"].sum().sort_index()
        rep_monthly.write("Month,Total Sales\n")
        for month, sales in monthly_sales.items():
            rep_monthly.write(f"{month},{sales}\n")
        rep_countries.write(f"Country VS Product VS Sales: {country_stats}\n")
        rep_topN.write(f"Top products by quantity sells:{top_products_qty}\n")
        report_overview.write(f"Return shares (%):\n{return_shares}\n")
        report_overview.write(f"Number of unique customers: {number_unique_customer}\n")
        report_overview.write(f"Median check: {median_check}\n")
        report_overview.write(f"Average check: {avg_check}\n")
        report_overview.write(f"Gross sum: {gross_sum}\n")
        report_overview.write(f"Netto sum: {netto_sum}\n")
except FileNotFoundError:
    print("File does not exist!")
finally:
    print("Finish!")

