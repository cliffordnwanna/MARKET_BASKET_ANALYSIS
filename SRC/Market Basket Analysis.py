# -*- coding: utf-8 -*-
"""GOMYCODE CHECKPOINT 25 [Unsupervised Association Rules Checkpoint].ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ve-CIRlqqzJRwXHjVWMwIAKKuv-uT81u

# MARKET BASKET ANALYSIS USING APRIORI ALGORITHMN.

## 1. Project Overview Objective:

The objective of this project is to analyze customer purchase patterns using Market Basket Analysis and the Apriori algorithm. The goal is to uncover association rules that can help a supermarket develop effective marketing strategies, optimize product placement, and increase sales through promotions and bundling.

Dataset: This project utilizes two datasets:

A toy dataset to demonstrate how the Apriori algorithm works.

A more extensive dataset containing historical customer purchase records from a supermarket, sourced from Kaggle. The dataset can be accessed here.(https://drive.google.com/file/d/1GO28zbMfhy6G6COiLDGr90Bk6Ig0hV6K/view)

##2. Apriori Algorithm on the Toy Dataset
"""

# 2.1. Importing Required Libraries

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# 2.2. Creating the Toy Dataset
#The toy dataset consists of small transactions to demonstrate how the Apriori algorithm identifies frequent itemsets and association rules.

# Sample toy dataset
toy_dataset = [
    ['Skirt', 'Sneakers', 'Scarf', 'Pants', 'Hat'],
    ['Sunglasses', 'Skirt', 'Sneakers', 'Pants', 'Hat'],
    ['Dress', 'Sandals', 'Scarf', 'Pants', 'Heels'],
    ['Dress', 'Necklace', 'Earrings', 'Scarf', 'Hat', 'Heels', 'Hat'],
    ['Earrings', 'Skirt', 'Skirt', 'Scarf', 'Shirt', 'Pants']
]

#2.3. Data Preprocessing
# We transform the dataset into a transaction format using TransactionEncoder.

# Convert the dataset into a transaction format
te = TransactionEncoder()
te_ary = te.fit(toy_dataset).transform(toy_dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)

# 2.4. Applying the Apriori Algorithm
# We find frequent itemsets that appear in at least 30% of the transactions.


# Identify frequent itemsets with a minimum support of 0.3
frequent_itemsets = apriori(df, min_support=0.3, use_colnames=True)

# 2.5. Generating Association Rules
# We generate association rules using confidence as the metric, with a threshold of 70%.


# Generate association rules
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)

# Display results
print("Frequent Itemsets:")
print(frequent_itemsets)
print("\nAssociation Rules:")
print(rules)

"""###2.6. Interpretation of Results

Frequent Itemsets:

Most Frequent Items: Pants and Scarf, each with a support of 0.8, indicating they are present in 80% of the transactions.

Common Pairs: Some frequent pairs include (Pants, Scarf) and (Pants, Skirt), each appearing in 60% of transactions.

Association Rules:

Example: The rule (Dress) → (Heels) has a confidence of 1.0, indicating that whenever a purchase includes a dress, it always includes heels.

Lift: A rule like (Pants) → (Skirt) has a lift of 1.25, showing a positive association.

###Business Recommendations:

Product Bundling: Since dresses are always accompanied by heels, consider offering bundles or placing these items together.

Promotions: Create discounts on common pairs like pants and scarves to increase sales volume.

Optimized Product Placement: High-confidence rules such as (Sneakers, Hat) suggest placing these products near each other to encourage cross-selling.

These insights highlight how association rule mining can be used to optimize product placements, marketing campaigns, and bundling strategies in a retail environment.

##3. Apriori Algorithm on Real-World Dataset
"""

#3.1. Importing and Preparing the Dataset

import pandas as pd
import plotly.express as px

# Load the dataset from Google Drive
from google.colab import drive
drive.mount('/content/drive')

# Load the dataset
df = pd.read_csv("/content/drive/MyDrive/Untitled folder/DATASETS/Market_Basket_Optimisation.csv")

#3.2. Visualize Data with Plotly

# Basic visualization to understand the data
fig = px.histogram(df, x='shrimp')
fig.show()

#3.3. Data Preprocessing
#We handle missing values and prepare the dataset for transaction analysis.


# Replace NaN values with 'NA'
df_filled = df.fillna('NA')

# Convert all items in the dataset to strings
transactions = df_filled.applymap(str).values.tolist()

# Transform dataset into transaction format
te_checkpoint = TransactionEncoder()
te_ary_checkpoint = te_checkpoint.fit(transactions).transform(transactions)
df_checkpoint = pd.DataFrame(te_ary_checkpoint, columns=te_checkpoint.columns_)

#3.4. Applying Apriori Algorithm

# Find frequent itemsets with a support threshold of 10%
frequent_itemsets_checkpoint = apriori(df_checkpoint, min_support=0.1, use_colnames=True)

#3.5. Generating Association Rules

# Generate association rules
rules_checkpoint = association_rules(frequent_itemsets_checkpoint, metric="confidence", min_threshold=0.1)

# Display results
print("Frequent Itemsets in Checkpoint Dataset:")
print(frequent_itemsets_checkpoint)
print("\nAssociation Rules in Checkpoint Dataset:")
print(rules_checkpoint)

"""###3.6. Interpretation and Business Recommendations

Frequent Itemsets:
Mineral Water appears in 23.83% of transactions, followed by Eggs (17.97%) and Spaghetti (17.41%).

Presence of 'NA' indicates potential issues with data collection; this should be investigated.

Association Rules:

Confidence & Lift:
 Rules like (Mineral Water → Spaghetti) can help design marketing strategies like bundling and discounts.
Example Rule: Whenever 'NA' is present, there's a 100% chance of finding 'Green Tea' and 'Spaghetti'. This should be investigated further to see if 'NA' represents a product category or an issue with the data.

Business Recommendations:

Address Data Quality: 'NA' appears to be prevalent. Consider cleaning the dataset by addressing missing or incorrect data.

Create Bundles and Offers: Products like Mineral Water, Eggs, and Spaghetti are frequently bought together. Consider promotions that capitalize on these associations.

Further Analysis: Segment data or explore seasonal patterns to refine marketing strategies

##4. Conclusion
This project demonstrates the use of the Apriori algorithm to uncover hidden patterns in supermarket purchase data. By identifying frequently bought items and high-confidence associations, we can make informed recommendations for marketing strategies, product placement, and promotional offers. Addressing data quality issues, especially those involving 'NA' values, would allow for even deeper insights and more effective strategies.

Key Takeaways:
The Apriori algorithm is an effective tool for Market Basket Analysis.
Frequent itemsets and association rules provide insights into customer purchase behavior.
Business recommendations can drive strategic marketing and sales improvements.

Next Steps: Future analysis could include deeper segmentation, time-series analysis to understand buying patterns across different seasons, or advanced algorithms for better recommendation systems.
"""

