import pandas as pd
import numpy as np
def load_and_process(dataSet):
    
    df1 = (
        pd.read_csv(dataSet)
        .loc[:,['bmi','smoker','region','charges']]
        .rename(columns={'bmi':'BMI','smoker':'Smoker','region':'Region','charges':'MedicalCosts_USD'})
        .assign(Smoker_bin=lambda x: np.where((x.Smoker) == 'yes', 1, 0))
        .round({'BMI':2, 'MedicalCosts_USD':3})
    )
    
    return df1