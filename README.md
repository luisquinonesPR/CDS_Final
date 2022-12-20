# Scalable Library: Flight Price Prediction

#### Authors: Giovanna Chaves, Daniela de los Santos, Margherita Philipp, Luis Quiñones

Computing for Data Science - Final Project

Data Science for Decision Making - Barcelona School of Economics

##

This library contains an end-to-end pipeline that will build a Random Forest model to predict flight prices in India, and evaluate that model it on a set of metrics. The dataset contains information about flight booking options from the website Easemytrip for flight travel between India's top 6 metro cities. For more details, see Appendix below.


## How to use this library

To build the model, you can run the functions of this library considering the following pipeline:
1.  `Load`: reads in the data and stores a copy of it
2.  `Preprocessor`: class that contains two methods: clean (drops nas for specificied columns) and mean_na (fills in mean for missing values for specified columns)
3.  `Features`: three classes that follow the scheme of an abstract parent class:
  - `Standardize`: Standardize features by removing the mean and scaling to unit variance.
  - `Polynomial`: Generate polynomial and interaction features.
  - `One_Hot_Enc`: Encode categorical features as a one-hot numeric array.
4.  `Split`: Splits dataset into train/test
5.  `Model`: Class with methods train and predict. It trains the dataset using RandomForestRegressor and predicts fitted values for the dependent variable.
6.  `Metrics`: Method returns MSE from comparing predictions to test data

## How to contribute to scaling this library

- `Preprocessor`:
Add new methods within `PreProcessor` class, that can modify the attribute .df

- `Features`:
To add new features, you shoud add a new class (such as `Standardize`, `Polynomial` and `One_Hot_Enc`) within the abstract class Transform. It will take as input the dataframe passed to the abstract class, and implement the abstract method <i>transform</i>.

- `Split`
To add other options for crossvalidation other than a train/test split, a new method can be added within the Split class that affects the attribute .df

- `Model`
New models can be added by including new methods that replicate the structure of the train and predict methods that currently work for Random Forest.

- `Metrics`
New metrics can be added within the class `Metrics`, following the same structure than the current present method (mse), using as inputs two arrays: `y_test` and `y_pred`.



## Appendix: About the dataset

The dataset currently contains information about flight booking options from the website Easemytrip for flight travel between India's top 6 metro cities. There are 300261 datapoints and 11 features in the cleaned dataset.

<b>Data source:</b>
https://www.kaggle.com/datasets/shubhambathwal/flight-price-prediction?select=Clean_Dataset.csv

<b>Data collection and methodology</b>
Octoparse scraping tool was used to extract data from the website. Data was collected in two parts: one for economy class tickets and another for business class tickets. A total of 300261 distinct flight booking options was extracted from the site. Data was collected for 50 days, from February 11th to March 31st, 2022.
Data source was secondary data and was collected from Ease my trip website.

<b>Variables</b>
1) Airline: The name of the airline company is stored in the airline column. It is a categorical feature having 6 different airlines.
2) Flight: Flight stores information regarding the plane's flight code. It is a categorical feature.
3) Source City: City from which the flight takes off. It is a categorical feature having 6 unique cities.
4) Departure Time: This is a derived categorical feature obtained created by grouping time periods into bins. It stores information about the departure time and have 6 unique time labels.
5) Stops: A categorical feature with 3 distinct values that stores the number of stops between the source and destination cities.
6) Arrival Time: This is a derived categorical feature created by grouping time intervals into bins. It has six distinct time labels and keeps information about the arrival time.
7) Destination City: City where the flight will land. It is a categorical feature having 6 unique cities.
8) Class: A categorical feature that contains information on seat class; it has two distinct values: Business and Economy.
9) Duration: A continuous feature that displays the overall amount of time it takes to travel between cities in hours.
10) Days Left: This is a derived characteristic that is calculated by subtracting the trip date by the booking date.
11) Price: Target variable stores information of the ticket price.
