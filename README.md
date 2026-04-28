<div align="center">
  <h1>🚀 MCP: Multi-Agent Conversational Platform</h1>
  <p><i>The Future of AI-Driven Recruitment and Job Hunting</i></p>
</div>

---

## 🌟 The Problem We Are Solving

Traditional job portals are broken. They rely on rigid forms, endless checkboxes, and manual keyword searches. Candidates hate filling out 5-page forms, and recruiters hate digging through static resumes that don't match their job descriptions.

**MCP changes everything.** By leveraging the power of Multi-Agent AI, MCP turns the recruitment process into a **natural conversation**. 

Instead of filling out forms:
- **Candidates** simply chat with our AI to build a profile. The AI knows what to ask and structures your data automatically.
- **Recruiters** just tell the AI what kind of hire they need. The AI creates the job post.
- **The System** mathematically matches the candidate to the job using high-dimensional vector embeddings—ensuring true *skill* matching, not just *keyword* matching.

---

## 🧠 Why We Chose This Tech Stack (The "Why")

MCP isn't just an LLM wrapper. It's a complex **State Machine** built with precision tools to ensure reliability, memory, and speed.

### 1. 🔄 LangGraph & State Machines
* **What it is:** A library for building stateful, multi-actor applications with LLMs.
* **Why we use it:** Normal chatbots forget context or get confused. We use LangGraph to build a **State Machine**. When you chat, your data enters a structured "State". The graph dynamically routes your conversation:
  - Is information missing? *Route to Follow-Up Node to ask you a question.*
  - Is the profile complete? *Route to Save Node.*
  - Want to search? *Route to Matching Node.*
  This ensures the AI never hallucinates a profile and always collects exactly what's needed.

### 2. ⚡ Groq API (Inference)
* **What it is:** The world's fastest AI inference engine.
* **Why we use it:** A conversational agent is useless if you have to wait 10 seconds for a reply. Groq powers our intent classification and entity extraction at lightning speeds, making the chat feel instant and human-like.

### 3. 🧠 NVIDIA AI Endpoints (Embeddings)
* **What it is:** State-of-the-art embedding models (`nvidia/nv-embed-v1`).
* **Why we use it:** When a candidate says "I know React" and a job asks for "Frontend Frameworks", a keyword search fails. NVIDIA's embeddings convert text into high-dimensional vectors that understand **semantic meaning**. It knows React *is* a frontend framework, guaranteeing perfect job-to-candidate matches.

### 4. 🗄️ ChromaDB (Vector Search)
* **What it is:** An open-source AI-native vector database.
* **Why we use it:** To search millions of vectors in milliseconds. Once a candidate asks "Find me a job", ChromaDB compares their profile vector against all job vectors and returns the mathematically closest matches instantly using K-Nearest Neighbors (KNN).

### 5. 🗂️ MongoDB (Persistent Storage)
* **What it is:** A flexible NoSQL database.
* **Why we use it:** While ChromaDB handles the "matching", we need a place to permanently store the actual structured JSON profiles (Name, Email, Salary, Skills). MongoDB allows candidates and recruiters to pause their chat, log out, and return later to update their profiles seamlessly.

---

## 🚀 Project Setup Instructions

### 1. Clone & Navigate
Ensure you are in the project root folder.
```bash
cd MCP
```

### 2. Set Up a Virtual Environment
Keep your dependencies clean by using a virtual environment:

**For Windows:**
```bash
python -m venv .venv_mcp
.venv_mcp\Scripts\activate
```
**For Mac/Linux:**
```bash
python3 -m venv .venv_mcp
source .venv_mcp/bin/activate
```

### 3. Install Dependencies
Install the AI libraries, graph frameworks, and database drivers:
```bash
pip install -r requirements.txt langchain-groq python-dotenv
```

### 4. Configure Environment Variables
Create a `.env` file in the root of the project to securely hold your API keys:
```env
GROQ_API_KEY=your_groq_api_key_here
NVIDIA_API_KEY=your_nvidia_api_key_here
MONGO_URI=your_mongodb_connection_string_here
```

---

## 💻 How to Run the Project

The architecture is split into two independent modules. You can run them in split terminal windows to see both sides in action!

### 👔 The Recruiter Module
Act as a hiring manager. Create jobs, view them, and let the AI hunt for candidates.
```bash
python -m Recruiter_module.Graph.recruiter_graph
```

### 🧑‍💻 The Candidate Module
Act as a job seeker. Chat with the AI to build your profile, update your skills, and let it recommend perfect job matches.
```bash
python -m Candidate_module.Graph.intent_graph
```

### 🗣️ Example Chat Flow
Once started, the AI will prompt you in the terminal. Type naturally:
- **Candidate:** *"I am looking for a remote Python Developer job. I have 3 years of experience in Django."*
- **Bot:** *"Great! What are your salary expectations?"* (LangGraph detected a missing field!)
- **Recruiter:** *"I want to post a new job for a Senior Data Scientist in NY paying $150k."*
- **Candidate:** *"Find me matching jobs."* (Triggers ChromaDB & NVIDIA Embeddings!)

To stop any chat gracefully, simply type `exit` or `quit`.
