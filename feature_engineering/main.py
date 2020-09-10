from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd
from numpy import log1p
from numpy import vstack, array, nan
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import Binarizer
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import FunctionTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.feature_selection import VarianceThreshold
from sklearn.feature_selection import SelectKBest
from minepy import MINE
from scipy.stats import pearsonr
from sklearn.feature_selection import chi2
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

iris = load_iris()

#原始数据
np.savetxt('01-original_data.csv', iris.data, fmt='%.2f', delimiter = ',')

#标准化处理
stand_data = StandardScaler().fit_transform(iris.data)
np.savetxt('02-standard_data.csv',stand_data,fmt='%.2f', delimiter = ',')

#区间缩放处理
minmaxscale_data = MinMaxScaler().fit_transform(iris.data)
np.savetxt('03-minmax_data.csv',minmaxscale_data,fmt='%.2f', delimiter = ',')

#归一化处理
norm_data = Normalizer().fit_transform(iris.data)
np.savetxt('04-norm_data.csv',norm_data,fmt='%.2f', delimiter = ',')

#定量特征二值化处理
binary_data = Binarizer(threshold=0).fit_transform(iris.data)
np.savetxt('05-bin_data.csv',binary_data,fmt='%d', delimiter = ',')

#定性特征哑编码处理
#onehot_data = OneHotEncoder().fit_transform(iris.data.target.reshape((-1,1)))
#np.savetxt('onehot_data.csv',onehot_data,fmt='%d', delimiter = ',')

#缺失值计算
imp = SimpleImputer(missing_values=np.nan,strategy='mean')
nan_data= imp.fit_transform(iris.data)

# 数据变换
# #基于多项式的变换
# polyfeature_data = PolynomialFeatures().fit_transform(iris.data)
#
# 基于单变元函数的数据变换
# functrans_data = FunctionTransformer(log1p).fit_transform(iris.data)
# print(data)

##特征选择
#Filter
#方差选择法，选择方差大于阈值的数据
var_data = VarianceThreshold(threshold=3).fit_transform(iris.data)
print(var_data)

#相关系数法，计算各个特征对目标值的相关系数
SelectKBest(lambda X, Y: array(map(lambda x:pearsonr(x, Y), X.T)).T, k=2).fit_transform(iris.data, iris.target)

#卡方检验
SelectKBest(chi2, k=2).fit_transform(iris.data,iris.target)

#互信息法,结合最大信息系数法来选择
def mic(x,y):
    m = MINE()
    m.compute_score(x,y)
    return (m.mic(),0.5)

#选择k个最好的特征，返回特征选择后的数据
SelectKBest(lambda X, Y: array(map(lambda x:mic(x, Y), X.T)).T, k=2).fit_transform(iris.data, iris.target)

#Wrapper
#递归特征消除法
RFE(estimator=LogisticRegression(), n_features_to_select=2).fit_transform(iris.data, iris.target)

#Embedded
#基于惩罚项的特征选择法

#带L1惩罚项的逻辑回归作为基模型的特征选择
SelectFromModel(LogisticRegression(penalty="l1", C=0.1)).fit_transform(iris.data, iris.target)

#带L1和L2惩罚项的逻辑回归作为基模型的特征选择
SelectFromModel(LR(threshold=0.5, C=0.1)).fit_transform(iris.data, iris.target)

#基于树模型的特征选择法
SelectFromModel(GradientBoostingClassifier()).fit_transform(iris.data, iris.target)

#降维
#主成分分析法，返回降维后的数据
pca_data = PCA(n_components=2).fit_transform(iris.data)

#线性判别分析法，返回降维后的数据
linear_data = LDA(n_components=2).fit_transform(iris.data, iris.target)





