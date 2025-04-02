from keybert import KeyBERT
import os
import pandas as pd
from bpe import Encoder

def process_source_code_key():
    try:
        with open('dataset/sourcecode_corpous.txt', 'a') as fw:
            df = pd.read_csv('dataset/spacy_and_data/android/df_android_detail_patch_word.csv')
            content_a = df['patch_word_a'].str
            content_b = df['patch_word_b'].str
            content_ab = df['patch_word_ab'].str
            # for item in content_b:
            #     print(item)
            fw.write(str(content_ab))



    except Exception as e:
        print(e)



def training_key():

    doc = """
             Supervised learning is the machine learning task of learning a function that
             maps an input to an output based on example input-output pairs. It infers a
             function from labeled training data consisting of a set of training examples.
             In supervised learning, each example is a pair consisting of an input object
             (typically a vector) and a desired output value (also called the supervisory signal).
             A supervised learning algorithm analyzes the training data and produces an inferred function,
             which can be used for mapping new examples. An optimal scenario will allow for the
             algorithm to correctly determine the class labels for unseen instances. This requires
             the learning algorithm to generalize from the training data to unseen situations in a
             'reasonable' way (see inductive bias).
          """
    kw_model = KeyBERT()
    keywords = kw_model.extract_keywords(doc)
    # key_list = kw_model.extract_keywords(doc, keyphrase_ngram_range=(1, 1), stop_words=None)
    print(keywords)
    with open('dataset/keywords_test.txt','a') as fw:
        fw.write(keywords)



def bpe_training():
    # with open('dataset/keywords.txt') as fr:
    #     key_words = fr.read()
    #
    # test_corpus = key_words
    test_corpus = '''
        Object raspberrypi functools dict kwargs. Gevent raspberrypi functools. Dunder raspberrypi decorator dict didn't lambda zip import pyramid, she lambda iterate?
        Kwargs raspberrypi diversity unit object gevent. Import fall integration decorator unit django yield functools twisted. Dunder integration decorator he she future. Python raspberrypi community pypy. Kwargs integration beautiful test reduce gil python closure. Gevent he integration generator fall test kwargs raise didn't visor he itertools...
        Reduce integration coroutine bdfl he python. Cython didn't integration while beautiful list python didn't nit!
        Object fall diversity 2to3 dunder script. Python fall for: integration exception dict kwargs dunder pycon. Import raspberrypi beautiful test import six web. Future integration mercurial self script web. Return raspberrypi community test she stable.
        Django raspberrypi mercurial unit import yield raspberrypi visual rocksdahouse. Dunder raspberrypi mercurial list reduce class test scipy helmet zip?
    '''

    encoder = Encoder(200, pct_bpe=0.88)  # params chosen for demonstration purposes
    encoder.fit(test_corpus.split('\n'))

    example = "Vizzini: He didn't fall? INCONCEIVABLE!"
    print(encoder.tokenize(example))



if __name__ == '__main__':
    # process_source_code_key()
    training_key()
    # bpe_training()