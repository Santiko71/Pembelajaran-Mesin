# Taufik Nur Santiko


import pandas as pd
import numpy as np

dataset = pd.read_csv('clean_dataset_stem.csv',sep=';')
dataset.shape

dataset_feature = dataset['ProcessedText'].astype(str)
dataset_label = dataset['Sentiment']

# cek distribusi label

import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

# Visualizing the target variable
plt.figure(figsize=(12,8))
sns.displot(dataset_label, label=f'target, skew: {dataset_label.skew():.2f}')
plt.legend(loc='best')
plt.show

dataset_label.value_counts()

# BOW
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(dataset_feature)
X

print(vectorizer.get_feature_names())
print(X.toarray())

vectorizer2 = CountVectorizer(analyzer='word', ngram_range=(2, 2))
X2 = vectorizer2.fit_transform(dataset_feature)
print(X2.toarray())
print(X2)