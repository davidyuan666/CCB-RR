import nltk
from nltk.corpus import stopwords
import word_embedding as wm
import string
# nltk.download('stopwords')


#https://maartengr.github.io/KeyBERT/guides/embeddings.html#flair


def preprocessing(corpus):
    # stop_words = set(stopwords.words('english'))
    stop_words = []
    training_data = []
    sentences = corpus.split(".")
    for i in range(len(sentences)):
        sentences[i] = sentences[i].strip()
        sentence = sentences[i].split()
        x = [word.strip(string.punctuation) for word in sentence
             if word not in stop_words]
        x = [word.lower() for word in x]
        training_data.append(x)
    return training_data


def prepare_data_for_training(sentences, w2v):
    data = {}
    for sentence in sentences:
        for word in sentence:
            if word not in data:
                data[word] = 1
            else:
                data[word] += 1
    V = len(data)
    data = sorted(list(data.keys()))
    vocab = {}
    for i in range(len(data)):
        vocab[data[i]] = i

    # for i in range(len(words)):
    for sentence in sentences:
        for i in range(len(sentence)):
            center_word = [0 for x in range(V)]
            center_word[vocab[sentence[i]]] = 1
            context = [0 for x in range(V)]

            for j in range(i - w2v.window_size, i + w2v.window_size):
                if i != j and j >= 0 and j < len(sentence):
                    context[vocab[sentence[j]]] += 1
            w2v.X_train.append(center_word)
            w2v.y_train.append(context)
    w2v.initialize(V, data)

    return w2v.X_train, w2v.y_train



if __name__ == '__main__':
    corpus = ""
    print('start loading corpous....')
    with open('dataset/filepath_corpous.txt') as fr:
        lines = fr.readlines()
        for line in lines:
            corpus += line.strip()

    # corpus += "The earth revolves around the sun. The moon revolves around the earth"
    epochs = 1000

    print('start preprocessing....')
    training_data = preprocessing(corpus)
    w2v = wm.word2vec()

    print('start training....')
    prepare_data_for_training(training_data, w2v)
    w2v.train(epochs)

    print(w2v.predict("around", 3))