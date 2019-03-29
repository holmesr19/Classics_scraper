'''
latin_text_visualizer.py
reads lemmata in from a file and creates word embeddings, then flattens
them into 2d with PCA to graph them
bancks holmes
'''
from gensim.models import Word2Vec
from sklearn.decomposition import PCA
from matplotlib import pyplot
from nltk import word_tokenize
import seaborn as sns
sns.set()

def stopwords():
    stopwords = ''
    with open('stopwords.txt', 'r') as file:
        for line in file:
            stopwords += line
    #print(stopwords.split())
    return stopwords.split()

#read lemmata into list of strings
def read_file(path):
    return_str = ''
    with open(path, 'r') as file:
        for line in file:
            return_str += line
    return return_str

#make model using w2v
def w2v(lemmata):
    token_list = []
    tokens = word_tokenize(lemmata)
    #remove outliers
    tokens = [ elem for elem in tokens if elem not in ['p', 'ovidi', 'nasonis', 'epitvlae', 'heroidvm', 'herois', 'pagus', 'classics', 'library', 'fero', 'thos', 'ovid'] and elem not in stopwords()] 
    token_list.append(tokens)
    return Word2Vec(token_list, min_count = len(tokens)/500, window = 15)    #an optional min_count argument is responsible for population control

#flatten with PCA
def make_pca(model):
    X = model[model.wv.vocab]
    pca = PCA(n_components = 2) 
    result = pca.fit_transform(X)
    return result

#make graph
def plot(data, model, pca_result):
    pyplot.scatter(pca_result[:, 0], pca_result[:, 1])
    words = list(model.wv.vocab)
    for i, word in enumerate(words):
        pyplot.annotate(word, xy = (pca_result[i, 0], pca_result[i, 1]))
    


    
        

""" #stitch these all together into 1 function once it works
her_data = read_file('corpora/her_lemmatized.txt')
#print(her_data)
her_model = w2v(her_data)
#print(her_model)
#print(list(her_model.wv.vocab))
her_pca = make_pca(her_model)
plot(her_data, her_model, her_pca) """

def stitch(path):
    word_data = read_file(path)
    word_model = w2v(word_data)
    word_pca = make_pca(word_model)
    plot(word_data, word_model, word_pca)

stitch('corpora/all_lemmatized.txt')
pyplot.show()
stitch('corpora/her_lemmatized.txt')
pyplot.title('heroides v. all, min_count: len/500, window: 10')
#pyplot.gca().legend(('all', 'heroides'))
pyplot.show()

#cross shape is accurate, make sure to use set axes for final graphs