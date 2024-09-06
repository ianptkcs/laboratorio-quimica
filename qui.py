import numpy as np
import matplotlib.pyplot as plt
import os

data = []

# Lendo todos os arquivos no diretório 'data/'
data_dir = 'data/'
for filename in os.listdir(data_dir):
    if filename.endswith('.txt'):  # Assumindo que os arquivos são .txt
        file_path = os.path.join(data_dir, filename)
        with open(file_path, 'r') as file:
            # Leia o conteúdo do arquivo e adicione-o à lista 'data'
            # Ajuste esta parte de acordo com o formato dos seus arquivos
            data.append(np.loadtxt(file))

# Convertendo a lista para um array numpy
data = np.array(data)

# Resto do seu código
media = np.mean(data, axis=0)
desvio = np.std(data, axis=0)

# Criando um array para o eixo x
x = np.arange(len(media))

plt.errorbar(x, media, yerr=desvio, fmt='o', capsize=5, label=r'Nb$_2$O$_5$ - HY/Co')
plt.xlabel('Tempo (s)')
plt.title('Comparação para 100 mg')
plt.ylabel(r'Volume de H$_2$ (ml)')
plt.legend()
plt.show()