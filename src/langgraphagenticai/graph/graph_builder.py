from langgraph.graph import StateGraph
from src.langgraphagenticai.state import State

class GraphBuilder:
    def __init__(self, model):
        self.llm = model
        self.graph_builder=StateGraph(State)