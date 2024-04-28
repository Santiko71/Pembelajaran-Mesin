# Taufik Nur Santiko

import pandas as pd
import numpy as np

dataset = pd.read_csv('clean_dataset_stem.csv',sep=';')
dataset_feature = dataset['ProcessedText'].astype(str)
dataset.shape
dataset_label = dataset['Sentimen']

import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

# Visualizing the target variable
plt.figure(figsize=(12,8))
sns.displot(dataset_label, label=f'taget, skew : {dataset_label.skew():.2f}')
plt.legend(loc='best')
plt.show()

dataset_label.value_counts()

# TF - IDF

from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(dataset_feature)
print(X)
print(X.shape)
print(vectorizer.get_feature_names())