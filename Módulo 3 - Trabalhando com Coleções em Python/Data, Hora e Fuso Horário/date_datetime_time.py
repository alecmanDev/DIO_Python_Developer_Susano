''' O módulo datetime é usado para trabalhar com horas '''

from datetime import date, datetime, time

# date()
d = date(2025, 3, 7)
print(d) # 2025-03-07


# date.today()
print(date.today()) # O dia, mês e ano local


# datetime
data_hora = datetime(2025, 3, 7, 8, 57, 50)
print(data_hora) # 2025-03-07 08:57:50


# datetime.today()
print(datetime.today())


# time()
hora = time(10, 22, 0)
print(hora)