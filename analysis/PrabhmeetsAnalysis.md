# Prabhmeet's Analysis:
First we will import pandas, and use it to read the dataset. As well as do some method cleaning, and some data Wrangling. All of that has been Chained together, in the chunk , below for the purpose of ease to read , and debug.
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
# This part processes the data without any method chaining.
dataSet= fun.load_and_process('./../data/processed/Processed_Medical_Data.csv')
dataSet
```
BMI	Smoker	Region	MedicalCosts_USD	Smoker_bin	BMI_Category
0	27.90	yes	southwest	16884.924	1	Overweight
1	33.77	no	southeast	1725.552	0	Obese
2	33.00	no	southeast	4449.462	0	Obese
3	22.70	no	northwest	21984.471	0	Normal
4	28.88	no	northwest	3866.855	0	Overweight
...	...	...	...	...	...	...
1333	30.97	no	northwest	10600.548	0	Obese
1334	31.92	no	northeast	2205.981	0	Obese
1335	36.85	no	southeast	1629.834	0	Obese
1336	25.80	no	southwest	2007.945	0	Overweight
1337	29.07	yes	northwest	29141.360	1	Overweight
1337 rows × 6 columns
Exploratory Research - Task 3
This pandas Filter information, allows us to perform , and review several analytical tests , that might show some correlation. We can go through this , and see if our dataset , needs any more filtering.
- Using this the categorize BMI was improved, as the previous version was leaving the dataset with several nan values.
- Also some duplicate values were observed which were also removed(This change was made in the data processing file).
- Also a decision was made to add a new column of BMI Category to help categorize the BMI's for easier understanding when producing plots.

Now we will explore the dataset Using plots.
```
dataSet = pd.DataFrame(dataSet)
pf(dataSet).to_notebook_iframe()
Summarize dataset:   0%|          | 0/20 [00:00<?, ?it/s]
Generate report structure:   0%|          | 0/1 [00:00<?, ?it/s]
Render HTML:   0%|          | 0/1 [00:00<?, ?it/s]
Pair plots, gives us several plots for all the different variables in out data Set.
-This will allow us to look for relationships in different variables.
```
## Exploratory Research
plot1 = sns.pairplot(dataSet,palette="virdis")

The only thing that could be concluded from this is that , there seems to be some linear relationship between bmi , and the amount of Medical charges.
We will also get some summary statitistics for our dataset.
```
dataSet.describe().round(0).rename({'50%':'Median'}).T
```
count	mean	std	min	25%	Median	75%	max
BMI	1337.0	31.0	6.0	16.0	26.0	30.0	35.0	53.0
MedicalCosts_USD	1337.0	13279.0	12110.0	1122.0	4746.0	9386.0	16658.0	63770.0
Smoker_bin	1337.0	0.0	0.0	0.0	0.0	0.0	0.0	1.0
This will show us some more summary statistics based off different BMI groups.
```
dataSet.groupby('BMI_Category').agg(['mean','std','median','min','max']).round(1).drop(columns={'BMI'})
```
MedicalCosts_USD	Smoker_bin
mean	std	median	min	max	mean	std	median	min	max
BMI_Category										
Normal	10434.5	7512.9	8604.2	1121.9	35069.4	0.2	0.4	0.0	0	1
Obese	15572.0	14553.2	10003.7	1131.5	63770.4	0.2	0.4	0.0	0	1
Overweight	10987.5	8039.5	8659.4	1252.4	38245.6	0.2	0.4	0.0	0	1
Underweight	8657.6	7591.7	6640.5	1621.3	32734.2	0.2	0.4	0.0	0	1
We can also use pandas profiling , to conduct even more statistical analysis on our dataset , which will also help us to look for other errors in our dataset.`
```
from pandas_profiling import ProfileReport as pf

# Your solution for `pandas_profiling`
pf(dataSet).to_notebook_iframe()
Summarize dataset:   0%|          | 0/20 [00:00<?, ?it/s]
Generate report structure:   0%|          | 0/1 [00:00<?, ?it/s]
Render HTML:   0%|          | 0/1 [00:00<?, ?it/s]
Now we will explore some statitistical data about our data Set.
We will Demonstrate the total number of
The following code gives us some statistical data to explore the previous found co-relation even more. And the mean Medical charge in the Obese groups is found to be the highest.
Although the mean difference between Normal and Overweight (Medical Charges) does not seem to be much.
```
moneyStats=dataSet.groupby('BMI_Category')['MedicalCosts_USD'].agg(['mean','std','min', 'median','max']).round(1).T
moneyStats
```
BMI_Category	Normal	Obese	Overweight	Underweight
mean	10434.5	15572.0	10987.5	8657.6
std	7512.9	14553.2	8039.5	7591.7
min	1121.9	1131.5	1252.4	1621.3
median	8604.2	10003.7	8659.4	6640.5
max	35069.4	63770.4	38245.6	32734.2
After reviewing the results from the i-notebook , the data was cleaned accordingly. Duplicate values, and functions were fixed to a more higher decimal values , to give more accurate results.
The following code, may not be much useful but I was curious to see the percentage of US Population that is under the Obese Category.
 - The plots produced below show us that a good chunk of the US population can be categorized as Obese, and that particular group has the highest mean Medical charges.
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
C:\Users\ISHITA GUPTA\miniconda3\lib\site-packages\seaborn\_decorators.py:36: FutureWarning: Pass the following variable as a keyword arg: x. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.
  warnings.warn(
```
[Text(0.5, 0, 'BMI'),
 Text(0.5, 1.0, 'Density of BMI of various American Citizens.')]

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
	ax=ax[1][0],
)
barplot.set(
	xlabel="BMI Category",
	ylabel="Mean Medical Charges in USD",
	title="Barplot",
)
logbarplot = sns.barplot(
	data = dataSet,
	x="BMI_Category",
	y="MedicalCosts_USD",
	order=['Underweight','Normal','Overweight','Obese'],
	ax=ax[1][1],
)
logbarplot.set(
	yscale="log",
	xlabel="BMI Category",
	ylabel="Log Transformed Mean Medical Charges in USD",
	title="Log Transformed Barplot",
)
fig.tight_layout(h_pad=4,w_pad=10)
plt.suptitle("Different plots comapring mean Medical Charges of American Citizens",y=1.05)
fig.show()
C:\Users\ISHITA~1\AppData\Local\Temp/ipykernel_29720/2232357595.py:58: UserWarning: Matplotlib is currently using module://matplotlib_inline.backend_inline, which is a non-GUI backend, so cannot show the figure.
  fig.show()

