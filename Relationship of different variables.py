import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats
import scipy.stats as stats

df = pd.read_csv ('C:\\Users\\guzzf\\OneDrive\\Escritorio\\ESCOM-GUS-2022\\TERCER SEMESTRE\\METEDOS NUMERICOS\\Proyecto de Metodos\\redmet_2023_05.csv')
# ruta de acceso 
# antes de iniciar conectar con drive al colab.
# df = pd.read_csv ('redmet_2023_05.csv')

range_fechas = df.iloc[2677:3073,0] 
range_rh = df.iloc [2677:3073,1]
range_tmp = df.iloc [2677:3073,2]
range_wdr = df.iloc [2677:3073,3]
range_wsp = df.iloc [2677:3073,4]

confidence_level = 0.95

data = df['RH']
media_rh = np.mean(data) # media de humedad relativa
des_estand = np.std(data)
print("La media de la Humedad Relativa es:")
print(media_rh)
print("La desviacion estándar de la Humedad Relativa es:")
print(des_estand)
erro = des_estand / ((396)**1/2)
print("El error estándar es:")
print(erro)
# Cálculo de la varianza
var = 0
for i in range(len(data)):
    var += pow((data[i] - media_rh), 2)  # Asegúrate de elevar al cuadrado la diferencia
var /= len(data)

# Cálculo del intervalo de confianza para la media de RH
t_value = stats.t.ppf((1 + confidence_level) / 2, df=len(data)-1)  # Obtener el valor crítico de t
margin_of_error = t_value * (des_estand / pow(len(data), 0.5))
confidence_interval = (media_rh - margin_of_error, media_rh + margin_of_error)

print("RH")
print(f"Intervalo de confianza al {confidence_level * 100}% de la Humedad Relativa es: {confidence_interval}")

sns.set(style="whitegrid")
plt.figure(figsize=(8, 6))
sns.histplot(data, kde=True)  # Trazar un histograma y una estimación de densidad.
plt.title('Distribución Normal de la Columna Humedad Relativa')
plt.axvline(media_rh, color ='green', linestyle ='dashed', linewidth = 2, label =f'media_rh ={media_rh:.2f}')
plt.xlabel('Humedad Relativa')
plt.ylabel('periodo de mayo 2022 a 2023')
plt.legend()
plt.show()


data_2 = df['TMP']
media_TMP = np.mean(data_2) # media de humedad relativa
des_estand_2 = np.std(data_2)
print("La media de la Temperatura es:")
print(media_TMP)
print("La desviacion estándar de la Temperatura es:")
print(des_estand_2)
erro_2 = des_estand_2 / ((396)**1/2)
print("El error estándar es:")
print(erro_2)

# Cálculo de la varianza
var_2 = 0
for i in range(len(data_2)):
    var_2 += pow((data_2[i] - media_TMP), 2)  # Asegúrate de elevar al cuadrado la diferencia
var_2 /= len(data_2)

# Cálculo del intervalo de confianza para la media de RH
t_value = stats.t.ppf((1 + confidence_level) / 2, df=len(data_2)-1)  # Obtener el valor crítico de t
margin_of_error = t_value * (des_estand_2 / pow(len(data_2), 0.5))
confidence_interval = (media_TMP - margin_of_error, media_TMP + margin_of_error)

print("TMP")
print(f"Intervalo de confianza al {confidence_level * 100}% de la Temperatura es: {confidence_interval}")

sns.set(style="whitegrid")
plt.figure(figsize=(8, 6))
sns.histplot(data_2, kde=True) 
plt.title('Distribución Normal de la Columna Temperatura')
plt.axvline(media_TMP, color ='green', linestyle ='dashed', linewidth = 2, label =f'media_TMP ={media_TMP:.2f}')
plt.xlabel('Temperatura')
plt.ylabel('periodo de mayo 2022 a 2023')
plt.legend()
plt.show()

