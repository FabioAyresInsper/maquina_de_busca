import json
from argparse import ArgumentParser
from collections import defaultdict

from nltk.tokenize import word_tokenize


def create_repo(corpus):
    '''Cria o repositorio.

    Args:
        corpus: dicionario que mapeia um docid para uma string contendo o
                documento completo.

    Returns:
        Um dicionário que mapeia docid para uma lista de tokens.
    '''
    return {docid: word_tokenize(text) for docid, text in corpus.items()}


def create_index(repo):
    '''Indexa os documentos de um corpus.

    Args:
        repo: dicionario que mapeia docid para uma lista de tokens.

    Returns:
        O índice reverso do repositorio: um dicionario que mapeia token para
        lista de docids.
    '''
    index = defaultdict(set)
    for docid, words in repo.items():
        for word in words:
            index[word].add(docid)
    return {word: list(docids) for word, docids in index.items()}


def main():
    parser = ArgumentParser()
    parser.add_argument('corpus',
                        help='Arquivo json com um dicionario docid para texto')
    parser.add_argument('repo_name',
                        help='Raiz do nome do arquivo de repositorio')
    args = parser.parse_args()

    with open(args.corpus, 'r') as file_corpus:
        corpus = json.load(file_corpus)

    repo = create_repo(corpus)
    index = create_index(repo)

    with open(args.repo_name + '_repo.json', 'w') as file_repo:
        json.dump(repo, file_repo, indent=4)

    with open(args.repo_name + '_index.json', 'w') as file_index:
        json.dump(index, file_index, indent=4)


if __name__ == '__main__':
    main()
