import os
import argparse
import asyncio
from dotenv import load_dotenv
from browser_use import Agent
from langchain_ollama import ChatOllama

load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

async def run_autonomous_application(url: str):
    resume_path = os.path.join(os.path.dirname(__file__), 'clency_resume.txt')
    with open(resume_path, "r") as file:
        my_resume = file.read()

 
    llm = ChatOllama(
        model="qwen3:4b",          
        temperature=0.0,
        num_ctx=32000             
    )
    
    task_instructions = f"""
    Go to this job application page: '{url}'
    Using my resume context below, accurately fill out the form input fields (Name, email, links, text questions).
    Adopt a professional engineering persona. Do NOT click submit. Stop at the review screen.
    ---
    {my_resume}
    """
    
    agent = Agent(
        task=task_instructions, 
        llm=llm,
        max_actions_per_step=1    
    )
    
    history = await agent.run()
    return history.final_result()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True, help="Job posting URL")
    args = parser.parse_args()
    
    asyncio.run(run_autonomous_application(args.url))
