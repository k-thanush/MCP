from Candidate_module.DB.mongo import collection

def load_profile(state):
    user_id=state.get("user_id")
    profile=collection.find_one({"user_id":user_id})

    if not profile:
        return{
            **state,
            "error":"user not found"
        }
    
    profile_data = {
        k: v for k, v in profile.items()
        if k not in ["_id", "user_id", "created_at", "updated_at"]
    }

    print("Loaded Profile:",profile_data)

    return{
        **state,
        "profile_data":profile_data,
        "profile_id":str(profile["_id"])
    }

    