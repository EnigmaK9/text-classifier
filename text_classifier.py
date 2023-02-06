"""
This module contains functions for loading data from a CSV file,
training a text classification model, and displaying the accuracy.
"""

import tkinter as tk
from tkinter import filedialog
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Función para cargar los datos desde un archivo CSV
def load_data():  
    """
    Loads data from a csv file into a pandas DataFrame

    Returns:
    -------
    df : pandas.DataFrame
        The data loaded from the csv file
    """ 
    file_path = filedialog.askopenfilename()
    df = pd.read_csv(file_path)
    return df

# Función para entrenar y evaluar el modelo
def train_model(df): 
    """
    Loads data from a csv file into a pandas DataFrame

    Returns:
    -------
    df : pandas.DataFrame
        The data loaded from the csv file
    Loads data from a csv file into a pandas DataFrame

    Returns:
    -------
    df : pandas.DataFrame
        The data loaded from the csv file
    """  
    # Dividir los datos en entrenamiento y prueba
    x_train, x_test, y_train, y_test = train_test_split(df["review"], df["label"], test_size=0.2)

    # Convertir los datos de texto en una matriz de características
    vectorizer = CountVectorizer()
    x_train_features = vectorizer.fit_transform(x_train)
    x_test_features = vectorizer.transform(x_test)

    # Entrenar un modelo de regresión logística
    clf = LogisticRegression()
    clf.fit(x_train_features, y_train)

    # Hacer predicciones en los datos de prueba
    y_pred = clf.predict(x_test_features)

    # Evaluar el rendimiento del modelo
    acc = accuracy_score(y_test, y_pred)
    result_label.config(text="Accuracy: " + str(acc))

# Configurar la GUI
root = tk.Tk()
root.title("Text Classifier GUI")

load_data_button = tk.Button(root, text="Load Data", command=load_data)
load_data_button.pack()

train_model_button = tk.Button(root, text="Train Model", command=train_model)
train_model_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()
