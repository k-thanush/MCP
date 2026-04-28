from typing import TypedDict, Optional, List, Dict, Any, Annotated


class RecruiterState(TypedDict):
    user_query: str
    user_id: str
    job_id: Optional[str]

    intent: str
    confidence: float
    reason: str

    job_data: Annotated[dict, "persist"]
    extracted_job: dict

    missing_fields: List[str]
    next_question: Optional[str]

    is_complete: Optional[bool]
    stage: Optional[str]
    error: Optional[str]

    response: str