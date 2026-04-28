from datetime import datetime
from Candidate_module.DB.mongo import collection
import uuid
from bson import ObjectId
from Utils.profile_to_text import profile_to_text
from Utils.embedder import generate_embeddings
from Utils.vector_store import store_embedding

def save_profile_node(state):
    profile_data=state.get("profile_data")

    if not profile_data:
        return{
            **state,
            "error":"No profile data to save."
        }

    Required_fields=[
        "skills",
        "total_experience_years",
        "expected_salary_min",
        "expected_salary_max",
        "preferred_locations",
        "preferred_work_type",
        "notice_period_days",
        "career_goals",
        "currency"
    ]

    filled_fields = sum(
        1 for field in Required_fields
        if profile_data.get(field) not in [None, "", []]
    )

    completeness=filled_fields/len(Required_fields)

    if state.get("user_id"):
        collection.update_one(
            {"user_id":state["user_id"]},
            {
                "$set": {
                    **profile_data,
                    "profile_completeness": completeness,
                    "updated_at": datetime.utcnow()
                }
            }
        )
        user_id = state["user_id"]
        message = "Profile updated successfully"

        # return{
        #     **state,
        #     "saved_profile_id":state["profile_id"],
        #     "message":"Profile updated successfully"
        # }
    
    else:
        user_id = state.get("user_id") or str(uuid.uuid4())
        document = {
            "user_id":user_id,  # ✅ FIX
            **profile_data,
            "profile_completeness": completeness,
            "extraced_from": "conversation",
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        }

        result = collection.insert_one(document)
        message = "Profile updated successfully"
        state["user_id"]=user_id


        # return {
        #     **state,
        #     "saved_profile_id": str(result.inserted_id),
        #     "confirmation_message": "Profile created successfully!"
        # }
    text=profile_to_text(profile_data)
    embeddings=generate_embeddings(text)
    store_embedding(user_id,embeddings,text)

    print("Embeddings stored in Chroma Db")

    return {
        **state,
        "user_id": user_id,
        "confirmation_message": message,
        "stage": None,             
        "next_question": None,
        "missing_fields": [],
        "is_complete": True,
    }