import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns

def load_process_Medical_Data(dataSet):
	## This will load up , and clean up the data.
	dataSet = (
		pd.read_csv('./../../data/processed/Processed_Medical_Data.csv')
	 	.loc[:,['age','bmi','charges']]
	 	.rename(columns={'charges':"Charges_USD"})
	 	.round({'bmi': 2, 'Charges_USD': 1})
		)

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
	## This adds an additional columns using the above function to our dataSet.
	dataSet['BMI_Category'] = dataSet.apply(categorizeBmi,axis='columns')

	## This will give us a short summary Statitistic of our data.
	dataSet.describe().round(2).loc["mean":"max"].T

	##




	return dataSet
