def load_process_Medical_Data(dataSet):
	dataSet = (
		pd.read_csv('./data/Medical_Cost.csv')
	 	.loc[:,['age','bmi','charges']]
	 	.rename(columns={'charges':"Charges_USD"})
	 	.round({'bmi': 2, 'Charges_USD': 1})
		)

	dataSet['BMI_Category'] = dataSet.apply(categorizeBmi,axis='columns')

	return dataSet
