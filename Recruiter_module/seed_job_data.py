from Recruiter_module.Graph.recruiter_graph import recruiter_graph


CREATE_JOB_POST_QUERIES = [
    (
        "Create job post for Backend Developer at Nimbus Labs in Bangalore. "
        "Need Python, FastAPI, PostgreSQL, and 3+ years experience. "
        "Apply here: https://nimbus.example.com/jobs/backend-dev"
    ),
    (
        "Create job post for Frontend Engineer at PixelForge in Hyderabad. "
        "Skills: React, TypeScript, Redux. Experience: 2-4 years. "
        "Apply link: https://pixelforge.example.com/careers/frontend-engineer"
    ),
    (
        "Create job post for Data Analyst at InsightWave in Pune. "
        "Need SQL, Excel, Power BI with 1-3 years experience. "
        "Apply at https://insightwave.example.com/jobs/data-analyst"
    ),
    (
        "Create job post for DevOps Engineer at CloudArc in Chennai. "
        "Skills required: AWS, Docker, Kubernetes, CI/CD. "
        "Experience: 4+ years. Apply link: https://cloudarc.example.com/jobs/devops"
    ),
    (
        "Create job post for Machine Learning Engineer at NeuralNest in Mumbai. "
        "Need Python, PyTorch, NLP, and 3+ years experience. "
        "Apply here: https://neuralnest.example.com/jobs/ml-engineer"
    ),
    (
        "Create job post for QA Automation Engineer at TestSphere in Noida. "
        "Skills: Selenium, Python, API testing. Experience: 2-5 years. "
        "Apply link: https://testsphere.example.com/careers/qa-automation"
    ),
    (
        "Create job post for Mobile App Developer at AppTrail in Kochi. "
        "Need Flutter, Dart, Firebase with 2+ years experience. "
        "Apply at https://apptrail.example.com/jobs/flutter-dev"
    ),
    (
        "Create job post for Full Stack Developer at CodeHarbor in Gurugram. "
        "Skills required: Node.js, React, MongoDB, and 3-6 years experience. "
        "Apply link: https://codeharbor.example.com/jobs/fullstack"
    ),
    (
        "Create job post for Product Manager at VisionLoop in Bangalore. "
        "Need roadmap planning, analytics, and stakeholder communication with 5+ years experience. "
        "Apply here: https://visionloop.example.com/jobs/product-manager"
    ),
    (
        "Create job post for UI UX Designer at PixelMint in Pune. "
        "Skills: Figma, prototyping, design systems. Experience: 2-4 years. "
        "Apply link: https://pixelmint.example.com/careers/ui-ux-designer"
    ),
    (
        "Create job post for Cybersecurity Analyst at ShieldGrid in Hyderabad. "
        "Need SIEM, incident response, network security, and 3+ years experience. "
        "Apply at https://shieldgrid.example.com/jobs/security-analyst"
    ),
    (
        "Create job post for Data Engineer at StreamForge in Chennai. "
        "Skills required: Spark, Kafka, Airflow, and 4+ years experience. "
        "Apply link: https://streamforge.example.com/jobs/data-engineer"
    ),
    (
        "Create job post for Site Reliability Engineer at UptimeCore in Bangalore. "
        "Need Linux, Kubernetes, monitoring, and 4+ years experience. "
        "Apply here: https://uptimecore.example.com/jobs/sre"
    ),
    (
        "Create job post for Business Analyst at MarketPulse in Delhi. "
        "Skills: SQL, reporting, requirement gathering with 2-5 years experience. "
        "Apply link: https://marketpulse.example.com/jobs/business-analyst"
    ),
    (
        "Create job post for Technical Writer at DocSprint in Remote. "
        "Need API documentation, developer docs, and 2+ years experience. "
        "Apply at https://docsprint.example.com/jobs/technical-writer"
    ),
    (
        "Create job post for Cloud Engineer at SkyRoute in Mumbai. "
        "Skills required: AWS, Terraform, networking with 3+ years experience. "
        "Apply link: https://skyroute.example.com/jobs/cloud-engineer"
    ),
    (
        "Create job post for Salesforce Developer at CRMStack in Pune. "
        "Need Apex, Lightning Web Components, integrations, and 3-5 years experience. "
        "Apply here: https://crmstack.example.com/jobs/salesforce-developer"
    ),
    (
        "Create job post for Blockchain Developer at LedgerFlow in Bengaluru. "
        "Skills: Solidity, smart contracts, Web3 with 2-4 years experience. "
        "Apply link: https://ledgerflow.example.com/jobs/blockchain-dev"
    ),
    (
        "Create job post for Game Developer at PixelRaid in Hyderabad. "
        "Need Unity, C#, gameplay systems with 2+ years experience. "
        "Apply at https://pixelraid.example.com/jobs/game-developer"
    ),
    (
        "Create job post for AI Prompt Engineer at PromptWorks in Remote. "
        "Skills required: prompt design, evaluation, Python with 1-3 years experience. "
        "Apply link: https://promptworks.example.com/jobs/prompt-engineer"
    ),
    (
        "Create job post for ERP Consultant at BizFlow in Ahmedabad. "
        "Need ERP implementation, process mapping, and 4+ years experience. "
        "Apply here: https://bizflow.example.com/jobs/erp-consultant"
    ),
    (
        "Create job post for Network Engineer at NetBridge in Kolkata. "
        "Skills: routing, switching, firewall management with 3+ years experience. "
        "Apply link: https://netbridge.example.com/careers/network-engineer"
    ),
    (
        "Create job post for Support Engineer at HelpOrbit in Jaipur. "
        "Need troubleshooting, ticketing tools, SQL basics with 1-3 years experience. "
        "Apply at https://helporbit.example.com/jobs/support-engineer"
    ),
    (
        "Create job post for HR Tech Specialist at PeopleSync in Chennai. "
        "Skills required: ATS platforms, HR analytics, automation with 3+ years experience. "
        "Apply link: https://peoplesync.example.com/jobs/hr-tech-specialist"
    ),
]


def build_initial_state(user_id: str) -> dict:
    return {
        "user_query": "",
        "user_id": user_id,
        "job_id": None,
        "intent": "",
        "confidence": 0.0,
        "reason": "",
        "job_data": {},
        "extracted_job": {},
        "missing_fields": [],
        "next_question": None,
        "is_complete": False,
        "stage": None,
        "error": None,
        "response": "",
    }


def seed_recruiter_job_data(user_id: str = "seed_user") -> None:
    for idx, query in enumerate(CREATE_JOB_POST_QUERIES, start=1):
        state = build_initial_state(user_id=user_id)
        state["user_query"] = query
        result = recruiter_graph.invoke(state)

        print(f"\n--- Seed Query {idx} ---")
        print(f"Query: {query}")
        print(f"Intent: {result.get('intent')}")
        print(f"Response: {result.get('response')}")
        if result.get("next_question"):
            print(f"Follow-up: {result['next_question']}")
        if result.get("error"):
            print(f"Error: {result['error']}")


if __name__ == "__main__":
    seed_recruiter_job_data()
