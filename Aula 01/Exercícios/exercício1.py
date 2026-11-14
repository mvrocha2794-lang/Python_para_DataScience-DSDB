import pandas as pd
import matplotlib.pyplot as plt 

dados = {
    'tempo': ['08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00' '16:00', '17:00'],
    'temperatura':[25, 28, 32, 35, 38, 42, 45, 41, 37, 33]
}

df= pd.DataFrame(dados)

df.plot (
x = 'tempo',
y = 'temperatura',
kind ='bar',
legend = False
)

plt.title('Visualização de temperatura')
plt.ylabel('Tempo(HORAS)')
plt.xlabel('Temperatura(C°)')
plt.show()

