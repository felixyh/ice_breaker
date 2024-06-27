import os

from langchain.prompts.prompt import PromptTemplate
from langchain_community.llms.ollama import Ollama


information = """
Jen-Hsun "Jensen" Huang (Chinese: 黃仁勳; pinyin: Huáng Rénxūn; Pe̍h-ōe-jī: N̂g Jîn-hun; 
born 17 February 1963[2]) is an American businessman and electrical engineer, 
serving as the president and CEO of Nvidia.[3] He co-founded Nvidia in 1993 at age 30 and in June 2024, 
it became the largest company in the world by market capitalization.[4] As of June 2024, 
Forbes estimated Huang's net worth at $118 billion, making him the 11th richest person in the world.[5]
"""

if __name__ == '__main__':

    summary_template = """ 
    Give the information {information} about a person from I want you to create:
    1. a short summary
    2. two interesting facts about them
    """

    summary_prompt_tempate = PromptTemplate(input_variables=["information"], template=summary_template)
    llm = Ollama(model="llama3")
    chain = summary_prompt_tempate | llm
    res = chain.invoke(input={"information": information})

    print(res)

