import os
import asyncio
from dotenv import load_dotenv
from browser_use import Agent
from langchain_openai import ChatOpenAI

load_dotenv()

async def main():
    # 1. Load your CV context
    with open("resume.txt", "r") as file:
        my_resume = file.read()

    # 2. Configure the LLM that will look at the web pages and make decisions
    # Vision capabilities are crucial here for identifying fields correctly
    llm = ChatOpenAI(model="gpt-4o", temperature=0.0)

    # 3. Formulate the dynamic task string
    target_job_url = "https://boards.greenhouse.io/examplecompany/jobs/12345"
    
    task_instructions = f"""
    Go to this job application page: '{target_job_url}'.
    
    Your goal is to apply for this job completely on my behalf.
    Here is all my professional data and resume details:
    ---
    {my_resume}
    ---
    
    Guidelines:
    1. Fill in all standard fields: First Name, Last Name, Email, Phone, LinkedIn, GitHub.
    2. Look for an "Upload Resume" button. Click it and look for a local file named 'resume.pdf' to upload if a file input is requested.
    3. If there are text questions (e.g., 'Why do you want to join?'), answer them concisely, adopting a professional, confident, and proactive engineering tone matching my profile.
    4. Crucial Guardrail: Do NOT click the final 'Submit Application' or 'Apply' button yet. Stop at the final review screen and let me know you are done filling it out.
    """

    # 4. Initialize and run the autonomous agent
    agent = Agent(
        task=task_instructions,
        llm=llm
    )

    history = await agent.run()
    
    # 5. Print the execution path for logging/sheets integration
    print("Execution complete!")
    print(history.final_result())

if __name__ == "__main__":
    asyncio.run(main())