# Importar bibliotecas:
import numpy as np
import pandas as pd
import sklearn.metrics as m

import os
import tarfile
from six.moves import urllib

# Recuperando o arquivo de coleta
FILE_TO_DOWNLOAD =  "Dados2.csv"
DATA_PATH = "Dados/"
#DOWNLOAD_ROOT = "https://raw.githubusercontent.com/GabrielVantuil/ECT2702-TAI/"
#DATA_URL = DOWNLOAD_ROOT + DATA_PATH + FILE_TO_DOWNLOAD
#def fetch_data(data_url=DATA_URL, data_path=DATA_PATH, file_to_download=FILE_TO_DOWNLOAD):
#  if not os.path.isdir(data_path):
#    os.makedirs(data_path)
#  urllib.request.urlretrieve(data_url, data_path+file_to_download)  
#fetch_data() 

# Importando dados do arquivo
dataset = pd.read_csv(DATA_PATH+FILE_TO_DOWNLOAD)

X = dataset.iloc[:,:3].values
y = dataset.iloc[:,3].values

# Dividindo o banco de dados entre treinamento e teste
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Fitting SVM to the Training set
from sklearn.svm import SVC
classifier = SVC(decision_function_shape='ovo')

classifier.fit(X_train, y_train)

C_2d_range = np.logspace(-2,10,30)

gamma_2d_range = np.logspace(-9,3,30)

print(C_2d_range)
classifiers = []


for C in C_2d_range:
    for gamma in gamma_2d_range:
      
        classifier = SVC(C=C, gamma=gamma)
        classifier.fit(X_train, y_train)
        
        y_pred = classifier.predict(X_test)
        
        error = m.mean_squared_error(y_pred,y_test)
        
        
        classifiers.append((C, gamma, error,y_pred, classifier))        
       
print(len(classifiers))



classifiers.sort(key = lambda x:x[2], reverse = False)
print(classifiers[0][3])
clf = classifiers[0][4]

# Salvar classificadores em um arquivo
from sklearn.externals import joblib
joblib.dump(clf, 'Dados/treinamento2.pkl') 
# Carregar classificadores do arquivo
classif = joblib.load('Dados/treinamento2.pkl')

# Predicting the Test set results
# y_pred = classifiers[0][3]
y_pred = classif.predict(X_test)
print(X_test)

print(y_test[0:35])
print(y_pred[0:35])

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

print(cm)

# Visualising the Training set results
#from matplotlib.colors import ListedColormap
#import matplotlib.pyplot as plt
#X_set, y_set = X_train, y_train
#X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
#                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
#plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
#                     alpha = 0.75, cmap = ListedColormap(('blue', 'green')))
#plt.xlim(X1.min(), X1.max())
#plt.ylim(X2.min(), X2.max())
#for i, j in enumerate(np.unique(y_set)):
#    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
#                c = ListedColormap(('red', 'green'))(i), label = j)
#plt.title('SVM (Training set)')
#plt.xlabel('Age')
#plt.ylabel('Estimated Salary')
#plt.legend()
#plt.show()
