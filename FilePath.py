import csv
import os
import pandas as pd


def process_words():
    try:
        directory = ['android', 'libreoffice', 'openstack', 'qt']
        vocabs = []
        for _directory in directory:
            for root, dirs, files in os.walk(os.path.join("dataset/spacy_and_data", _directory, 'data')):
                for file in files:
                    print(file)
                    df = pd.read_csv('dataset/spacy_and_data/' + _directory + '/data/' + file)
                    file_words = df['file_word_set'].str.split()
                    for word in file_words:
                        if word not in vocabs:
                            vocabs.append(word)

        uni_vocabs = []
        for item in vocabs:
            for word in item:
                if word not in uni_vocabs:
                    uni_vocabs.append(item)

        with open('dataset/filepath_vocabs.txt', 'a') as fw:
            for word in uni_vocabs:
                fw.write(str(word) + '\n')

    except Exception as e:
        print(e)
        pass


def process_reviewers():
    try:
        directory = ['android', 'libreoffice', 'openstack', 'qt']
        vocabs = []
        for _directory in directory:
            for root, dirs, files in os.walk(os.path.join("dataset/spacy_and_data", _directory, 'data')):
                for file in files:
                    print(file)
                    df = pd.read_csv('dataset/spacy_and_data/' + _directory + '/data/' + file)
                    review_id_words = df['review_id'].astype(str).str.split('|')
                    for word in review_id_words:
                        if word not in vocabs:
                            vocabs.append(word)

        uni_vocabs = []
        for item in vocabs:
            for word in item:
                if word not in uni_vocabs:
                    uni_vocabs.append(item)

        with open('dataset/reviewer_vocabs.txt', 'a') as fw:
            for word in uni_vocabs:
                fw.write(str(word) + '\n')

    except Exception as e:
        print(e)
        pass


def process_corpous():
    pd.set_option('display.max_columns', 1000)
    pd.set_option('display.max_rows', 1000)
    pd.set_option('display.max_colwidth', 1000)
    pd.set_option('display.width', 1000)
    try:
        directory = ['android', 'libreoffice', 'openstack', 'qt']
        with open('dataset/filepath_corpous.txt', 'a') as fw:
            for _directory in directory:
                for root, dirs, files in os.walk(os.path.join("dataset/spacy_and_data", _directory, 'data')):
                    for file in files:
                        print(file)
                        df = pd.read_csv('dataset/spacy_and_data/' + _directory + '/data/' + file)
                        content = df['file_word_set'].str
                        fw.write(str(content.strip()) + " ." + '\n')

    except Exception as e:
        print(e)
        pass


if __name__ == '__main__':
    # process_words()
    # process_reviewers()
    process_corpous()
