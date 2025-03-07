from datetime import date, datetime, timedelta, time

# Criando data e hora

tam_carro = 'P'
t_peq = 30
t_med = 45
t_gra = 60
data_atual = datetime.now() # Data e hora atual com fuso atual

if tam_carro == "P":
    data_estimada = data_atual + timedelta(minutes=t_peq)
    print(f'O carro chegou: {data_atual} e ficará pronto às {data_estimada}')
          
elif tam_carro == "M":
    data_estimada = data_atual + timedelta(days=t_med)
    print(f'O carro chegou: {data_atual} e ficará pronto às {data_estimada}')
else:
    data_estimada = data_atual + timedelta(minutes=t_gra)
    print(f'O carro chegou: {data_atual} e ficará pronto às {data_estimada}')

print(date.today() - timedelta(days=1))


# Print apenas para exibir a hora
resultado = datetime(2025, 3, 7, 10, 19, 20) - timedelta(hours=1)
print(resultado.time())

# Print apenas na data
print(datetime.now().date())