from Recruiter_module.DB.job_store import collection

def view_jobs(state):
    jobs=list(collection.find({},{"_id":0}))

    if not jobs:
        return{
            **state,
            "response":"No job found"
        }

    response="Your jobs:\n"

    for i,job in enumerate(jobs,1):
        response += f"{i}. {job.get('role')} at {job.get('company_name')} ({job.get('location')})\n"
    
    return{
        **state,
        "response":response
    }