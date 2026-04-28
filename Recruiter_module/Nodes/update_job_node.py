from Recruiter_module.DB.job_store import collection
from Recruiter_module.Chains.job_extraction_chain import extract_job_entities

def update_job_node(state):
    user_query = state.get("user_query")
    extracted = extract_job_entities(user_query)
    extracted_data = extracted.model_dump()
    print("Extracted for update:", extracted_data)

    role = extracted_data.get("role")
    company = extracted_data.get("company_name")

    if not role:
        return {
            **state,
            "response": "Please specify the job role to update."
        }

    query = {"role": role}

    if company:
        query["company_name"] = company

    existing_job = collection.find_one(query)

    if not existing_job:
        return {
            **state,
            "response": f"No job found for role '{role}'."
        }

    updated_fields = {}

    for key, value in extracted_data.items():
        if value not in [None, "", []] and key != "missing_fields":
            updated_fields[key] = value

    if not updated_fields:
        return {
            **state,
            "response": "No valid updates provided."
        }
    
    collection.update_one(
        {"_id": existing_job["_id"]},
        {"$set": updated_fields}
    )

    return {
        **state,
        "response": f"{role} job updated successfully."
    }