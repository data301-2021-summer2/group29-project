import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns



def categorizeBmi(row):
	bmi = float(row['bmi'])
	if bmi < 18.59:
		return "Underweight"
	elif bmi < 24.99:
		return "Normal"
	elif bmi <29.99:
		return "Overweight"
	elif bmi >= 30.0:
		return "Obese"


def load_Process_data():
	dataSet = (
		pd.read_csv('./../../data/processed/Processed_Medical_Data.csv')
	 	.loc[:,['bmi','charges']]
	 	.rename(columns={'charges':"Charges_USD"})
	 	.round({'bmi': 2, 'Charges_USD': 1})
		.astype({'bmi':float})

		)
	dataSet['BMI_Category'] = dataSet.apply(categorizeBmi,axis='columns')
	return dataSet

def printrandom():
	print("This is random world")

