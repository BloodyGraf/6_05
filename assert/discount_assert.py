def apply_discount(price, discount):
    return int(float(price) * (1.0 - float(discount)))

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            content = f.readlines()
    except FileNotFoundError:
        print(f"неверное имя файла  {filename}")
    else:
        return content

def write_file(filename, data):
    try:
        with open(filename, 'w') as f:
            for d in data:
                f.write(f"{str(d)}\n")
    except FileNotFoundError:
        # pass
        print(f"неверное имя файла  {filename}")

data = read_file("../files/data.txt")
discount = read_file("../files/discount.txt")

result_data = []
counter = 0
for d in data:
    i = d.split(",")
    result_data.append(f"{i[0]}, {apply_discount(i[1],discount[counter])}")
    counter += 1

write_file("../files/discounted_prices.txt", result_data)