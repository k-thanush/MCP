from typing import TypedDict,Optional,List,Dict,Any,Annotated


class CandidateState(TypedDict):
    user_query:str
    user_id: str 
    profile_id: Optional[str]   
    intent:str
    confidence:float
    reason:str

    profile_data:Annotated[dict, "persist"] 
    extracted_profile:dict
    missing_fields:list[str]
    next_question:Optional[str]

    selected_profile_id: Optional[str]
    available_profiles: Optional[List[Dict[str, Any]]]

    is_complete: Optional[bool]   
    stage: Optional[str]        
    error: Optional[str]
    response:str