"""
===========================================
 Análisis de Datos Simulados
===========================================

Autor      : Néstor O. Vásquez C.
Proyecto   : DATA-ANALYTICS
Versión    : 1.0
Fecha      : 08/07/2025
Descripción:
    Este script genera un conjunto de datos ficticio utilizando listas
    o estructuras definidas manualmente. Posteriormente, aplica análisis 
    básico como inspección del DataFrame y estadísticas descriptivas.

Entradas:
    - Datos generados internamente (no se utilizan archivos externos)

Salidas:
    - Impresión en consola del DataFrame y estadísticas básicas

Requisitos:
    - pandas

Uso:
    python scripts/analisis_datos_simulados.py
"""

# Modulo para importat librerias del Proyecto:
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

# Creación de Diccionario para simulación de datos:
Data = {
    'Edad':[20, 38, 40, 45, 25, 32, 18],
    'Ingresos':[1600000, 3600000, 4500000, 4600000, 2500000, 3200000, 1200000]
}

# Se convierte el Diccinario a un Pandas Data Frame y se imprime el resultado en df:
df = pd.DataFrame(Data)
print(df)

# Crear gráfico
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Edad', y='Ingresos', color='red', s=100)

# Agregar una etiqueta por cada punto
for i in range(len(df)):
    edad = df.loc[i, 'Edad']
    ingresos = df.loc[i, 'Ingresos']
    texto = f"{int(edad)} años\n${int(ingresos)}"
    
    # Mostrar el texto ligeramente desplazado del punto para mejor visibilidad
    plt.text(edad + 0.5, ingresos + 50, texto, fontsize=9, color='black')

plt.title('Relación entre Edad e Ingresos', fontsize=14)
plt.xlabel('Edad')
plt.ylabel('Ingresos')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()