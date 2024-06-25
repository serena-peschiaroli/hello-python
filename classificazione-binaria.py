#Partendo dal dataset fornito nella pratica:
#realizzare un modello di classificazione binaria su tutte le sue variabili numeriche e calcolare la sua accuratezza
#realizzare un altro modello considerando solo le prime 5 variabili numeriche e calcolare la sua accuratezza
#Confrontare i due modelli e commentare le loro performance

#Suggerimento: per considerare le prime 5 variabili di un dataframe utilizzare df.iloc[:,0:5]

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import RocCurveDisplay
from sklearn.metrics import accuracy_score, recall_score, balanced_accuracy_score, f1_score, precision_score,roc_auc_score

# caricaamento del dataset

df = pd.read_csv("https://proai-datasets.s3.eu-west-3.amazonaws.com/sample_dataset.csv")

#separazione delle caratteristiche e del target

X = df.drop('target', axis=1).select_dtypes(exclude='object')
y = df['target']

#divisione del dataset in training set e test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

#pre-elaborazione: pulizia dei dati

cleaner = SimpleImputer()
cleaner.fit(X_train)
X_train = cleaner.transform(X_train)
X_test = cleaner.transform(X_test)

#pre-elaborazione: riscalatura dei dati

scaler =  StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test=scaler.transform(X_test)

# Creazione e addestramento del modello di regressione logistica con tutte le variabili numeriche
model_all = LogisticRegression()

model_all.fit(X_train, y_train)

#predizione e valutazione delle performance

y_pred_all = model_all.predict(X_test)

print("Performance del modello con tutte le variabili numeriche:")
print(classification_report(y_test, y_pred_all))
accuracy_all = accuracy_score(y_test, y_pred_all)
print(f'Accuracy: {accuracy_all}')

# Selezione delle prime cinque variabili numeriche
X5 = df.iloc[:, 0:5]
y = df['target']

# Divisione del dataset in training set e test set
X5_train, X5_test, y_train, y_test = train_test_split(X5, y, test_size=0.3, random_state=0)

# Pre-elaborazione: Pulizia dei dati
cleaner.fit(X5_train)
X5_train = cleaner.transform(X5_train)
X5_test = cleaner.transform(X5_test)

# Pre-elaborazione: Riscalatura dei dati
scaler.fit(X5_train)
X5_train = scaler.transform(X5_train)
X5_test = scaler.transform(X5_test)

# Creazione e addestramento del modello di regressione logistica con le prime cinque variabili numeriche
model_5 = LogisticRegression()
model_5.fit(X5_train, y_train)

# Predizione e valutazione delle performance
y_pred_5 = model_5.predict(X5_test)

print("\nPerformance del modello con le prime cinque variabili numeriche:")
print(classification_report(y_test, y_pred_5))
accuracy_5 = accuracy_score(y_test, y_pred_5)
print(f'Accuracy: {accuracy_5}')

#confrtontO:

print("\nConfronto delle performance dei due modelli:")
print(f'Accuracy con tutte le variabili numeriche: {accuracy_all}')
print(f'Accuracy con le prime cinque variabili numeriche: {accuracy_5}')

# Visualizzazione della curva ROC per entrambi i modelli
RocCurveDisplay.from_estimator(model_all, X_test, y_test)
RocCurveDisplay.from_estimator(model_5, X5_test, y_test)
