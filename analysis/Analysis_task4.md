# This is the file where we conduct our final analysis - Task 4

## Ishita's Analysis:
*My Research questions:*
- Does the geographical location play a part in increased medical costs?
- Is there a relationship or correlation between being a smoker and having higher medical costs?

I used a lot of plots and graphs to visualize my dataset to help answer my research questions.

When I created a correlation matrix, I observed that the pearson correlation coefficient, which is a measure of the linear association between two variables, had a very high value of 0.79 between the \"Medical Costs\" and the \"Smoker\" variable. This indicates that there is a positive linear correlation between the variables.

A scatterplot of Medical charges by regions in the USA showed that there is not a significant difference in the medical charges amongst the different regions. To further explore this relationship, I created a boxplot and a violinplot. Both of these plots also suggested that there was no notable difference in the medical charges. However, both of these plots demonstrated that the 'southeast' region had higher medical costs, while 'southwest' seemed to have the least costs.

The plots can be found below:

![Region Plots](../images/region.jpeg)

*Note:* 
- All of the data and code used to create these plots can be found in my analysis folder (Ishita Gupta).
- If the above image is not visible on GitHub, it can be viewed by going to images/region.jpeg

Next, I analyzed the relationship between the 'Smoker' variable and the 'Medical Charges' variable.

I started by creating a boxplot of medical charges by whether the person is a smoker or not. This boxplot displayed immense evidence that a smoker has higher medical costs on average. The minimum value of the medical costs of a smoker also appears to be higher than the value of the upper quartile of a non-smoker.

I also created two barplots displaying the medical charges by 'region' and 'smoker'. This was to combine both my research questions and visualize the data together. Both of the barplots confirmed the previous observations that there was not much evidence to say that a particular region had much higher medical costs and that it was very evident that a smoker had to incur more medical charges in the United States.

These plots can be found below:

![Smoker and Region Plots](../images/smoker.jpeg)

*Note:* If the above image is not visible on GitHub, it can be viewed by going to images/smoker.jpeg

### Conclusion:

Upon analyzing and visualizing the data, we can reach the following conclusions:

- There does not appear to be a causal relationsip or a correlation amongst the different regions in the United States and the medical charges people incur in those areas. However, it is apparent that the 'southeast' region has a higher medical cost. This could be explored by experts, who could conduct research and collect more data to better understand this relationship.
- There appears to be a strong correlation among whether the person is a smoker and their medical charges. However, when the data was analyzed, it was found that the number of non-smokers in the dataset were far greater than the number of smokers. This difference in the count could also be a factor in this vast difference in the medical costs.

## Prabhmeet's Analysis:
First we will import pandas, and use it to read the dataset. As well as do some method cleaning, and some data Wrangling. All of that has been Chained together, in this chunk , below for the purpose of ease to read , and debug.

Also a function was built , that used method chanining to clean , process, and wrangle the data, and act as a pipeline. In this section we use that function to load in our data. The function was placed inside the scripts folder 

```
import pandas as pd
from pandas_profiling import ProfileReport as pf
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
%matplotlib inline

## Using a seperate file to import our functions.
from scripts import project_functions as fun
%load_ext autoreload
The autoreload extension is already loaded. To reload it, use:
  %reload_ext autoreload
```
Now we will use a pandas profiling library to get a brief overiview of our data , and look over some of the plots of our dataset.

```
pf(dataSet).to_notebook_iframe()
```
Followowing changes were made after reading, and exploring the Profile report.

-  Using this the categorize BMI was improved, as the previous version was leaving the dataset with several nan values. 

-  Also some duplicate values were observed which were also removed(This change was made in the data processing file).
-   Also a decision was made to add a new column of BMI Category to help categorize the BMI's for easier understanding when producing plots.



Now we will explore some decriptive statistics on our dataSet.

```py
dataSet.describe().round(0).rename({'50%':'Median'}).drop(columns='Smoker_bin').T
```

![Stats1](Prabhmeets_images/Stats1.png)



The following code gives us some statistical data to explore the previous found co-relation in my EDA. 

**Conclusion** : The mean Medical charge for the Obese group is found to be the highest. Although the difference between Normal and Overweight (mean Medical Charges) does not seem to be much.

```
dataSet.groupby('BMI_Category').agg(['mean','std','median','min','max']).round(1).drop(columns={'BMI'})
```
![Stats2](Prabhmeets_images/Stats2.png)

The following code was used to explore the percentage of US Population that is under the Obese Category. During my Exploratory analysis i got an intuition, that a good amount of American citizens have higher BMI than normal , that is they have BMI more the an 24.9 which is considered unhealthy.

 - From the plots below , it can be concluded that more than 50 percentil of the US population can be categorized as having , an unhealthy BMI. 
```
fig, ax =plt.subplots(1,2,figsize=(15,5))
sns.countplot(dataSet['BMI_Category'],ax=ax[0]).set(
	xlabel = "BMI Category",
	title="Count of Different BMI Categories in the data Set.",
	
)
sns.kdeplot(
   data=dataSet, x="BMI",fill=True,ax=ax[1]
).set(
	xlabel = "BMI",
	title="Density of BMI of various American Citizens.",
	
)

```
![Plot1](Prabhmeets_images/plot1.png)

