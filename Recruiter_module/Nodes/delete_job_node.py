from Recruiter_module.DB.job_store import collection
from Recruiter_module.Chains.job_extraction_chain import extract_job_entities

def delete_job_node(state):
    user_query = state.get("user_query")
    extracted = extract_job_entities(user_query)
    extracted_data = extracted.model_dump()

    print("Extracted for delete:", extracted_data)

    role = extracted_data.get("role")
    company = extracted_data.get("company_name")

    if not role:
        return {
            **state,
            "response": "Please specify the job role to delete."
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

    collection.delete_one({"_id": existing_job["_id"]})

    return {
        **state,
        "response": f"{role} job deleted successfully."
    }
