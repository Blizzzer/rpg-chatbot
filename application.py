from neuralnetwork import NeuralNetwork
from preprocessing import Preprocessor
from conversationgraph import ConversationGraph


class Application(object):

    def __init__(self) -> None:
        super().__init__()
        self.conversation_graph = ConversationGraph()
        self.lemmatizer = Preprocessor(self.conversation_graph.corpuses)
        self.neural_network = NeuralNetwork(8, self.conversation_graph)

    def start(self):
        self.train_mode()
        print("Welcome in our rpg chat bot npc !!!")
        while True:
            expression = input("Player: ")
            input_lemmatize = self.lemmatizer.lemmatize_expression(expression)
            self.neural_network.predict(input_lemmatize)

    def train_mode(self):
        self.neural_network.train(
            self.lemmatizer.prepare_nn_entries(),
            self.lemmatizer.lemmatize_all_patterns())


Application().start()
