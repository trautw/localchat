# FROM https://github.com/mattesmattes/pca/blob/main/pca.py
# Personal Chat Appliance

from gpt_index import SimpleDirectoryReader, GPTSimpleVectorIndex


def construct_index(directory_path):
    documents = SimpleDirectoryReader('docs').load_data()
    GPTSimpleVectorIndex.from_documents(documents).save_to_disk('data/index.json')

construct_index("docs")
