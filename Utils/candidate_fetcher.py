from Candidate_module.DB.mongo import collection

def fetch_candidates_by_ids(user_ids):
    candidates = list(collection.find(
        {"user_id": {"$in": user_ids}},
        {"_id": 0}
    ))

    return candidates