import os
from dotenv import load_dotenv

load_dotenv()

from langchain_community.llms.ollama import Ollama
from langchain.prompts.prompt import PromptTemplate
from langchain_core.tools import Tool

# AgentExecutor is the runtime of agent
from langchain.agents import create_react_agent, AgentExecutor

# simplest way to download the pre-made prompt from the community
from langchain import hub



def lookup(name: str) -> str:
    return "https://www.linkedin.com/in/felix-yang-a61abb135/"
