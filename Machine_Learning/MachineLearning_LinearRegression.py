# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 09:57:20 2021

@author: Jesus Eduardo
"""

"Machine Learning Regression Model - Predict the time of a marathon"

import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.metrics import mean_squared_error

"------- Data Preprocessing ---------"

corredores_data=pd.read_csv('MarathonData.csv')

# View the data

print(corredores_data.info())
print("")
print(corredores_data.describe())

corredores_data["Wall21"] = pd.to_numeric(corredores_data["Wall21"], errors="coerce")
# Convert Wall 21 column in number type

print(corredores_data.info())

print("")
corredores_data=corredores_data.drop(columns=["Name"])
corredores_data=corredores_data.drop(columns=["id"])
corredores_data=corredores_data.drop(columns=["Marathon"])
corredores_data=corredores_data.drop(columns=["CATEGORY"])

print(corredores_data)

# Null values check

print("")
print(corredores_data.isna().sum()) #Revision de datos nulos

print("")
corredores_data["CrossTraining"] = corredores_data["CrossTraining"].fillna(0)
corredores_data = corredores_data.dropna(how="any")
print(corredores_data)

#6 No-numeric data process

print("")
values_category={"Category": {"MAM":1, "M45":2, "M40":3, "M50":4, "M55":5, "WAM":6}}
corredores_data.replace(values_category, inplace=True)
values_training={"CrossTraining": {"ciclista 1h":1, "ciclista 4h":4, "ciclista 13h":13, "ciclista 3h":3, "ciclista 5h":5}}
corredores_data.replace(values_training, inplace=True)
print(corredores_data)

"------- Training Model ---------"

#1 Separate the data

training_data=corredores_data.sample(frac=0.8,random_state=0)
test_data=corredores_data.drop(training_data.index)

#2 Depend and independents values

etiquetas_entrenamiento=training_data.pop("MarathonTime")
etiquetas_test=test_data.pop("MarathonTime")

#3 Choose the model

"As we has to do is predict with supervised values, choose a Linear Regression Model"

model = LinearRegression()
model.fit(training_data,etiquetas_entrenamiento)

# Evaluate the model

predicciones = model.predict(test_data)
print(predicciones)

error= np.sqrt(mean_squared_error(etiquetas_test,predicciones))
print("Accuracy: ",(1-error)*100,"%")

"------- Predictions ---------"

nuevo_corredor=pd.DataFrame(np.array([[1,400,15,0,1.4]]),columns=["Category","km4week","sp4week","Crosstrainig","Wall21"])

prediction=model.predict(nuevo_corredor)
print("Prediction is: ", prediction," hours")