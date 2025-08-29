#Что нужно сделать дома?
# Создайте программу, которая загружает данные из REST API, выполняет предварительную обработку данных
# (удаление пропущенных значений, преобразование типов), и сохраняет очищенные данные в новый CSV файл.
import requests
import pandas as pd

#example of JSON:
# {"message": { "bulldog": ["boston", "english", "french"],
# "pug": [],
# "beagle": [] },
# "status": "success"}

url = "https://dog.ceo/api/breeds/list/all" # dog api
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
else:
    raise Exception(f"Ошибка загрузки данных: {response.status_code}")

breeds_dict = data["message"]
rows = []
for breed, sub_breeds in breeds_dict.items():
    if sub_breeds:  # if sub breed exists
        for sub in sub_breeds:
            rows.append({"breed": breed, "sub_breed": sub})
    else:
        rows.append({"breed": breed, "sub_breed": None})


df = pd.DataFrame(rows) #dataFrame

print("Original data:")
print(df.head())

df = df.dropna(subset=["breed"])  # remove rows without breed
df["breed"] = df["breed"].astype(str)
df.to_csv("/Users/Alyona_Arlova/Desktop/DE03-onl-Alyona-Arlova/PYTHON/HW9/dog_new.csv")
print("Check dog new file")




