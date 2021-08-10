import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns

def load_process_Medical_Data(data):
	## This will load up , and clean up the data.
	"""
	Feed this function the Medical dataset from 
	"""
	dataSet = (
		pd.read_csv(data)
	 	.loc[:,['bmi','charges']]
	 	.rename(columns={'charges':"Charges_USD"})
	 	.round({'bmi': 2, 'Charges_USD': 1})
		.astype({'bmi':float})
		
		)
	## This will update the dataset in my directory.
	dataSet.to_csv('./data/processed/Medical_Cost.csv')
	## Adding more informative columns to our data Set.
	def categorizeBmi(row):
		bmi = float(row['bmi'])
		if bmi < 18.59:
			return "Underweight"
		elif bmi < 25.0:
			return "Normal"
		elif bmi <29.99:
			return "Overweight"
		elif bmi >= 30.0:
			return "Obese"
	## This adds an additional columns using the above function to our dataSet.
	dataSet['BMI_Category'] = dataSet.apply(categorizeBmi,axis='columns')

	## This will give us a short summary Statitistic of our data.
	dataSet.describe().round(2).loc["mean":"max"].T

	##

	return dataSet
