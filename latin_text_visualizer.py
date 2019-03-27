'''
latin_text_visualizer.py
reads lemmata in from a file and creates word embeddings, then flattens
them into 2d with PCA to graph them
bancks holmes
'''
from gensim.models import Word2Vec
from sklearn.decomposition import PCA
from matplotlib import pyplot

#read lemmata into list of strings
def read_file(path):
    return_str = ''
    with open(path, 'r') as file:
        for line in file:
            return_str += line
    return return_str.split()

#make model using w2v
def w2v(lemmata):
    return Word2Vec(lemmata)

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
    pyplot.show()
#where to limit to the 100 (or more?) most used words?

#stitch these all together
her_data = read_file('corpora/her_lemmatized.txt')
print(her_data)
her_model = w2v(her_data)
her_pca = make_pca(her_model)
plot(her_data, her_model, her_pca)