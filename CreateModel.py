from sklearn.feature_extraction.text import TfidfVectorizer
import io
import json
from sklearn.svm import SVC
from sklearn.metrics import roc_auc_score

listFile = ['bad_comment_train.json', 'good_comment_train.json', 'bad_comment_test.json', 'good_comment_test.json']




def loadAll():
    data = []
    for i in range(0, len(listFile)):
        with io.open(listFile[i], 'r', encoding='utf8') as f:
            data_file = json.load(f)
            for j in range(0, len(data_file)):
                data.append(data_file[j]['comment'])
    print(len(data))
    return data



tfidf_vectorizer = TfidfVectorizer(use_idf=True)
tfidf_vectorizer_vectors = tfidf_vectorizer.fit_transform(loadAll())
X_train = tfidf_vectorizer_vectors[0:9000]
# X_test = tfidf_vectorizer_vectors[9000:13000]
index = 4500
y_train = []
for i in range(0, index * 2):
    if(i < index):
        y_train.append(0)
    else:
        y_train.append(1)
# index = 2000
# y_test = []
# for i in range(0, index * 2):
#     if(i < index):
#         y_test.append(0)
#     else:
#         y_test.append(1)

#Train
clf = SVC(probability=True, kernel='rbf')
clf.fit(X_train, y_train)

# #Predict
# predicts = clf.predict(X_test)
# print(len(predicts))
#
# count = 0
# for i in range(0, len(predicts)):
#     if(predicts[i] == y_test[i]):
#         count += 1
# print("Count :", count)
# print("Do chinh xac: ", count/4000)
