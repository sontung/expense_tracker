import random
from pathlib import Path


def create_dummy_file(file_name="data.txt"):
    my_file = Path(file_name)
    if my_file.is_file():
        pass
    else:
        pass
    a_file = open(file_name, "w")
    categories = {"dairy": ["milk", "yogurt"], "breakfast": ["bread", "cereal"], "fruits": ["kale", "orange", "banana"]}
    for i in range(50):
        cat = random.choice(list(categories.keys()))
        prod = random.choice(categories[cat])
        print(f"{prod} {cat} {random.random()*10}", file=a_file)


def track(file_name="data.txt"):
    my_file = Path(file_name)
    data = {}
    cat2price = {}
    prod2price = {}
    if my_file.is_file():
        with open(file_name) as f:
            contents = f.readlines()
            for line in contents:
                if len(line) > 0 and not line.isspace():
                    line = line.rstrip()
                    product, category, price = line.split(" ")
                    price = float(price)

                    if product not in prod2price:
                        prod2price[product] = price
                    else:
                        prod2price[product] += price

                    if category not in data:
                        data[category] = {product: price}
                        cat2price[category] = price
                    else:
                        cat2price[category] += price
                        if product not in data[category]:
                            data[category][product] = price
                        else:
                            data[category][product] += price
    print("here is your food bill")
    sorted_categories = sorted(list(cat2price.keys()), key=lambda x: cat2price[x], reverse=True)
    total_bill = sum(list(cat2price.values()))
    for cat in sorted_categories:
        print()
        print(f"{cat} {cat2price[cat]} aud {round(cat2price[cat]/total_bill*100, 2)} %")
        sorted_products = sorted(list(data[cat].keys()), key=lambda x: data[cat][x], reverse=True)
        for prod in sorted_products:
            total_bill_local = sum(list(data[cat].values()))
            prod_price = data[cat][prod]
            print(f"  {prod} {prod_price} aud\n"
                  f"    {round(prod_price/total_bill_local*100, 2)} % of this category\n"
                  f"    {round(prod_price/total_bill*100, 2)} % of total bill")

    print("\nhere your most expensive products\n")
    sorted_products = sorted(list(prod2price.keys()), key=lambda x: prod2price[x], reverse=True)
    total_bill = sum(list(prod2price.values()))
    for prod in sorted_products:
        print(f"  {prod} {prod2price[prod]} aud, {round(prod2price[prod]/total_bill*100, 2)} %")


if __name__ == '__main__':
    track()
