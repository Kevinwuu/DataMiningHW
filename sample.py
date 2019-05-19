from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd

# 讀取乳癌資料
data = datasets.load_breast_cancer()

# 將資料集轉成data frame
df = pd.DataFrame(data['data'], columns=data['feature_names'])
print(df.head())

# print(data.keys())

# 使用PCA把維度降低

X = data['data']
y = data['target']
pca = PCA(n_components=2)
# X=pca.inverse_transform(newX) 轉換回原始數據
reduced_X = pca.fit_transform(X)

# 訓練集測試集資料分割 80/20
# X_train, X_test, y_train, y_test = train_test_split(data, y, test_size=0.2)
# print(X_train.shape, y_train.shape)
# print(X_test.shape, y_test.shape)



