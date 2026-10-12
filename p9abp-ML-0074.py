# Jaquez Andres 0074
import pandas as pd # type: ignore

print("Jaquez Andres 0074")

# Punto 12: código de prueba
print(pd.__version__)

# Reto ABP: Diagnóstico de diabetes
# Un hospital quiere predecir si un paciente tiene riesgo de diabetes
# antes de hacer análisis complejos.
datos_pacientes = {
    'id_paciente': [101, 102, 103, 104, 105, 106, 107, 108],
    'edad': [45, 32, 58, 27, 63, 51, 39, 70],
    'nivel_glucosa': [148, 85, 183, 89, 137, 166, 110, 197],
    'presion_arterial': [72, 66, 64, 66, 40, 74, 80, 70],
    'indice_masa_corporal': [33.6, 26.6, 23.3, 28.1, 43.1, 30.5, 25.8, 35.2],
    'diagnostico_diabetes': [1, 0, 1, 0, 1, 1, 0, 1]
}

df = pd.DataFrame(datos_pacientes)

print("\n=== DATASET DE PACIENTES ===")
print(df)

# 1. Target (y): lo que el modelo debe predecir
y = df['diagnostico_diabetes']

# 3. Columna eliminada: id_paciente solo identifica al paciente,
#    no describe ninguna característica médica, no ayuda a predecir.
df_limpio = df.drop(columns=['id_paciente'])

# 2. Features (X): las pistas que describen al paciente
X = df_limpio.drop(columns=['diagnostico_diabetes'])

print("\n=== 1. TARGET (y) ===")
print(y.head())

print("\n=== 2. FEATURES (X) ===")
print(X.head())

print("\n=== 3. COLUMNA ELIMINADA ===")
print("id_paciente: es solo un número de identificación y no aporta")
print("información médica útil para detectar el riesgo de diabetes.")

print("\nForma de X:", X.shape)
print("Forma de y:", y.shape)
print("\nPacientes con diabetes (1) y sin diabetes (0):")
print(y.value_counts())

print("\nJaquez Andres 0074")
# Jaquez Andres 0074
