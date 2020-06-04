from typing import List
from model import NeuralNetworkTrainingDTO
from conversationgraph import ConversationGraph
import numpy as np
import tflearn


class NeuralNetwork:

    def __init__(self,
                 neurons_list: List[int],
                 conversation_graph: ConversationGraph) -> None:
        super().__init__()
        self.lemmatized_patterns: List[str] = None
        self.output_enumeration = []
        self.model: tflearn.DNN = None
        self.neurons_list = neurons_list
        self.conversation_graph = conversation_graph

    def predict(self,
                line: str):
        entry = []
        for lemma in self.lemmatized_patterns:
            if lemma in line:
                entry.append(1)
            else:
                entry.append(0)
        entry = np.array(entry)

        res = self.model.predict([entry])
        res_max = np.argmax(res)
        if max(res[0]) < 0.5:
            return "UNKNOWN"
        else:
            return self.output_enumeration[res_max]

    def train(self,
              trainSet: List[NeuralNetworkTrainingDTO],
              inputLemmas: List[str]):
        self.lemmatized_patterns = inputLemmas
        training = []
        outputs = []
        for ts in trainSet:
            for tsl in ts.lemmas:
                entry = []
                for lemma in inputLemmas:
                    if lemma in tsl:
                        entry.append(1)
                    else:
                        entry.append(0)
                training.append(entry)
                outputs.append(ts.tag)

        classes = []
        self.output_enumeration = list(set(outputs))
        for out in outputs:
            output = [0 for _ in range(len(set(outputs)))]
            for i, tag in enumerate(set(outputs)):
                if out == tag:
                    output[i] = 1
                    classes.append(output)
                    continue

        training = np.array(training)
        classes = np.array(classes)

        net = tflearn.input_data(shape=[None, len(training[0])])
        for neurons in self.neurons_list:
            net = tflearn.fully_connected(net, neurons)
        net = tflearn.fully_connected(net, len(classes[0]), activation="softmax")
        net = tflearn.regression(net)

        self.model = tflearn.DNN(net)

        self.model.fit(training, classes, n_epoch=1000, batch_size=8, show_metric=True)
