#еализуйте программу в модуле main.py, которая использует функцию make_order(product, qty)
# из модуля shop.py для оформления заказа. В модуле shop.py хранится словарь с товарами и их ценами.
# Пользователь вводит название товара и количество, функция проверяет, есть ли такой товар,
# и если он найден, считает общую стоимость и возвращает строку с информацией о заказе.
# Если товара нет — возвращается сообщение «Товар не найден». Заказы сохраняются в файл orders.txt.

products = {"Phone": 400, "Laptop": 1000,
            "Monitor": 50, "Keyboard": 25,
            "Memory card": 90}

def make_order(product, qty):
    if product in products:
        total_price = qty * products[product]
        order_info = f"Total price for {product} ({qty} qty.) is {total_price}"
        print(order_info)
        with open("/Users/Alyona_Arlova/Desktop/DE03-onl-Alyona-Arlova/PYTHON/HW6/orders.txt", "a") as Order:
            Order.write(order_info + "\n")
        return order_info
    else:
        print("Товар не найден")
        return None

