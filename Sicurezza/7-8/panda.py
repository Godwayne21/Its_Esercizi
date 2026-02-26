import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import tensorflow as tf
import matplotlib.pyplot as plt
import seaborn as sns

# URL diretto al dataset (versione ridotta)
url = "https://raw.githubusercontent.com/defcom17/NSL_KDD/master/KDDTrain%2B_20Percent.txt"
col_names = ["duration","protocol_type","service","flag","src_bytes","dst_bytes","land","wrong_fragment","urgent","hot",
             "num_failed_logins","logged_in","num_compromised","root_shell","su_attempted","num_root","num_file_creations",
             "num_shells","num_access_files","num_outbound_cmds","is_host_login","is_guest_login","count","srv_count",
             "serror_rate","srv_serror_rate","rerror_rate","srv_rerror_rate","same_srv_rate","diff_srv_rate",
             "srv_diff_host_rate","dst_host_count","dst_host_srv_count","dst_host_same_srv_rate",
             "dst_host_diff_srv_rate","dst_host_same_src_port_rate","dst_host_srv_diff_host_rate",
             "dst_host_serror_rate","dst_host_srv_serror_rate","dst_host_rerror_rate","dst_host_srv_rerror_rate","label", "difficulty"]

df = pd.read_csv(url, names=col_names)

# --- 1. PREPROCESSING MULTI-CLASSE ---
# Invece di 0/1, usiamo LabelEncoder per mappare ogni stringa a un numero
le = LabelEncoder()
y = le.fit_transform(df['label'])
num_classes = len(le.classes_)

features_numeric = ['duration', 'src_bytes', 'dst_bytes', 'count', 'srv_count', 'dst_host_count']
features_cat = ['protocol_type', 'service', 'flag']

X_numeric = df[features_numeric]
X_cat = pd.get_dummies(df[features_cat])
X = pd.concat([X_numeric, X_cat], axis=1)

scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- 2. MODELLI ---

# A) KNN (Funziona già bene con multi-classe)
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
y_pred_knn = knn.predict(X_test)

# B) Rete Neurale (Modificata per multi-classe)
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(num_classes, activation='softmax') # Softmax per più classi
])

model.compile(optimizer='adam', 
              loss='sparse_categorical_crossentropy', # Loss specifica per numeri interi
              metrics=['accuracy'])

print("\nAddestramento Rete Neurale...")
model.fit(X_train, y_train, epochs=10, batch_size=32, verbose=0) # Aumentate epoche

# --- 3. GRAFICO E ANALISI ---
def plot_confusion_matrix(y_true, y_pred, title):
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(12, 8))
    # Usiamo solo le label presenti nel test set per il grafico
    present_labels = le.inverse_transform(np.unique(y_true))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                xticklabels=present_labels, yticklabels=present_labels)
    plt.title(title)
    plt.ylabel('Reale')
    plt.xlabel('Predetto')
    plt.xticks(rotation=45)
    plt.show()

# Mostriamo i risultati
print(f"\nAccuratezza KNN: {accuracy_score(y_test, y_pred_knn):.4f}")
y_pred_nn_probs = model.predict(X_test)
y_pred_nn = np.argmax(y_pred_nn_probs, axis=1)
print(f"Accuratezza Rete Neurale: {accuracy_score(y_test, y_pred_nn):.4f}")

# Genera il grafico per KNN
plot_confusion_matrix(y_test, y_pred_knn, "Matrice di Confusione: KNN (Dettaglio Attacchi)")

# Report testuale finale
print("\n--- Report Classificazione KNN ---")
print(classification_report(y_test, y_pred_knn, target_names=le.classes_))