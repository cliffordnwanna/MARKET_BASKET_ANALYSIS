

# Market Basket Analysis Using the Apriori Algorithm

## 📋 Project Overview

This project leverages **Market Basket Analysis** to understand customer purchase behavior using the **Apriori Algorithm**. By identifying frequent itemsets and association rules from transaction data, we aim to provide insights that can help supermarkets optimize product placement, design promotional offers, and ultimately enhance sales strategies. 

## 🎯 Objective

The primary objective of this project is to analyze purchase patterns and discover associations between products. By applying the Apriori algorithm, we can identify frequently purchased items together, providing insights for:
- **Product bundling**
- **Optimized store layout**
- **Targeted marketing promotions**

## 📂 Dataset

1. **Toy Dataset**: A small dataset used to illustrate how the Apriori algorithm works.
2. **Real-World Dataset**: A more extensive dataset containing historical purchase records from a supermarket. The dataset was sourced from [Kaggle](https://www.kaggle.com) and can be accessed [here](#).

## 🛠️ Technologies & Tools

- **Programming Language**: Python
- **Libraries**: `pandas`, `mlxtend`, `plotly`
- **Algorithm**: Apriori Algorithm for association rule mining

## 🧑‍💻 Project Workflow

### 1. Apriori Algorithm on the Toy Dataset

#### 1.1 Importing Required Libraries
```python
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
```

#### 1.2 Creating the Toy Dataset
- A small, sample dataset is used to demonstrate the application of the Apriori algorithm.

```python
toy_dataset = [
    ['Skirt', 'Sneakers', 'Scarf', 'Pants', 'Hat'],
    ['Sunglasses', 'Skirt', 'Sneakers', 'Pants', 'Hat'],
    ['Dress', 'Sandals', 'Scarf', 'Pants', 'Heels'],
    ['Dress', 'Necklace', 'Earrings', 'Scarf', 'Hat', 'Heels', 'Hat'],
    ['Earrings', 'Skirt', 'Skirt', 'Scarf', 'Shirt', 'Pants']
]
```

#### 1.3 Data Preprocessing
- The dataset is transformed into a transaction format using `TransactionEncoder`.

#### 1.4 Applying the Apriori Algorithm
- Identify frequent itemsets with a minimum support of 0.3.

#### 1.5 Generating Association Rules
- Rules are generated using confidence as the metric with a threshold of 70%.

#### 1.6 Interpretation of Results
- **Frequent Itemsets**: Commonly purchased items, such as Pants and Scarf (80% support).
- **Association Rules**: For example, `(Dress) → (Heels)` with 100% confidence suggests dresses are always purchased with heels.
- **Business Recommendations**: Create bundles, design promotions, and optimize product placement based on association patterns.

### 2. Apriori Algorithm on Real-World Dataset

#### 2.1 Importing and Preparing the Dataset
```python
import pandas as pd
import plotly.express as px

# Load the dataset from Google Drive
from google.colab import drive
drive.mount('/content/drive')

df = pd.read_csv("/content/drive/MyDrive/Untitled folder/DATASETS/Market_Basket_Optimisation.csv")
```

#### 2.2 Visualize Data with Plotly
- Visualizations provide insights into the dataset distribution.

#### 2.3 Data Preprocessing
- Handle missing values by replacing `NaN` and prepare the dataset for transaction analysis.

#### 2.4 Applying Apriori Algorithm
- Find frequent itemsets with a support threshold of 10%.

#### 2.5 Generating Association Rules
- Generate association rules using a confidence threshold of 0.1.

#### 2.6 Interpretation and Business Recommendations
- **Frequent Itemsets**: Products like Mineral Water, Eggs, and Spaghetti were commonly purchased.
- **Association Rules**: For instance, `(Mineral Water → Spaghetti)` can inform promotional bundles.
- **Address Data Quality**: Prevalence of `NA` suggests missing or incomplete data, requiring further investigation.

## 📊 Results & Insights

- **Most Frequent Items**: Pants and Scarf appeared in 80% of transactions in the toy dataset, while Mineral Water was seen in 23.83% of real-world transactions.
- **Example Rule**: `(Dress) → (Heels)` had a 100% confidence, making it a strong candidate for product bundling.
- **Business Recommendations**:
  - **Product Bundling**: Products frequently bought together can be bundled to increase sales.
  - **Optimized Placement**: Place frequently associated products near each other for effective cross-selling.
  - **Promotions**: Discounts and promotions on associated items to encourage purchases.

## 📝 Conclusion

This project demonstrates the effectiveness of the Apriori algorithm for uncovering hidden patterns in supermarket transactions. By understanding which items are frequently purchased together, businesses can make data-driven decisions on product placement, bundling, and marketing strategies. Addressing data quality issues can further enhance the depth of analysis, enabling more precise recommendations.

### 🔑 Key Takeaways
- The **Apriori algorithm** is a powerful tool for **Market Basket Analysis**.
- **Frequent itemsets** and **association rules** reveal customer buying patterns.
- **Business recommendations** can drive strategic marketing and improve sales.

## 📈 Next Steps
- **Address Data Quality**: Improve the quality of the dataset by addressing missing values and `NA` entries.
- **Deeper Segmentation**: Perform customer segmentation to personalize marketing strategies.
- **Time-Series Analysis**: Analyze purchasing patterns over time to uncover seasonal trends.
- **Advanced Algorithms**: Explore more advanced algorithms like **FP-Growth** for faster and scalable analysis.

## 📂 Repository Structure
```plaintext
├── data/                         # Dataset files
├── notebooks/                    # Jupyter notebooks for exploration & modeling
├── src/                          # Source code for data preprocessing & algorithms
├── README.md                     # Project overview and documentation
└── requirements.txt              # List of dependencies
```

## 💡 Getting Started

### Prerequisites
- Python 3.x
- Libraries: `pandas`, `mlxtend`, `plotly`

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/market-basket-analysis-apriori.git
   ```
2. Navigate to the project directory:
   ```bash
   cd market-basket-analysis-apriori
   ```
3. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Project
1. Run the Jupyter notebook to see the analysis on the toy dataset.
2. Use the script to replicate the analysis on the real-world dataset.

## 📧 Contact

For any questions or suggestions, feel free to reach out:
- **Chukwuma Nwanna**
- **Email**: nwannachumaclifford@gmail.com

