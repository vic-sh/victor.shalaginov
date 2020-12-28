#[{'Yandex': 'yandex.ru'}, {'Google': 'google.ru'}]

list_final = []

with open('dns.txt', 'r') as file:
    for line in file:
        list = line.split()
        list_final.append(dict([(list[1], list[0])]))

print(list_final)