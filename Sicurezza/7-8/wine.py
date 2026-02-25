import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier # <--- Nuovo import per la Rete Neurale
from sklearn.metrics import classification_report, accuracy_score
import pandas as pd

# 1. Caricamento dati (Originale)
wine = load_wine()
data = wine.data
target = wine.target

# 2. Preparazione (Necessaria per le Reti Neurali)
X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.3)

# Le Reti Neurali SONO ESTREMAMENTE SENSIBILI allo scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 3. Creazione della Rete Neurale
# hidden_layer_sizes=(10, 10) crea 2 strati interni con 10 neuroni ciascuno
# max_iter=1000 dà tempo alla rete di "imparare"
mlp = MLPClassifier(hidden_layer_sizes=(10, 10), max_iter=1000, random_state=1)
mlp.fit(X_train_scaled, y_train)

# Predizioni
y_pred = mlp.predict(X_test_scaled)

# --- STAMPA RISULTATI ---
print("--- RISULTATI RETE NEURALE (MLP) ---")
print(f"Accuratezza: {accuracy_score(y_test, y_pred):.2%}")
print("\nReport di Classificazione:")
print(classification_report(y_test, y_pred, target_names=wine.target_names))

# 4. Scatter plot originale
fig, ax = plt.subplots()
x_index, y_index = 2, 9
colors = ['blue', 'red', 'green']

for label, color in zip(range(len(wine.target_names)), colors):
    ax.scatter(data[target==label, x_index], 
                data[target==label, y_index],
                label=wine.target_names[label],
                c=color, alpha=0.6)

ax.set_title(f"Rete Neurale - Accuratezza: {accuracy_score(y_test, y_pred):.2%}")
ax.set_xlabel(wine.feature_names[x_index])
ax.set_ylabel(wine.feature_names[y_index])
ax.legend()
plt.show()

# Scatter matrix originale
pd.plotting.scatter_matrix(pd.DataFrame(data, columns=wine.feature_names), c=target, figsize=(10, 10))
plt.show()