data_3 = df['WDR']
media_WDR = np.mean(data_3) # media de humedad relativa
des_estand_3 = np.std(data_3)
print("La media de la Dirección del Viento es:")
print(media_WDR)
print("La desviacion estándar de la Dirección del Viento es:")
print(des_estand_3)
erro_3 = des_estand_3 / ((396)**1/2)
print("El error estándar es:")
print(erro_3)

# Cálculo de la varianza
var_3 = 0
for i in range(len(data_3)):
    var_3 += pow((data_3[i] - media_TMP), 2)  # Asegúrate de elevar al cuadrado la diferencia
var_3 /= len(data_3)

# Cálculo del intervalo de confianza para la media de RH
t_value = stats.t.ppf((1 + confidence_level) / 2, df=len(data_3)-1)  # Obtener el valor crítico de t
margin_of_error = t_value * (des_estand_3 / pow(len(data_3), 0.5))
confidence_interval = (media_WDR - margin_of_error, media_WDR + margin_of_error)

print("WDR")
print(f"Intervalo de confianza al {confidence_level * 100}% de la Dirección del Viento es: {confidence_interval}")


sns.set(style="whitegrid")
plt.figure(figsize=(8, 6))
sns.histplot(data_3, kde=True) 
plt.title('Distribución Normal de la Columna Dirección del Viento')
plt.axvline(media_WDR, color ='green', linestyle ='dashed', linewidth = 2, label =f'media_WDR ={media_WDR:.2f}')
plt.xlabel('Dirección del Viento')
plt.ylabel('periodo de mayo 2022 a 2023')
plt.legend()
plt.show()


data_4 = df['WSP']
media_WSP = np.mean(data_4) # media de humedad relativa
des_estand_4 = np.std(data_4)
print("La media de la Velocidad del Viento es:")
print(media_WSP)
print("La desviacion estándar de la Velecidad del Viento es:")
print(des_estand_4)
erro_4 = des_estand_4 / ((396)**1/2)
print("El error estándar es:")
print(erro_4)


# Cálculo de la varianza
var_4 = 0
for i in range(len(data_4)):
    var_4 += pow((data_4[i] - media_WSP), 2)  # Asegúrate de elevar al cuadrado la diferencia
var_4 /= len(data_4)

# Cálculo del intervalo de confianza para la media de RH
t_value = stats.t.ppf((1 + confidence_level) / 2, df=len(data_4)-1)  # Obtener el valor crítico de t
margin_of_error = t_value * (des_estand_4 / pow(len(data_4), 0.5))
confidence_interval = (media_WSP - margin_of_error, media_WSP + margin_of_error)

print("WSP")
print(f"Intervalo de confianza al {confidence_level * 100}% de la Velocidad del Viento es: {confidence_interval}")



sns.set(style="whitegrid")
plt.figure(figsize=(8, 6))
sns.histplot(data_4, kde=True)  
plt.title('Distribución Normal de la Columna Velocidad del Viento')
plt.axvline(media_WSP, color ='green', linestyle ='dashed', linewidth = 2, label =f'media_WSP ={media_WSP:.2f}')
plt.xlabel('Velocidad del Viento')
plt.ylabel('periodo de mayo 2022 a 2023')
plt.legend()
plt.show()

#valor_max = max(data)
#print(valor_max)
#valor_min = min(data)
#print(valor_min)

# Cálculo de la varianza
var = 0
for i in range(len(data)):
    var += pow((data[i] - media_rh), 2)  # Asegúrate de elevar al cuadrado la diferencia
var /= len(data)

# Cálculo de la desviación estándar
desvRH = pow(var, 0.5)
print("Desviacion estandar de RH: ", desvRH)

# Cálculo del intervalo de confianza para la media de RH
confidence_level = 0.95
t_value = stats.t.ppf((1 + confidence_level) / 2, df=len(data)-1)  # Obtener el valor crítico de t
margin_of_error = t_value * (desvRH / pow(len(data), 0.5))
confidence_interval = (media_rh - margin_of_error, media_rh + margin_of_error)

print("RH")
print(f"Intervalo de confianza al {confidence_level * 100}%: {confidence_interval}")
