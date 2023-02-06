import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Cargar los datos
df = pd.read_csv("/dataset/IMDB_Dataset.csv")

# Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(df["review"], df["sentiment"], test_size=0.2)

# Convertir los datos de texto en una matriz de características
vectorizer = CountVectorizer()
X_train_features = vectorizer.fit_transform(X_train)
X_test_features = vectorizer.transform(X_test)

# Entrenar un modelo de regresión logística
clf = LogisticRegression()
clf.fit(X_train_features, y_train)

# Hacer predicciones en los datos de prueba
y_pred = clf.predict(X_test_features)

# Evaluar el rendimiento del modelo
acc = accuracy_score(y_test, y_pred)
print("Accuracy:", acc)
