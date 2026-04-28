from Utils.job_to_text import job_to_text
from Utils.embedder import generate_embeddings
from Utils.candidate_fetcher import fetch_candidates_by_ids
from Utils.candidate_matcher import find_matching_candidates

def candidate_matching_node(state):
    job_data=state.get("job_data")

    if not job_data:
        return{
            **state,
            "response":"Please provide job details first"
        }
    
    text=job_to_text(job_data)
    embedding=generate_embeddings(text)
    results=find_matching_candidates(embedding)

    user_ids=results.get("ids",[])

    if not user_ids:
        return {
            **state,
            "response": "No matching candidates found."
        }
    
    candidates=fetch_candidates_by_ids(user_ids)

    response="Top matching candidates:\n\n"

    for i, candidate in enumerate(candidates, 1):
        response += (
            f"{i}️⃣ Candidate ID: {candidate.get('user_id')}\n"
            f"💡 Skills: {', '.join(candidate.get('skills', []))}\n"
            f"📍 Location: {', '.join(candidate.get('preferred_locations', []))}\n"
            f"💼 Experience: {candidate.get('total_experience_years')} years\n\n"
            "--------------------------------------------------\n\n"
        )
    
    return {
        **state,
        "matched_candidates": candidates,
        "response": response
    }