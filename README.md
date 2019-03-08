### Predict Future Sales - Competition
### Table of Contents

1. [Installation](#installation)
2. [Project Description](#description)
3. [File Descriptions](#files)
4. [Results](#results)
5. [Licensing, Authors, and Acknowledgements](#licensing)

## Installation <a name="installation"></a>

I used Anaconda Package with Python version 3.7 to create this notebook with the following libraries Pandas, NumPy, Matplotlib, Scikit-Learn. Addidtionaly, the notebook requires NLTK library. 
run: conda install nltk 

## Project Description<a name="description"></a>

This notebook serves as final project for the "How to win a data science competition" Coursera course. This challenge is also posted on [kaggle.com](https://www.kaggle.com/c/competitive-data-science-predict-future-sales).
In this competition I worked with a challenging time-series dataset consisting of daily sales data, kindly provided by the largest Russian software firms - 1C Company. The goal is to predict total sales for every product and store in the next month. The list of shops and products slightly changes every month. Creating a robust model that can handle such situations is part of the challenge.

## File Descriptions <a name="files"></a>
The following files were provided for analysis:
data/sales_train.csv - the training set. Daily historical data from January 2013 to October 2015. 
data/test.csv - the test set. I need to forecast the sales for these shops and products for November 2015. 
data/sample_submission.csv - a sample submission file in the correct format. 
data/items.csv - supplemental information about the items/products. 
data/item_categories.csv - supplemental information about the items categories. 
data/shops.csv- supplemental information about the shops.

Data fields: 
ID - an Id that represents a (Shop, Item) tuple within the test set
shop_id - unique identifier of a shop 
item_id - unique identifier of a product 
item_category_id - unique identifier of item category 
item_cnt_day - number of products sold. This is a target field that needs to be predicted for a monthly period of time
item_price - current price of an item date - date in format dd/mm/yyyy 
date_block_num - a consecutive month number, used for convenience. January 2013 is 0, February 2013 is 1,..., October 2015 is 33 
item_name - name of item 
shop_name - name of shop 
item_category_name - name of item category

helper.py - the python module with helper functions
future_sales - python notebook that includes exploratory analysis, feature engineering, model selection and evaluation


## Results<a name="results"></a>

...

## Licensing, Authors, Acknowledgements<a name="licensing"></a>

...
