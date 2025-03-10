'''O Python gerencia fusos horários usando o módulo datetime em conjunto com a biblioteca pytz. Isso é útil para converter horários entre diferentes regiões do mundo.'''

# pip install pytz
from datetime import datetime, timezone, timedelta
import pytz

# Criando datetime com timezone
d = datetime.now(pytz.timezone('Europe/Oslo'))
d2 = datetime.now(pytz.timezone('America/Sao_Paulo'))

print(d)
print(d2)

# Trabalhando com tz sem bibliotecas externas
# Criando datetime com timezone
data_oslo = datetime.now(timezone(timedelta(hours=2), 'OSL'))
date_sp = datetime.now(timezone(timedelta(hours=-3), 'SP'))

print(data_oslo)
print(date_sp)