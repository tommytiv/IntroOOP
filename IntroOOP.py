class Node:
    """ base class """

    def __init__(self, name, cost):
        """
        :param name:
        :param cost:
        """
        self.name = name
        self.cost = cost

    def get_expected_cost(self):
        """ abstract method to be overridden in derived classes
        :returns expected cost of this node """
        raise NotImplementedError("This is an abstract method and needs to implemented in  derived classes.")


class ChanceNode(Node):
    def __init__(self, name, cost, future_nodes, probs):
        Node.__init__(self, name, cost)
        self.futureNodes = future_nodes
        self.probs = probs

    def get_expected_cost(self):
        exp_cost = self.cost  # the expected cost of this node including cost of visit
        i = 0  # index to iterate over probabilities
        for node in self.futureNodes:
            exp_cost += self.probs[i] * node.get_expected_cost()
            i += 1
        return exp_cost


class TerminalNode(Node):
    def __init__(self, name, cost):
        Node.__init__(self, name, cost)

    def get_expected_cost(self):
        return self.cost


class DecisionNode(Node):
    def __init__(self, name, cost, future_nodes):
        Node.__init__(self, name, cost)
        self.futureNodes = future_nodes

    def get_expected_cost(self):
        """return the expected cost of associated future nodes"""
        outcomes = dict()  # dictionary to store expected cost of future nodes
        for thisNode in self.futureNodes:
            outcomes[thisNode.name] = thisNode.get_expected_cost()

            return outcomes


# creating terminal nodes
T1 = TerminalNode("T1", cost=10)
T2 = TerminalNode("T2", cost=20)
T3 = TerminalNode("T3", cost=30)
T4 = TerminalNode("T4", cost=40)
T5 = TerminalNode("T5", cost=50)
T6 = TerminalNode("T6", cost=60)

# creating future nodes & chance nodes, note this order works#

C2FutureNodes = [T1, T2, T3]
C2 = ChanceNode("C2", 15, C2FutureNodes, [0.1, 0.2, 0.7])

C1FutureNodes = [C2, T4]
C1 = ChanceNode("C1", 0, C1FutureNodes, [0.5, 0.5])

C3 = ChanceNode("C3", 0, [T5, T6], [0.2, 0.8])

D1 = DecisionNode("D1", 0, [C1, C3])

print(D1.get_expected_cost())
