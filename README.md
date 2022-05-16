# The final project!

Created during Professor Bowen's FIN377 Class at Lehigh University

# Research Proposal: Recession Indication For The College Student 

### *By: Anders Seline, Mollie Maggiacomo, and Andrew Zhang*

## Research Question

Our group intends to create a means of predicting if the economy as a whole shows signs of approaching a recessionary period by observing the values of a chosen set of factors. These include well-known recession indicators widely used by economists, as well as other data points near and dear to almost every college student. For starters, the usual metrics of an oncoming downturn we will consider are as follows:

- Consumer Confidence Index (CCI)
- 10-Federal Funds Rate Spread
- Normalized GDP 

Furthermore, here is how each of these values is determined:

- The CCI is calculated by gathering the opinions of household consumer’s opinions on both the current and future outlook of the economy (weighted 40% and 60% respectively).
- The 10-FF Spread is the difference between long term bond yields and the federal funds rate. A small difference or even inversion in yields is indicative of investors seeing few attractive investment opportunities, and piling into long term, relatively low risk government bonds. 
- GDP normalized for population and inflation rates measures economic output over time. 

We settled on using these indicators instead of a myriad of others for a few reasons. First and foremost, they are easily measured and interpreted, and are widely reported and available. Common online databases such as FRED have tons of datasets pertaining to tracking these values over long periods of time, perfect for our observations. Second, they are all leading indicators of a recession - meaning that once the CCI dips, the 10-FF curve inverts, or the GDP drops - we may be in for a period of future economic decline. Since we are hoping to predict a recession from these variables, it is important that they show signs of an oncoming recession instead of telling us that one is already underway. As we begin our process of creating such an indicator which utilizes all three of these variables, we hope to uncover which of these shows the strongest evidence of being able to predict a recession. We intend to accomplish this by considering the NBER receissoin indicator, which reports 1 during periods of recession, and 0 otherwise.

That’s all well and good, but as college students, we wanted to add something to the equation that particularly interested us: alcohol, money, and fast food. Lucky for us, each of the variables have been shown in some way or another to be indicative of a recession, for better or for worse. Considering the former, alcohol sales have a tendency to expand during times of economic hardship as people unfortunately feel as though they need something to make these times seem easier. For copper, this material is widely used in construction, a sector which tends to slow during recession and rapidly expand during expansionary periods. By tracking the price for copper, we can assume that this can serve as a proxy for demand. As for fast food, there exists a sort of exchange rate known as the Big Mac Index. This is published by The Economist each year, and attempts to measure the Purchase Power Parity between countries by comparing the relative price of a McDonald’s Big Mac in each. This is able to somewhat accurately determine the over/undervaluation of a certain currency by comparing this quasi-exchange rate to that of the nation’s currencies. Since each country is responsible for sourcing its own goods and labor in order to produce these standardized products, it levels the playing field and “seeks to make exchange-rate theory a bit more digestible”. We can utilize this in predicting a recession since these periods usually cause the value of currency to depreciate. Additionally, it adds another dimension to our factors by including some data on how the economies of other nations are fairing. We will also explore the correlation between these two factors, as well as with the ones listed above. So, by using:

- Consumer Confidence Index (CCI)
- 10-Federal Funds Rate Spread
- Normalized GDP
- Alcohol Sales 
- Copper Price
- Big Mac Index

We will create a model which will determine if the current state of these factors is cause for alarm by analyzing how they correlate with the NBER recession indicator. 

### Hypotheses

- The CCI, 10-FF Yield Spread, GDP, and Copper Price will all have a significant positive correlation
- Alcohol Sales will have a negative correlation with CCI, 10-FF Yield Spread, GDP, and Copper Price
- Defining Big Mac Index as the difference between the actual and implied exchange rate of the USD and a foreign currency (ie. the currency is undervalued if this difference is positive), this factor will have a negative correlation with the CCI, 10-FF Yield Spread, GDP, and Copper Price
- The factors chosen are in fact indicators of a recession, and a model built from them will be able to predict future recessions with reasonable accuracy 

### Success Metrics 

Like other machine learning endeavours, we will ultimately judge our model based on a few statistical measurements. Tentatively, we will consider the precision, accuracy, sensitivity, and false negative rates of our model in order to judge the validity of our predictions. Since we are treating a recession as a binary variable, we must ensure that we are maximizing the number of recessions we correctly predict, minimizing the number that we miss, and ensuring that the overall accuracy and precision of our model is high enough to be trustworthy. Since we are testing both sensitivity and precision, we will also include F-score in our analysis. 

## Necessary Data

First and foremost, we need to acquire quantitative data on each of our recession indicators. Luckily, most of these metrics are well tracked and are widely available, making this step in the process fairly easy. The following links are the datasets for each variable we intend to use:

- [Actual Recession Indicator](https://fred.stlouisfed.org/series/USREC)
- [10yr minus FF Rate Spread](https://fred.stlouisfed.org/series/T10YFF)
- [Normalized US GDP](https://fred.stlouisfed.org/series/USALORSGPNOSTSAM)
- [Consumer Confidence Index](https://fred.stlouisfed.org/series/CSCICP03USM665S)
- [Purchases of Alcoholic Products](https://fred.stlouisfed.org/series/DAOPRC1A027NBEA)
- [Price of Copper](https://fred.stlouisfed.org/series/WPUSI019011)

As of now, we assume our period of observation to be from 1967 to 2021. This will give us plenty of data to train our model on, along with multiple major recessions. However, the Big Mac Index was created in 1986, and cutting off the rest of our data at this point may result in the model not having enough data to be trained over. We will attempt to create a model which ignores this index before 1986, and includes it afterwards. The following list contains what variables we expect our dataframe to track:

- Index
- Date
- Recession Indicator
- CCI 
- 10-FF Yield Spread
- GDP
- Alcohol Sales Volume
- Alcohol Sales Pct. Change
- Copper Price
- Big Mac Index

All of the necessary preliminary datasets will be stored in a common “inputs” folder, and will each be loaded into their own dataframe. From here, a date column will be added if none exists, and the data will be transformed if necessary. Then each of the columns will be added into the master dataframe.

We hope that this approach will ultimately prove successful, and that we are able to successfully create a means of determining if there is enough risk present in the market to warrant worry about an upcoming recession. 
