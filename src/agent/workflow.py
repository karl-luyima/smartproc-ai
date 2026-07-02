from langgraph.graph import StateGraph, END
from src.agent.state import ProcurementState
from src.agent.nodes import (
    load_data,
    evaluate_vendors,
    generate_reasoning,
    finalize
)

def build_graph():
    graph = StateGraph(ProcurementState)

    graph.add_node("load_data", load_data)
    graph.add_node("evaluate", evaluate_vendors)
    graph.add_node("reason", generate_reasoning)
    graph.add_node("final", finalize)

    graph.set_entry_point("load_data")

    graph.add_edge("load_data", "evaluate")
    graph.add_edge("evaluate", "reason")
    graph.add_edge("reason", "final")
    graph.add_edge("final", END)

    return graph.compile()