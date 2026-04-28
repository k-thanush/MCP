from Utils.profile_to_text import profile_to_text
from Utils.embedder import generate_embeddings
from Utils.job_matcher import find_matching_jobs
from Utils.job_fetcher import fetch_jobs_by_ids

def job_matching_node(state):
    profile_data=state.get("profile_data")
    
    if not profile_data:
        return{
            **state,
            "response":"first complete your profile to search jobs related to you.."
        }
    
    text=profile_to_text(profile_data)
    embeddings=generate_embeddings(text)
    results=find_matching_jobs(embeddings)
    job_ids=results.get("ids",[])

    if not job_ids:
        return {
            **state,
            "response": "No matching jobs found."
        }
    
    jobs=fetch_jobs_by_ids(job_ids)

    response="Top matching jobs:\n\n"

    for i,job in enumerate(jobs,1):
        response += (
            f"{i}️⃣ {job.get('role')} at {job.get('company_name')}\n"
            f"📍 Location: {job.get('location')}\n"
            f"💼 Experience: {job.get('experience')}\n"
            f"🔗 Apply: {job.get('apply_link')}\n\n"
            "--------------------------------------------------\n\n"
        )
    
    return {
        **state,
        "matched_jobs": jobs,
        "response": response
    }
