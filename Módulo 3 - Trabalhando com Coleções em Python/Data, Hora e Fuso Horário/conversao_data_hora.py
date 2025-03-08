import datetime

d = datetime.datetime.now()

# Formatando data e hora
print(d.strftime("%d/%m/%Y %H:%M"))

# Convertendo string para datetime
date_string = "08/03/2025 15:30"
d = datetime.datetime.strptime(date_string, "d%/%m/%Y %H:%M")
print(d)