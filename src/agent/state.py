from typing import TypedDict, List, Dict, Any

class ProcurementState(TypedDict):
    request_id: int
    quotes: List[Dict[str, Any]]
    vendors: List[Dict[str, Any]]

    scores: List[Dict[str, Any]]
    best_vendor: Dict[str, Any]

    reasoning: List[str]