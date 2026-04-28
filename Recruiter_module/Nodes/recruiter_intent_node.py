from Recruiter_module.Chains.intent_chain import classify_recruiter_intent
from Recruiter_module.Schema.recruiter_state import RecruiterState

def recruiter_intent_node(state:RecruiterState)->RecruiterState:
    user_input=state["user_query"]

    if state.get("stage") == "followup":
        print("⚠️ Follow-up mode → skipping intent detection")

        return {
            **state,
            "intent": "Create_job"   
        }
    
    intent_result=classify_recruiter_intent(user_input)
    print("Detected intent:", intent_result.intent)

    return{
        **state,
        "intent":intent_result.intent
    }

