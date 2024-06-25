import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import RocCurveDisplay
from sklearn.metrics import accuracy_score, recall_score, balanced_accuracy_score, f1_score, precision_score,roc_auc_score


df= pd.read_csv("https://proai-datasets.s3.eu-west-3.amazonaws.com/sample_dataset.csv")

df

X = df.drop('target', axis=1).select_dtypes(exclude='object')
y = df['target']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3, random_state=0)

X_train
y_test

##preprocessing

#pulizia
cleaner = SimpleImputer()
cleaner.fit(X_train)

X_train = cleaner.transform(X_train)
X_test = cleaner.transform(X_test)

X_train

##riscalatura

scaler = StandardScaler()

scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

X_train.mean(0)

X_train.std(0)

##classificazione

##istanza di regressione logisica

model = LogisticRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

y_pred

y_test

#misurazione performance

print(classification_report(y_test, y_pred))

RocCurveDisplay.from_estimator(model, X_test, y_test)

##calcolo delle metriche individuali

accuracy_score(y_test, y_pred)

precision_score(y_test, y_pred)

recall_score(y_test, y_pred)

f1_score(y_test, y_pred)

balanced_accuracy_score(y_test, y_pred)

##area curva roc, prima calcolo delle probabilità

score = model.predict_proba(X_test) [:, 1]

roc_auc_score(y_test, model.predict_proba(X_test) [:,1])