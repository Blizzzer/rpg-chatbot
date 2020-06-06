import random
import pickle
from configparser import SafeConfigParser
from typing import List

from conversationgraph import ConversationGraph
from model import Corpus
from neuralnetwork import NeuralNetwork
from preprocessing import Preprocessor


def main(neurons_list: List[int], threshold: float, inputs=None, expectedResults=None):
    config = SafeConfigParser()
    config.read("config.ini")

    conversation_graph = ConversationGraph(config.get("main", "path_to_cg_json"))
    lemmatizer = Preprocessor(conversation_graph.corpuses)
    neural_network = NeuralNetwork(neurons_list, conversation_graph, threshold)

    entries = prepare_nn_entries(lemmatizer)
    patterns = prepare_nn_patterns(lemmatizer)

    neural_network.train(entries, patterns)

    print(config.get("strings", "welcome_message"))
    if inputs is None:

        while True:
            user_input = input(config.get("strings", "player_tag") + ": ")
            print(response(config, lemmatizer, neural_network, conversation_graph, user_input))
    else:
        file = open("outputs.txt", "a")
        file.write("Outputs for threshold: " + threshold.__str__() + ", neurons in layers: " +
                   ','.join([str(s) for s in neurons_list]) + "\n")
        counter = 0
        for i, user_input in enumerate(inputs, 0):
            res = response(config, lemmatizer, neural_network,
                           conversation_graph, user_input)[len(config.get("strings", "npc_tag") + ": "):]
            print(res)
            tag = conversation_graph.get_tag_by_response(res)
            file.write(res + " ----> tag: " + tag)
            file.write("\n")
            if tag in expectedResults[i]:
                counter = counter + 1
        file.write("Accuracy: " + str(counter) + "/" + str(len(inputs)))
        file.write("\n")
        file.close()


def response(config, lemmatizer, neural_network, conversation_graph, user_input):
    input_lemmatize = lemmatizer.lemmatize_expression(user_input)
    matching_tag: str = neural_network.predict(input_lemmatize)

    tag: Corpus = conversation_graph.get_corpus_to_respond(matching_tag)

    conversation_graph.close_corresponding_tags(tag)

    tag.isAchieved = True

    return (config.get("strings", "npc_tag") + ": " + random.choice(tag.responses))


def prepare_nn_entries(lemmatizer: Preprocessor):
    try:
        with open('nn_entries.pickle', 'rb') as handle:
            nn_entries = pickle.load(handle)
    except:
        nn_entries = lemmatizer.prepare_nn_entries()
        with open('nn_entries.pickle', 'wb') as handle:
            pickle.dump(nn_entries, handle, protocol=pickle.HIGHEST_PROTOCOL)
    return nn_entries


def prepare_nn_patterns(lemmatizer: Preprocessor):
    try:
        with open('nn_patterns.pickle', 'rb') as handle:
            nn_patterns = pickle.load(handle)
    except:
        nn_patterns = lemmatizer.lemmatize_all_patterns()
        with open('nn_patterns.pickle', 'wb') as handle:
            pickle.dump(nn_patterns, handle, protocol=pickle.HIGHEST_PROTOCOL)
    return nn_patterns
