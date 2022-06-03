from itertools import product


product = {
    "city":        "Москва",
    "temperature":  "20"
}
print (product["city"])
product ["temperature"] = "15"
print (product)
print (product.get("country", "Россия"))
product ["date"] = "27.05.2019"
print(product)
print(len(product))