from suggestions import Suggestions


class KnowledgeGraph:
    MAX_DEPTH = 3

    def __init__(self, term):
        self.__term = term.lower()
        self.__nodes = [term]
        self.__edges = []  # (from node), (to node)
        self.__build_graph(term)

    def __build_graph(self, term, depth=0):
        if depth == self.MAX_DEPTH:
            return
        suggestions = Suggestions(term).get_suggestion()
        for suggestion in suggestions:
            if ' vs ' not in suggestion:
                continue
            if suggestion.count(' vs ') > 1:
                continue
            a, b = suggestion.split(' vs ')
            a = a.lower()
            b = b.lower()
            if b not in self.__nodes:
                self.__nodes.append(b)
                edge = (a, b)
                rev_edge = (b, a)
                if edge not in self.__edges and rev_edge not in self.__edges:
                    self.__edges.append(edge)
                self.__build_graph(b, depth=depth + 1)

    @property
    def nodes(self):
        return self.__nodes

    @property
    def edges(self):
        return self.__edges


if __name__ == '__main__':
    graph = KnowledgeGraph('python')
    print(len(graph.nodes))
    print(graph.nodes)
    print(graph.edges)