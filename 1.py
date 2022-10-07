name = input("Введите имя: ")
lastname = input("Введите фамилию: ")
day = input("Введите ДЕНЬ рождения: ")
month = input("Введите МЕСЯЦ рождения: ")
year = input("Введите ГОД рождения: ")
birth_date = day + "." + month + "." + year

print(name, lastname, birth_date, sep="_", )

name, lastname = lastname, name
year = int(year)
year = year + 60
year = str(year)
birth_date = day + "." + month + "." + year

print(name, lastname, birth_date, sep="_")
