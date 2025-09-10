import numpy as np #Eisagogi ton aparaititon vivliothikon
import pandas as pd
df = pd.read_csv('heart.csv')
print(df.shape)
print(df.columns)
print(df.dtypes)
df.head() #Emfanizei tis 5 protes seires tou synolou dedomenon
df.isnull().any() #Emfanizei an mia stili exei times "null"
df.info()
df.describe().T #Emfanisi stoixeion opos mesi timi, megisti timi kai apoklisi
#ARXIZEI H OPTIKOPOIHSH DEDOMENON
import matplotlib.pyplot as plt
import seaborn as sns
# Gia kathe stili tou synolou dedomenon, ftiaxnoume ena istogramma to opoio apeikonizei th syxnothta emfanishs mias timhs
fig = plt.figure(figsize = (15,15))
ax = fig.gca()
g = df.hist(ax=ax)
#Elegxos an to synolo dedomenon einai isorrophmeno h oxi
g = sns.countplot(x='target', data=df)
plt.xlabel('Target')
plt.ylabel('Count')
plt.show()
#Sysxetisi metaxy ton timon tou dataset
corr_matrix = df.corr()
top_corr_features = corr_matrix.index
# Plotting the heatmap
plt.figure(figsize=(20,20))
sns.heatmap(data=df[top_corr_features].corr(), annot=True, cmap='RdYlGn')
dataset = pd.get_dummies(df, columns=['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal'])
#Xrhsimopoioume mono autes tis metavlites giati mporoun na paroun mono duo times.
dataset.columns
from sklearn.preprocessing import StandardScaler
standScaler = StandardScaler()
columns_to_scale = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
dataset[columns_to_scale] = standScaler.fit_transform(dataset[columns_to_scale])
dataset.head()
# Splitting the dataset into dependent and independent features
X = dataset.drop('target', axis=1)
y = dataset['target']
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
knn_scores = []
for i in range(1, 21):
  knn_classifier = KNeighborsClassifier(n_neighbors=i)
  cvs_scores = cross_val_score(knn_classifier, X, y, cv=10)
  knn_scores.append(round(cvs_scores.mean(),3))
# Plotting the results of knn_scores
plt.figure(figsize=(20,18))
plt.plot([k for k in range(1, 21)], knn_scores, color = 'red')
for i in range(1,21):
    plt.text(i, knn_scores[i-1], (i, knn_scores[i-1]))
plt.xticks([i for i in range(1, 21)])
plt.xlabel('Number of Neighbors (K)')
plt.ylabel('Scores')
plt.title('Times tou K neighbors taxinomiti gia diafores times tou K')
plt.show()
# Training the knn classifier model with k value as 12
knn_classifier = KNeighborsClassifier(n_neighbors=12)
cvs_scores = cross_val_score(knn_classifier, X, y, cv=10)
print("H akriveia tou taxinomiti KNeighbours me K=12 tha einai: {}%".format(round(cvs_scores.mean(), 4)*100))
from sklearn.tree import DecisionTreeClassifier
decision_scores = []
for i in range(1, 11):
  decision_classifier = DecisionTreeClassifier(max_depth=i)
  cvs_scores = cross_val_score(decision_classifier, X, y, cv=10)
  decision_scores.append(round(cvs_scores.mean(),3))
# Plotting the results of decision_scores
plt.figure(figsize=(20,18))
plt.plot([i for i in range(1, 11)], decision_scores, color = 'red')
for i in range(1,11):
    plt.text(i, decision_scores[i-1], (i, decision_scores[i-1]))
plt.xticks([i for i in range(1, 11)])
plt.xlabel('Vathos tou dendrou apofashs (N)')
plt.ylabel('Scores')
plt.title('Scores tou taxinomiti dendrou apofashs')
plt.show()
decision_classifier = DecisionTreeClassifier(max_depth=3)
cvs_scores = cross_val_score(decision_classifier, X, y, cv=10)
print("Decision Tree Classifier Accuracy with max_depth=3 is: {}%".format(round(cvs_scores.mean(), 4)*100))
# Importing essential libraries
from sklearn.ensemble import RandomForestClassifier
# Finding the best accuracy for random forest algorithm using cross_val_score 
forest_scores = []
for i in range(10, 101, 10):
  forest_classifier = RandomForestClassifier(n_estimators=i)
  cvs_scores = cross_val_score(forest_classifier, X, y, cv=5)
  forest_scores.append(round(cvs_scores.mean(),3))
# Plotting the results of forest_scores
plt.figure(figsize=(20,15))
plt.plot([n for n in range(10, 101, 10)], forest_scores, color = 'red')
for i in range(1,11):
    plt.text(i*10, forest_scores[i-1], (i*10, forest_scores[i-1]))
plt.xticks([i for i in range(10, 101, 10)])
plt.xlabel('Arithmos ektimhton (N)')
plt.ylabel('Scores')
plt.title('Random Forest Classifier scores for different N values')
# Training the random forest classifier model with n value as 90
forest_classifier = RandomForestClassifier(n_estimators=90)
cvs_scores = cross_val_score(forest_classifier, X, y, cv=5)
print("H akriveia tou Random Forest Classifier me ektimites=90 is: {}%".format(round(cvs_scores.mean(), 4)*100))