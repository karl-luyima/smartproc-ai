from typing import TypedDict, List, Dict, Any, Optional

class ProcurementState(TypedDict, total=False):
    request_id: int
    quotes: List[Dict[str, Any]]
    vendors: List[Dict[str, Any]]

    scores: List[Dict[str, Any]]
    best_vendor: Optional[Dict[str, Any]]

    confidence: float
    reasoning: List[str]
    result: Dict[str, Any]
    flag: str