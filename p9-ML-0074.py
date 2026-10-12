# Jaquez Andres 0074
import pandas as pd # type: ignore

print("Jaquez Andres 0074")

# Punto 12: código de prueba
print(pd.__version__)

# Punto 13: Caso práctico (Python + Pandas)
# Número de lista 31 -> datos1
datos1 = {
    'distancia_km': [2.5, 4.0, 1.2, 5.8, 3.1],
    'trafico_nivel': [1, 3, 1, 3, 2],
    'edad_repartidor': [22, 35, 19, 28, 40],
    'tiempo_entrega_min': [15, 32, 10, 42, 25]
}

df = pd.DataFrame(datos1)

print("\n=== DATASET COMPLETO (datos1) ===")
print(df)

# Features (X): variables de entrada
X = df[['distancia_km', 'trafico_nivel', 'edad_repartidor']]

# Target (y): lo que queremos predecir
y = df['tiempo_entrega_min']

print("\n=== FEATURES (X) ===")
print(X.head(2))

print("\n=== TARGET (y) ===")
print(y.head(2))

print("\nForma de X:", X.shape)
print("Forma de y:", y.shape)

print("\nJaquez Andres 0074")
# Jaquez Andres 0074
