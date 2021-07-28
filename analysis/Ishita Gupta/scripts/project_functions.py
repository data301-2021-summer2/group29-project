import pandas as pd
import numpy as np
def load_and_process(dataSet):
    
    #Method Chain 1 - to load data
    df1 = (
        pd.read_csv('/Users/ISHITA GUPTA/Documents/COSC301/group29-project/data/raw/Medical_Cost.csv')
        .loc[:,['bmi','smoker','region','charges']]
    )
    
    #Method Chain 2 - To clean and process data
    df2 = (
        df1
        .rename(columns={'bmi':'BMI','smoker':'Smoker','region':'Region','charges':'MedicalCosts_USD'})
        .round({'BMI':2, 'MedicalCosts_USD':3})
    )
    
    return df2