from Candidate_module.Graph.intent_graph import intent_graph


CREATE_PROFILE_QUERIES = [
    (
        "Create my candidate profile. I have skills in Python, Django, and PostgreSQL with 3 years experience. "
        "I prefer remote jobs in Bangalore, expected salary is 1200000 to 1600000 INR, notice period 30 days, "
        "and my career goal is to become a senior backend engineer."
    ),
    (
        "Create profile for me with React, TypeScript, and Next.js skills, total experience 2.5 years. "
        "Preferred work type is hybrid in Hyderabad, expected salary 900000 to 1200000 INR, notice period 45 days, "
        "career goal is to grow into a frontend architect role."
    ),
    (
        "Please create my profile. Skills are Java, Spring Boot, and Microservices, experience 4 years. "
        "I want onsite roles in Pune, salary expectation 1400000 to 1800000 INR, currency INR, notice period 60 days, "
        "career goal is to lead backend platform projects."
    ),
    (
        "Create candidate profile with skills SQL, Power BI, and Excel, total experience 2 years. "
        "Preferred work type remote, preferred locations Chennai and Remote, expected salary 700000 to 950000 INR, "
        "notice period 30 days, and career goal is to become a data analytics specialist."
    ),
    (
        "Create my profile using skills AWS, Docker, Kubernetes, and Terraform with 5 years experience. "
        "I prefer hybrid jobs in Mumbai, expected salary min 1800000 max 2400000 INR, notice period 60 days, "
        "career goal is to become a cloud solutions architect."
    ),
    (
        "Create a profile for me. Skills include Flutter, Dart, and Firebase, experience is 3 years. "
        "Preferred work type remote, preferred locations Kochi and Remote, expected salary 1000000 to 1400000 INR, "
        "notice period 30 days, career goal is to build scalable mobile products."
    ),
    (
        "Create my profile with skills Node.js, Express, MongoDB, and Redis, total experience 4.5 years. "
        "I prefer onsite jobs in Gurugram, expected salary 1500000 to 2000000 INR, notice period 45 days, "
        "career goal is to move into engineering management."
    ),
    (
        "Create candidate profile: skills are Selenium, Cypress, and API testing with 3 years experience. "
        "Preferred work type hybrid, preferred locations Noida, salary expectation 900000 to 1250000 INR, "
        "notice period 30 days, and career goal is to become a QA automation lead."
    ),
    (
        "Create profile for me with skills C#, .NET Core, and Azure, total experience 6 years. "
        "I prefer remote work in Bengaluru, expected salary 2000000 to 2800000 INR, notice period 60 days, "
        "career goal is to become a principal engineer."
    ),
    (
        "Create my candidate profile. My skills are Go, Kafka, and distributed systems with 5 years experience. "
        "Preferred work type onsite, preferred location Chennai, expected salary 1700000 to 2300000 INR, "
        "notice period 90 days, and career goal is to design high scale backend systems."
    ),
    (
        "Create profile with skills Figma, Adobe XD, and design systems, experience 2.8 years. "
        "Preferred work type remote, preferred locations Delhi and Remote, expected salary 850000 to 1150000 INR, "
        "notice period 30 days, career goal is to become a senior product designer."
    ),
    (
        "Create candidate profile. Skills are Machine Learning, PyTorch, and NLP with 4 years experience. "
        "Preferred work type hybrid in Bangalore, expected salary 1900000 to 2600000 INR, notice period 60 days, "
        "career goal is to become an AI research engineer."
    ),
    (
        "Create my profile with skills Android, Kotlin, and Jetpack Compose, total experience 3.2 years. "
        "Preferred work type onsite, preferred location Hyderabad, expected salary 1100000 to 1500000 INR, "
        "notice period 45 days, career goal is to lead mobile app architecture."
    ),
    (
        "Create profile for me. Skills include Salesforce Apex, LWC, and integrations, experience 4 years. "
        "Preferred work type hybrid in Pune, salary expectation 1400000 to 1900000 INR, notice period 60 days, "
        "career goal is to become a Salesforce technical consultant."
    ),
    (
        "Create my candidate profile with skills network security, SIEM, and incident response with 5 years experience. "
        "Preferred work type onsite in Kolkata, expected salary 1600000 to 2200000 INR, notice period 30 days, "
        "career goal is to become a cybersecurity manager."
    ),
    (
        "Create profile: skills are Rust, systems programming, and Linux internals with 4 years experience. "
        "Preferred work type remote, preferred locations Remote and Bengaluru, expected salary 1800000 to 2500000 INR, "
        "notice period 45 days, career goal is to build performance critical infrastructure."
    ),
    (
        "Create profile for me with skills business analysis, SQL, and stakeholder management, 3 years experience. "
        "Preferred work type hybrid in Ahmedabad, expected salary 950000 to 1300000 INR, notice period 30 days, "
        "career goal is to become a product strategy lead."
    ),
    (
        "Create candidate profile using skills React Native, JavaScript, and REST APIs, total experience 2 years. "
        "Preferred work type remote, preferred locations Jaipur and Remote, expected salary 800000 to 1100000 INR, "
        "notice period 30 days, career goal is to become a cross platform mobile expert."
    ),
    (
        "Create my profile with skills data engineering, Spark, and Airflow, experience 5.5 years. "
        "Preferred work type hybrid in Mumbai, expected salary 2000000 to 2700000 INR, notice period 60 days, "
        "career goal is to become a data platform architect."
    ),
    (
        "Create profile for me with skills technical writing, API documentation, and developer education, 3 years experience. "
        "Preferred work type remote, preferred location Chennai, expected salary 900000 to 1250000 INR, "
        "notice period 30 days, and career goal is to lead developer documentation initiatives."
    ),
]


def build_initial_state() -> dict:
    return {
        "user_query": "",
        "user_id": None,
        "profile_id": None,
        "intent": "",
        "confidence": 0.0,
        "reason": "",
        "profile_data": {},
        "extracted_profile": {},
        "missing_fields": [],
        "next_question": None,
        "selected_profile_id": None,
        "available_profiles": None,
        "is_complete": False,
        "stage": None,
        "error": None,
        "response": "",
    }


def seed_candidate_profiles() -> None:
    for idx, query in enumerate(CREATE_PROFILE_QUERIES, start=1):
        state = build_initial_state()
        state["user_query"] = query
        result = intent_graph.invoke(state)

        print(f"\n--- Seed Candidate Query {idx} ---")
        print(f"Query: {query}")
        print(f"Intent: {result.get('intent')}")
        if result.get("confirmation_message"):
            print(f"Confirmation: {result['confirmation_message']}")
        if result.get("next_question"):
            print(f"Follow-up: {result['next_question']}")
        if result.get("error"):
            print(f"Error: {result['error']}")


if __name__ == "__main__":
    seed_candidate_profiles()
