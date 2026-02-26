import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import tensorflow as tf
 
# URL diretto al dataset (versione ridotta)
url = "https://raw.githubusercontent.com/defcom17/NSL_KDD/master/KDDTrain%2B_20Percent.txt"
# Colonne principali
col_names = ["duration","protocol_type","service","flag","src_bytes","dst_bytes","land","wrong_fragment","urgent","hot",
             "num_failed_logins","logged_in","num_compromised","root_shell","su_attempted","num_root","num_file_creations",
             "num_shells","num_access_files","num_outbound_cmds","is_host_login","is_guest_login","count","srv_count",
             "serror_rate","srv_serror_rate","rerror_rate","srv_rerror_rate","same_srv_rate","diff_srv_rate",
             "srv_diff_host_rate","dst_host_count","dst_host_srv_count","dst_host_same_srv_rate",
             "dst_host_diff_srv_rate","dst_host_same_src_port_rate","dst_host_srv_diff_host_rate",
             "dst_host_serror_rate","dst_host_srv_serror_rate","dst_host_rerror_rate","dst_host_srv_rerror_rate","label", "difficulty"]
 
df = pd.read_csv(url, names=col_names)
 
# 1. PREPROCESSING
# Trasformiamo la label in Binario: "normal" -> 0, tutto il resto (attacco) -> 1
df['target'] = df['label'].apply(lambda x: 0 if x == 'normal' else 1)
 
# Selezioniamo alcune feature numeriche e categoriche
features_numeric = ['duration', 'src_bytes', 'dst_bytes', 'count', 'srv_count', 'dst_host_count']
features_cat = ['protocol_type', 'service', 'flag']
 
# Creiamo il set di dati X con le sole colonne scelte
X_numeric = df[features_numeric]
X_cat = pd.get_dummies(df[features_cat]) # Trasforma 'tcp' in colonne separate (0/1)
 
# Uniamo tutto
X = pd.concat([X_numeric, X_cat], axis=1)
y = df['target']
 
print(f"Nuovo numero di feature dopo l'encoding: {X.shape[1]}")
 
# 2. NORMALIZZAZIONE (Cruciale per KNN e NN)
# Le reti soffrono se 'src_bytes' è 1.000.000 e 'logged_in' è 1.
scaler = StandardScaler()
X = scaler.fit_transform(X)
 
# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
 
print(f"Dati pronti. Feature vector size: {X_train.shape[1]}")
 
# --- CONFRONTO ---
 
# A) KNN
print("Addestramento KNN...")
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
y_pred_knn = knn.predict(X_test)
print(f"KNN Accuracy: {accuracy_score(y_test, y_pred_knn):.4f}")
 
# B) Rete Neurale (TensorFlow)
print("\nAddestramento Neural Network...")
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(X_train.shape[1],)), # Input Layer: dimensione del vettore feature
    tf.keras.layers.Dense(16, activation='relu'),      # Hidden Layer
    tf.keras.layers.Dense(8, activation='relu'),       # Hidden Layer
    tf.keras.layers.Dense(1, activation='sigmoid')     # Output Layer (0 o 1)
])
 
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=5, batch_size=32, verbose=1)
 
# Prendiamo i primi 10 campioni del test set
campioni = X_test[:10]
reali = y_test[:10].values
 
# Predizioni (per la NN usiamo una soglia di 0.5 perché l'output è una probabilità)
pred_knn = knn.predict(campioni)
pred_nn = (model.predict(campioni) > 0.5).astype(int).flatten()
 
print("Reale | KNN | NN")
for r, k, n in zip(reali, pred_knn, pred_nn):
    status = "✅" if r == k == n else "❌"
    print(f"  {r}   |  {k}  | {n}  {status}")
 
from sklearn.metrics import confusion_matrix, classification_report
print("\n--- Analisi Dettagliata KNN ---")
print(confusion_matrix(y_test, y_pred_knn))
print(classification_report(y_test, y_pred_knn, target_names=['Normal', 'Attack']))
