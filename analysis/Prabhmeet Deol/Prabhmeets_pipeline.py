import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns

dataSet =(
	 pd.read_csv('./data/Medical_Cost.csv')
	 .loc[:,['age','bmi','charges']]
	 .rename(columns={'charges':"Charges_USD"})
	 .round({'bmi': 2, 'Charges_USD': 1})
	 )
#dataSet = dataSet[dataSet['bmi']<40]
## Adding more informative columns to our data Set.
def categorizeBmi(bmiSet):
	bmi = bmiSet['bmi']
	if bmi <18.5:
		return "Underweight"
	elif bmi < 24.9:
		return "Normal"
	elif bmi <29.9:
		return "Overweight"
	elif bmi > 30.0:
		return "Obese"
dataSet['BMI_Category'] = dataSet.apply(categorizeBmi,axis='columns')