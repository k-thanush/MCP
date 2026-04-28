from langgraph.graph import StateGraph,END
from Candidate_module.Chains.Intent_chain import classify_intent
from Candidate_module.Nodes.follow_up_node import follow_up_node
from Candidate_module.Nodes.profile_extraction_node import profile_extraction_node
from Candidate_module.Schema.IntentAgentState import CandidateState
from Candidate_module.Nodes.intent_node import intent_node, route_after_missing, route_based_on_intent,route_after_extraction
from Candidate_module.Nodes.detect_missing_nodes import detect_missing_fields
from Candidate_module.Nodes.save_profile_node import save_profile_node
from Candidate_module.Nodes.load_profile_node import load_profile
from Candidate_module.Nodes.merge_updated_node import merge_update
from Candidate_module.Nodes.view_profile_node import view_profile
from Candidate_module.Nodes.job_matching_node import job_matching_node

# --- GRAPH CONSTRUCTION ---
# Initialize the state machine with the CandidateState memory dictionary
workflow=StateGraph(CandidateState)

# Add all the processing nodes (steps) that the agent can perform
workflow.add_node("intent_node", intent_node)
workflow.set_entry_point("intent_node")
workflow.add_node("extract_profile_node", profile_extraction_node)
workflow.add_node("detect_missing_fields", detect_missing_fields)
workflow.add_node("ask_followup_node", follow_up_node)
workflow.add_node("save_profile_node",save_profile_node)
workflow.add_node("load_profile_node",load_profile)
workflow.add_node("merge_updated_node",merge_update)
workflow.add_node("view_profile_node",view_profile)
workflow.add_node("job_matching_node",job_matching_node)

# --- INTENT ROUTING ---
# Based on what the user wants to do, route them to the appropriate node
workflow.add_conditional_edges(
    "intent_node",
    route_based_on_intent,
    {
        "create_profile":"extract_profile_node",
        "update_profile":"load_profile_node",
        "view_profile":"view_profile_node",
        "job_search":"job_matching_node",
        "general_query": END,
    }
)

workflow.add_edge("load_profile_node","extract_profile_node")
workflow.add_edge("extract_profile_node","merge_updated_node")
workflow.add_edge("merge_updated_node","detect_missing_fields")

# --- DATA COMPLETION ROUTING ---
# Check if the extracted profile has missing required fields
workflow.add_conditional_edges(
    "detect_missing_fields",
    route_after_missing,
    {
        "save_profile":"save_profile_node",
        "ask_followup":"ask_followup_node"
    }
)

workflow.add_edge("save_profile_node",END)
workflow.add_edge("view_profile_node",END)
workflow.add_edge("job_matching_node",END)
# Compile the graph. We set an interrupt at 'ask_followup_node' so the 
# system pauses execution and waits for human input before continuing.
intent_graph=workflow.compile(
     interrupt_after=["ask_followup_node"]
)



# if __name__ == "__main__":

#     png_bytes = intent_graph.get_graph().draw_mermaid_png()

#     with open("intent_graph.png", "wb") as f:
#         f.write(png_bytes)
#     # -----------------------------
#     # Initial Test State
#     # -----------------------------
#     state = {
#         "user_query":"I am experienced in C# for 2 years i would like to work in remote jobs in trichy with salary of 7 to 8lpa and my goal is become an ceo can you create me an profile",
#         "user_id":None,
#         "intent": None,
#         "confidence": None,
#         "reasoning": None,
#         "profile_data": {},
#         "missing_fields": [],
#         "next_question": None,
#         "is_complete": None,
#         "stage": None,
#         "error": None,
#         "saved_profile_id": None,
#         "confirmation_message": None
#     }

#     while True:
#         print("Running Graph...")

#         state = intent_graph.invoke(state)

#         print("\nCurrent State:")
#         print("Profile Data:", state.get("profile_data"))
#         print("Missing Fields:", state.get("missing_fields"))
#         print("Next Question:", state.get("next_question"))
#         print("Is Complete:", state.get("is_complete"))

#         if state.get("is_complete"):
#             print("\nProfile creation complete!")
#             break

#         user_input = input("\nYour response: ")

#         state = {
#             **state,
#             "user_query": user_input
#         }
    
if __name__ == "__main__":

    state = {
        "user_query": "",
        "user_id": None,

        "intent": "",
        "confidence": 0.0,
        "reason": "",

        "profile_data": {},
        "extracted_profile": {},

        "missing_fields": [],
        "next_question": None,

        "is_complete": False,
        "stage": None,
        "error": None,

        "saved_profile_id": None,
        "confirmation_message": None,

        "response": ""
    }

    print("\n--- Candidate Chat ---\n")

    while True:
        user_input = input("Candidate: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Exiting...")
            break

        # Update state
        state["user_query"] = user_input
       
        # Run graph
        # Run the graph with the current state memory
        state = intent_graph.invoke(state)

        # 🔥 Response handling: Print the appropriate AI response
        if state.get("next_question"):
            print("\n🤖:", state["next_question"])

        elif state.get("response"):
            print("\n🤖:", state["response"])

        elif state.get("confirmation_message"):
            print("\n🤖:", state["confirmation_message"])

        else:
            print("\n🤖: Done")

        # Debug info (optional)
        print("\n📊 Profile Data:", state.get("profile_data"))
        print("⚠️ Missing Fields:", state.get("missing_fields"))
        print("-" * 50)