import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns

def load_and_process():
    ## This will load up , and clean up the data.
    
    df_processed = (
        pd.read_csv('./../data/raw/Medical_Cost.csv')
        .loc[:,['bmi','smoker','region','charges']]
        .rename(columns={'bmi':'BMI','smoker':'Smoker','region':'Region','charges':'MedicalCosts_USD'})
        .assign(Smoker_bin=lambda x: np.where((x['Smoker']) == 'yes', 1, 0))
        .round({'BMI':2, 'MedicalCosts_USD':3})
    )

    def categorizeBmi(row):
        bmi = float(row['BMI'])
        if bmi < 18.59:
            return "Underweight"
        elif bmi < 25.0:
            return "Normal"
        elif bmi <29.99:
            return "Overweight"
        elif bmi >= 30.0:
            return "Obese"
    
    ## This adds an additional column using the above function to our dataSet.
    df_processed['BMI_Category'] = df_processed.apply(categorizeBmi,axis='columns')
    ## This drops the duplicates
    df_processed.drop_duplicates(inplace=True)

    return df_processed