The following code will help us explore the relationship between BMI Category, and Medical Charges.
```
fig, ax =plt.subplots(2,2,figsize=(15,10))

boxplot = sns.boxplot(
	data = dataSet,
	x="BMI_Category",
	y="MedicalCosts_USD",
	order=['Underweight','Normal','Overweight','Obese'],
	ax=ax[0][0]

)
boxplot.set(
	#yscale="log",
	xlabel="BMI Category",
	ylabel="Mean Medical Charges in USD",
	title="Boxplot",
)
logboxplot = sns.boxplot(
	data = dataSet,
	x="BMI_Category",
	y="MedicalCosts_USD",
	order=['Underweight','Normal','Overweight','Obese'],
	ax=ax[0][1],

)
logboxplot.set(
	yscale="log",
	xlabel="BMI Category",
	ylabel="Log Transformed Mean Medical Charges in USD",
	title="Log Transformed Boxplot",
)
barplot = sns.barplot(
	data = dataSet,
	x="BMI_Category",
	y="MedicalCosts_USD",
	order=['Underweight','Normal','Overweight','Obese'],
	ax=ax[1][1],
)
barplot.set(
	xlabel="BMI Category",
	ylabel="Mean Medical Charges in USD",
	title="Barplot",
)
sns.violinplot(
	data = dataSet,
	x="BMI_Category",
	y="MedicalCosts_USD",
	order=['Underweight','Normal','Overweight','Obese'],
	ax=ax[1][0],

).set(
	#yscale="log",
	xlabel="BMI Category",
	ylabel="Medical Charges in USD",
	title="Violon plot.",
)
fig.tight_layout(h_pad=4,w_pad=10)
plt.suptitle("Different plots comapring mean Medical Charges of American Citizens",y=1.05)
fig.show()

```
![Plot2](Prabhmeets_images/plot2.png)

```
fig, ax =plt.subplots(1,2,figsize=(15,5))
scatter1=sns.scatterplot(
	data=dataSet,
	x="BMI",
	y="MedicalCosts_USD",
	hue="BMI_Category",
	ax=ax[0],
	)
scatter1.set(
	xlabel="BMI",
	ylabel="Medical Charges in USD",
	title="Normal",
)
scatter1=sns.scatterplot(
	data=dataSet,
	x="BMI",
	y="MedicalCosts_USD",
	hue="BMI_Category",
	ax=ax[1]
	)
scatter1.set(
	yscale="log",
	xlabel="BMI",
	ylabel="Medical Charges in USD",
	title="Log Transformed",
)
plt.suptitle("Scatterplot Medical Charges of American Citizens",y=1)
fig.show()

```

![Plot3](Prabhmeets_images/plot3.png)

```
regplot = sns.regplot(
	data = dataSet,
	x="BMI",
	y="MedicalCosts_USD",
)
regplot.set(
	yscale="log",
	xlabel="BMI ",
	ylabel="Medical Charges in USD",
	title="BMI vs Medical Charges of U.S. Citizens",
)
```


![Plot4](Prabhmeets_images/plot4.png)

## EDA Concolusion

-  It does look like the obese category of , does on average have higher medical expenses. Although it was also found that, 50 percentile of Americans are actually Obese. Therefore this observation will be irrelevant , unless we are able to sample equal number of observations, and explore their mean medical Spending. 

## Research Question

-  Does having a bmi greater than 25 result, in higher medical expenses in America .

From All the above graphs we might , assume that the obese groups have higher medical bills than other groups. Although this might be biased since we have a higher count of Obese people in our population. Therefore we will now try to sample equal observations , from each of out categories.

## Note:

The above plots , and research was sourced from a different file , from my personal analysis file. In that file , the dataset was explored to have outliers, and duplicates. Which were later removed , before being presented in this file.

## Research Conclusion.

-  As per the data explored , having a BMI over 25 in America did not seem to be related with higher medical Expenses. Although it was also found that more than 50% of Americans are either Overweight or Obese as per [CDC guidelines](https://www.cdc.gov/healthyweight/assessing/index.html). Evidence was also found for being Obese or overweight and having higher Medical charges. This relation might just be due to the fact since, a good percentile of Americans are unhealthy in terms or their BMI, they also happened to be the ones with higher medical Charges. Meaning it might be just due to chance that the ones with higher medical charges also happened to be unhealthy in terms of their weight. To overcome this research barrier on having too many Individual from one group , we would have to randomly sample the dataset, and obtain equal number of subjects from each group , and then explore the mean medical spendings of the groups.
-  A seperate analysis where the Medical Dataset was randomly sampled to have equal number of perople from each Bmi cateegory was also performed. Plots and data from that dataset can be found in my personal EDA file. In that file it was concluded that there was no linear relationship between a higher bmi, and higher Medical charged in American Citizens.

