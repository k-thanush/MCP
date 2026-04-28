from Candidate_module.Chains.Intent_chain import classify_intent
from Candidate_module.Schema.IntentAgentState import CandidateState

def intent_node(state:CandidateState)->CandidateState:
    """
    Analyzes the user's input and assigns an 'intent' (e.g. create_profile, job_search).
    If the state is in 'followup' stage, it bypasses the LLM classification.
    """
    user_query=state["user_query"]

    if state.get("stage") == "followup":
        print("⚠️ Follow-up mode → skipping intent detection")

        return {
            **state,
            "intent": "create_profile"
        }
    
    result=classify_intent(user_query)

    print("Detected intent:", result.intent)
    new_state= {
        **state,
        "intent": result.intent,
        "confidence": result.confidence,
        "reason": result.reason
    }
    if result.intent=="create_profile":
        new_state["stage"]="profile_building"
    
    return new_state

def route_based_on_intent(state: CandidateState) -> str:
    """
    Determines which node to go next based on intent.
    This acts as the main traffic controller for the graph.
    """

    if state.get("stage") == "followup":
        return "create_profile"
    
    intent = state["intent"]

    print("Routing intent:", intent)

    if intent == "create_profile":
        return "create_profile"

    elif intent == "update_profile":
        return "update_profile"

    elif intent == "job_search":
        return "job_search"
    
    elif intent == "resume_upload":
        return "resume_upload" 
    
    elif intent == "view_profile":
        return "view_profile"
    
    elif intent == "delete_profile":
        return "delete_profile"

    else:
        return "general_query"

def route_after_missing(state):
    """
    After checking for missing fields, this routes either to Save (if complete)
    or back to the Human (if missing fields need to be asked).
    """
    if state["intent"]=="update_profile":
        return "save_profile"
    if state["is_complete"]:
        return "save_profile"
    else:
        return "ask_followup"

def route_after_extraction(state):
    if state["intent"] == "update_profile":
        return "merge"

    return "detect"

if __name__=="__main__":
    test_queries = [
        "I need to add my skills"
    ]

    for query in test_queries:
        result = classify_intent(query)

        print("\n---------------------------")
        print("Query:", query)
        print("Intent:", result.intent)
        print("Confidence:", result.confidence)
        print("Reason:", result.reason)