from langgraph.graph import StateGraph,END
from Recruiter_module.Schema.recruiter_state import RecruiterState
from Recruiter_module.Nodes.job_extraction_node import job_extraction_node
from Recruiter_module.Nodes.merge_updated_node import merge_updated_node
from Recruiter_module.Nodes.recruiter_intent_node import recruiter_intent_node
from Recruiter_module.Nodes.detect_missing_node import detect_missing_node
from Recruiter_module.Nodes.followup_node import follow_up_node
from Recruiter_module.Nodes.save_job_node import save_job_node
from Recruiter_module.Nodes.view_jobs_node import view_jobs
from Recruiter_module.Nodes.update_job_node import update_job_node
from Recruiter_module.Nodes.delete_job_node import delete_job_node
from Recruiter_module.Nodes.candidate_matching_node import candidate_matching_node

def route_after_missing_detection(state):
    if state.get("is_complete"):
        if state.get("intent") == "Update_job":
            return "update_job_node"
        return "save_job_node"
    else:
        return "follow_up_node"
    

def route_based_on_intent(state):
    intent=state.get("intent")

    if intent=="Create_job":
        return "job_extraction_node"
    elif intent=="Update_job":
        return "update_job_node"
    elif intent=="View_jobs":
        return "view_jobs_node"
    elif intent=="Delete_job":
        return "delete_job_node"
    elif intent == "Search_candidates":
        return "candidate_matching_node"
    else:
        return "general_node" 

def general_node(state):
    return {
        **state,
        "response": "I can help you create, view, update, or delete jobs."
    }

# --- RECRUITER GRAPH CONSTRUCTION ---
# Initialize the State Graph with the Recruiter memory state
builder=StateGraph(RecruiterState)

# Add processing nodes for the recruiter workflow
builder.add_node("intent_detection_node",recruiter_intent_node)
builder.add_node("job_extraction_node",job_extraction_node)
builder.add_node("merge_update_node",merge_updated_node)
builder.add_node("detect_missing_node",detect_missing_node)
builder.add_node("follow_up_node",follow_up_node)
builder.add_node("save_job_node",save_job_node)
builder.add_node("view_jobs_node",view_jobs)
builder.add_node("update_job_node",update_job_node)
builder.add_node("delete_job_node",delete_job_node)
builder.add_node("general_node",general_node)
builder.add_node("candidate_matching_node",candidate_matching_node)

builder.set_entry_point("intent_detection_node")

# --- ROUTING LOGIC ---
# Define which node to run next based on the recruiter's intent
builder.add_conditional_edges(
    "intent_detection_node",
    route_based_on_intent,
    {
        "job_extraction_node": "job_extraction_node",
        "view_jobs_node": "view_jobs_node",
        "delete_job_node": "delete_job_node",
        "general_node":"general_node",
        "update_job_node":"update_job_node",
        "candidate_matching_node":"candidate_matching_node"
    }
)
builder.add_edge("job_extraction_node","merge_update_node")
builder.add_edge("merge_update_node","detect_missing_node")    

# Determine if the job post is complete, or if the AI needs to ask follow-up questions
builder.add_conditional_edges(
    "detect_missing_node",
    route_after_missing_detection,
    {
        "follow_up_node":"follow_up_node",
        "save_job_node":"save_job_node"
    }
)

builder.add_edge("follow_up_node",END)
builder.add_edge("save_job_node",END)
builder.add_edge("view_jobs_node",END)
builder.add_edge("delete_job_node", END)
builder.add_edge("update_job_node",END)
builder.add_edge("general_node",END)
builder.add_edge("candidate_matching_node",END)

recruiter_graph=builder.compile()

if __name__=="__main__":

    state = {
    "user_query": "",
    "user_id": "user_1",
    "job_id": None,

    "intent": "",
    "confidence": 0.0,
    "reason": "",

    "job_data": {},
    "extracted_job": {},

    "missing_fields": [],
    "next_question": None,

    "is_complete": False,
    "stage": None,
    "error": None,

    "response": ""
}


    print("\n--- Recruiter Chat ---\n")

    while True:
        user_input = input("Recruiter: ")

        if user_input.lower() in ["exit", "quit"]:
            break

        state["user_query"] = user_input

        state = recruiter_graph.invoke(state)

        if state.get("next_question"):
            print("\n🤖:", state["next_question"])
        else:
            print("\n🤖:", state.get("response", "Done"))

        print("\nCurrent Job Data:", state["job_data"])
        print("-" * 50)