Since we can also plot numerical data with numerical data (BMI vs Medical charges),
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
C:\Users\ISHITA~1\AppData\Local\Temp/ipykernel_29720/1829644599.py:28: UserWarning: Matplotlib is currently using module://matplotlib_inline.backend_inline, which is a non-GUI backend, so cannot show the figure.
  fig.show()

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
[None,
 Text(0.5, 0, 'BMI '),
 Text(0, 0.5, 'Medical Charges in USD'),
 Text(0.5, 1.0, 'BMI vs Medical Charges of U.S. Citizens')]

EDA Concolusion
It does look like the obese category of , does on average have higher medical expenses. Although it was also found that, 50 percentile of Americans are actually Obese. Therefore this observation will be irrelevant , unless we are able to sample equal number of observations, and explore their mean medical Spending.
Research Question
Does having a bmi greater than 25 result, in higher medical expenses in America .
From All the above graphs we might , assume that the obese groups have higher medical bills than other groups. Although this might be biased since we have a higher count of Obese people in our population. Therefore we will now try to sample equal observations , from each of out categories.
```
randomSample = dataSet.groupby('BMI_Category').sample(n=20)
randomSample
```
BMI	Smoker	Region	MedicalCosts_USD	Smoker_bin	BMI_Category
370	21.09	no	northwest	13415.038	0	Normal
943	22.61	no	northwest	1628.471	0	Normal
37	20.80	no	southwest	2302.300	0	Normal
241	22.14	no	northeast	5354.075	0	Normal
1295	22.00	no	southwest	1964.780	0	Normal
...	...	...	...	...	...	...
128	17.76	yes	northwest	32734.186	1	Underweight
172	15.96	no	northeast	1694.796	0	Underweight
198	18.05	no	northwest	9644.252	0	Underweight
1085	18.30	yes	southwest	19023.260	1	Underweight
1029	17.29	no	northeast	6877.980	0	Underweight
80 rows × 6 columns
Now we will try to get new Summary statistics on randomly sampled data.
```
randomSample.groupby('BMI_Category')['MedicalCosts_USD'].agg(['mean','std','min', 'median','max']).round(1).T
```
BMI_Category	Normal	Obese	Overweight	Underweight
mean	9338.1	19817.1	11691.2	8430.3
std	7617.5	19190.6	6313.3	7715.3
min	1628.5	1135.9	1708.9	1621.3
median	5712.5	9833.5	9897.9	5878.5
max	30166.6	63770.4	26109.3	32734.2
In [ ]:
## The following plots show that The Obese group still has the highest median Medcial Charges , although we do not see a linear trend from underweight to obese. i.e The Overweight did not show evidence of having a higher mean that Normal people, even though Obese people did.
```
fig, ax =plt.subplots(2,2,figsize=(15,10))

boxplot = sns.boxplot(
	data = randomSample,
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
	data = randomSample,
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
	data = randomSample,
	x="BMI_Category",
	y="MedicalCosts_USD",
	order=['Underweight','Normal','Overweight','Obese'],
	ax=ax[1][0],
)
barplot.set(
	xlabel="BMI Category",
	ylabel="Mean Medical Charges in USD",
	title="Barplot",
)
logbarplot = sns.barplot(
	data = randomSample,
	x="BMI_Category",
	y="MedicalCosts_USD",
	order=['Underweight','Normal','Overweight','Obese'],
	ax=ax[1][1],
)
logbarplot.set(
	yscale="log",
	xlabel="BMI Category",
	ylabel="Log Transformed Mean Medical Charges in USD",
	title="Log Transformed Barplot",
)
fig.tight_layout(h_pad=4,w_pad=10)
plt.suptitle("Different plots comapring mean Medical Charges of American Citizens",y=1.05)
fig.show()
C:\Users\ISHITA~1\AppData\Local\Temp/ipykernel_29720/2893148298.py:58: UserWarning: Matplotlib is currently using module://matplotlib_inline.backend_inline, which is a non-GUI backend, so cannot show the figure.
  fig.show()

```
fig, ax =plt.subplots(1,2,figsize=(15,5))
scatter1=sns.scatterplot(
	data=randomSample,
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
	data=randomSample,
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
C:\Users\ISHITA~1\AppData\Local\Temp/ipykernel_29720/989366099.py:28: UserWarning: Matplotlib is currently using module://matplotlib_inline.backend_inline, which is a non-GUI backend, so cannot show the figure.
  fig.show()

Also the scatter plot before failed to show any linear co-relation between bmi and Medical Charges.
Research Conclusion.
As per the data explore , having a BMI over 25 in America did not seem to be related with higher medical Expenses.
Although it was found that more than 50% of Americans can be categorized as Obsese as per CDC guidelines. Although being Obese did seem to be related to higher Medical charges, a linear relationship between BMI and higher medical expenses was not observed.