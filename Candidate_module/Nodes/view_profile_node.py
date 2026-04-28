from Candidate_module.DB.mongo import collection

def view_profile(state):
    user_id=state.get("user_id")
    profile=collection.find_one({"user_id":user_id})

    if not profile:
        return{
            **state,
            "error":"Profile not found,first create your profile"
        }
    
    profile_data = {
        k: v for k, v in profile.items()
        if k not in ["_id", "user_id", "created_at", "updated_at"]
    }

    response=f"""
    👤 Your Profile:

    🛠 Skills: {profile_data.get("skills")}
    📊 Experience: {profile_data.get("total_experience_years")} years
    💰 Salary Expectation: {profile_data.get("expected_salary_min")} - {profile_data.get("expected_salary_max")} {profile_data.get("currency")}
    📍 Preferred Location: {profile_data.get("preferred_locations")}
    🏢 Work Type: {profile_data.get("preferred_work_type")}
    ⏳ Notice Period: {profile_data.get("notice_period_days")} days
    🎯 Career Goals: {profile_data.get("career_goals")}
"""

    return{
        **state,
        "response":response
    }
    