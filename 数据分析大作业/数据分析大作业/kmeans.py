# -*- coding: utf-8 -*-  聚类
"""
Created on Sun Dec 23 10:00:30 2018

@author: Administrator
"""

#########################################################################  
#                           第一步 计算TFIDF   实验六
import codecs
from sklearn.feature_extraction.text import TfidfTransformer    
from sklearn.feature_extraction.text import CountVectorizer
import jieba
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

print('计算tfidf：')

# 语料库corpus构建
corpus = [] # 语料库
filepath_men = '.\\ydzhuang_men.csv'
filepath_women = '.\\ydzhuang_women.csv'
# =============================================================================
# def corpusCreate(path):
#     file = open(path,'r')
#     lines = file.readlines()
#     file.close()
#         
#     # 只分词的语料库
#     for line in lines:
#         ziduan = line.split(',')
#         title = ziduan[0]
#         cut_text = jieba.cut(title) # 分词
#         result = " ".join(cut_text)
#         corpus.append(result)
# corpusCreate(filepath_men)
# corpusCreate(filepath_women)
# 
# =============================================================================

# 去停用词的语料库 
jiebaTxt = open('.\\output\\jieba.txt', mode = 'w') # 存储预处理后的文本结果
remove_words = [u'的', u'，',u'和', u'是', u'随着', u'对于', u'对',u'等',u'能',u'都',u'。',u' ',u'、',u'中',u'在',u'了',
                u'通常',u'如果',u'我们',u'005d',u'运动',u'外套'] # 自定义去除词库
def corpusCreate(path):
    file = open(path,'r')  #
    lines = file.readlines()
#    print(lines)   #lines储存的是每个表的每行内容组成的文本，并用",”隔开
    file.close()
    
    for line in lines:
        result = ''
        ziduan = line.split(',')  #把“，”作为文本分词的依据
#        print(ziduan)
        title = ziduan[0]       #取ziduan数组的第一列，即titles
        cut_text = jieba.cut(title) # 分词
        for word in cut_text: # 循环读出每个分词
            if word not in remove_words: # 如果不在去除词库中
                result += word + ' ' # 分词追加到列表
        jiebaTxt.write(result+'\r\n')
        corpus.append(result)  
corpusCreate(filepath_men)
corpusCreate(filepath_women)

jiebaTxt.flush()
jiebaTxt.close()


# TFIDF计算
#将文本中的词语转换为词频矩阵 矩阵元素a[i][j] 表示j词在i类文本下的词频  
vectorizer = CountVectorizer() 
    
#该类会统计每个词语的tf-idf权值  
transformer = TfidfTransformer()  
  
#第一个fit_transform是计算tf-idf 第二个fit_transform是将文本转为词频矩阵  
tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))   #fit拟合
  
#获取词袋模型中的所有词语    
word = vectorizer.get_feature_names() # get_feature_names()可看到所有文本的关键字toarray()可看到词频矩阵的结果

#将tf-idf矩阵抽取出来，元素w[i][j]表示j词在i类文本中的tf-idf权重  
weight = tfidf.toarray()  #toarray转换成数组

resName = ".\\output\\Tfidf_Result.txt" # TFIDF值输出文本
result = codecs.open(resName, 'w', 'utf-8')  #  用codecs提供的open方法来指定打开的文件的语言编码，它会在读 取的时候自动转换为内部unicode
for j in range(len(word)):  
    result.write(word[j] + ' ')  
result.write('\r\n')  #将出现过的的词语输出

#打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词语权重    
for i in range(len(weight)):  
#    print(u"-------这里输出第",i,u"类文本的词语tf-idf权重------")    
    for j in range(len(word)):  
        result.write(str(weight[i][j]) + ' ')  #weight指权重
    result.write('\r\n')  
print('TFIDF计算完成！')
result.close()
'''
'''

########################################################################  
#                               第二步 聚类Kmeans
print('Start Kmeans:')

# =============================================================================
# # 选取最佳聚类数
# SSE = []  # 存放每次结果的误差平方和
# for k in range(1,21):
#     clf = KMeans(n_clusters = k, init='k-means++', max_iter=300, n_init=1)  
#     clf.fit(weight)
# #    estimator = KMeans(n_clusters=k)  # 构造聚类器
# #    estimator.fit(weight)
#     SSE.append(clf.inertia_) # estimator.inertia_获取聚类准则的总和  append() 方法用于在列表末尾添加新的对象。
# X = range(1,21)
# plt.xlabel('k')
# plt.ylabel('SSE')
# plt.plot(X,SSE,'o-')
# plt.savefig('.\\output\\sse.png') # 图表输出到本地
# plt.show()
# =============================================================================

# 以最佳聚类数进行聚类
outputTxt = open('.\\output\\output.txt', 'w')
true_k = 16 # 最佳聚类个数
# 指定分成16个类
clf = KMeans(n_clusters = true_k, init='k-means++', max_iter=400, n_init=1)  #构造聚类器
s = clf.fit(weight)  #进行聚类

outputTxt.write('s：')
outputTxt.write(str(s))
print('s：')  
print(s)

# 输出每个分类头8个特征词进行类别的表示
clusterTxt = open('.\\output\\clusterLabel.txt', mode = 'w') # 存储每个分类的描述标签
order_centroids = clf.cluster_centers_.argsort()[:, ::-1]   #argsort函数返回的是数组值从小到大的索引值
terms = vectorizer.get_feature_names()
for i in range(true_k):  #输出每个分类头8个特征词       聚类的中心print clf.cluster_centers_ 每个样本所属的簇print clf.labels_
    clusterTxt.write('Cluster'+str(i)+':')
    for ind in order_centroids[i, :8]:
        print(' %s' % terms[ind],)
        clusterTxt.write(terms[ind]+' ')
    print ('')
    clusterTxt.write('\r\n')

clusterTxt.flush()
clusterTxt.close()
  
## 打印出各个族的中心点
##print('clf.cluster_centers_：') 
##print(str(clf.cluster_centers_))
outputTxt.write('clf.cluster_centers_：')
outputTxt.write(str(clf.cluster_centers_))
#     
##每个样本所属的簇 
##print('clf.labels_:') 
##print(clf.labels_)
outputTxt.write('clf.labels_：')
outputTxt.write(str(clf.labels_)) 

i = 1
#print('while循环：')
outputTxt.write('while循环：')
while i <= len(clf.labels_):  
#    print(i, clf.labels_[i-1])
    outputTxt.write(str(i)+' '+str(clf.labels_[i-1])) 
    i = i + 1

outputTxt.flush()
outputTxt.close()
# 样本距其最近的聚类中心的平方距离之和，用来评判分类的准确度，值越小越好
# k-means的超参数n_clusters可以通过该值来评估
print("inertia: {}".format(clf.inertia_))  #选择的k的值与它的值相吻合，则聚类效果好（评估聚类器的聚类效果）


########################################################################  
#                               第三步 可视化
print('可视化：')

# 使用T-SNE算法，对权重进行降维，准确度比PCA算法高，但是耗时长,用了将近20分钟运行完
from sklearn.manifold import TSNE    
tsne = TSNE(n_components=2)   #嵌入二维空间，结果以二维数据展示
decomposition_data = tsne.fit_transform(weight)  #先拟合，再标准化

x = []
y = []

for i in decomposition_data:
    x.append(i[0])
    y.append(i[1])
    
#fig = plt.figure(figsize=(20, 20))
ax = plt.axes()
plt.scatter(x, y, c=clf.labels_, marker="x")
plt.xticks(())
plt.yticks(())
plt.savefig('.\\output\\kmeans.png', aspect=1)
plt.show()
