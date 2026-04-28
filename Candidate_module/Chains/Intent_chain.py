from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
import os
from dotenv import load_dotenv
from Candidate_module.Schema.IntentOutputSchema import IntentOutputSchema
from Candidate_module.Schema.IntentAgentState import CandidateState


load_dotenv()

llm=ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)

parser=PydanticOutputParser(pydantic_object=IntentOutputSchema)

intent_prompt=ChatPromptTemplate.from_messages(
    [
        ("system",f"""
        You are an intent classifier model,your task is to identify the intent base on the user query
        You should also provide confidence score between 0 and 1 and also provide reason for the classification
         
        Classify the users intent into exactly one of the following:
        - create_profile → user provides profile info
        - update_profile → user updates profile
        - view_profile → user wants to see profile
        - job_search → user wants to find jobs
        - general_query → anything else

        IMPORTANT:
        - "show me jobs", "find jobs", "jobs for me", "fetch jobs", "what jobs suit me"
        → job_search

        
        Do not return anything outside JSON
        """
        ),
        (
            "human","{user_query}"
        )
    ],
    
)

intent_chain=intent_prompt|llm|parser

def classify_intent(user_query:str)->CandidateState:
    return intent_chain.invoke({"user_query": user_query})


if __name__ == "__main__":
    user_query = "I want to create a frontend developer profile"
    result = classify_intent(user_query)
    print(result)


