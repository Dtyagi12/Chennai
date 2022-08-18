## Chennai House Price Prdeiction

# Objective:-

Using the historical data of retail sector based on certain criterias like Squarefeet area of property, Area of city where property located, Number of rooms, Category of property like industrial, commercial, Date of construction and Date of sale develop a machine learning model which predict price of property and provide a range of its Sales Price.

# Solution:-

Here dataset is provided from kaggle and original dataset mentioned in train-chennai-sale.csv. After getting dataset we need to perform some tasks as discussed below:-

# 1. Data Cleaning:-

Library Used:- PANDAS

Here using pandas library first we import .csv file in the IDE(Google Colab). Than in cleaning we take care of some important things like null values, spelling error, feature engineering etc. We goes column by column and firstly decide the feature having categorical data or continous data. Than for removing null values in categorical feature I prefer to use mode and in continous feature took mean. 
Now for feature engineering I remove unnecessary columns like PRT_ID, COMMIS(Commission of broker), REG_FEE(Registration fee) and using DATE_BUILD and DATE_SOLD I create Age_of_building which also have impact on SALE_PRICE.

# 2. Data Visualisation:-

Library Used:- Matplotlib, Seaborn, Plotly

Here it gives us visual representation of data and provide information regading effect of feature on the target(SALE_PRICE). From here we got information about using of what encoding and in which way needed to develop a ML model. Like all selected features shows linear trend with respect to target(SALE_PRICE) except BUILD_TYPE, so for linear trend I used label encoding and for non-linear trend I used one-hot encoding.

# 3. Model development:-

Library Used:- sklearn

# 4. Model Deployment:- https://housepricedakshya.herokuapp.com/
