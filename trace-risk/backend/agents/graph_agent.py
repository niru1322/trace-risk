# graph_agent.py - Silent (no debug prints)

class GraphAgent:
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.company = ""

    def add_company_director(self, company, director):
        self.company = company
        if company not in self.nodes:
            self.nodes.append(company)
        if director not in self.nodes:
            self.nodes.append(director)
        self.edges.append((company, director))

    def show(self):
        pass
    def visualize(self):
        pass
    def get_missing_info(self):
        return "What are past companies?"