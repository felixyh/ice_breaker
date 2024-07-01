from langchain.prompts.prompt import PromptTemplate
from langchain_community.llms.ollama import Ollama
from third_parties.linkedin import scrape_linkedin_profile

if __name__ == '__main__':

    summary_template = """ 
    Give the linkdedin information {information} about a person from I want you to create:
    1. a short summary
    2. two interesting facts about them
    """

    summary_prompt_tempate = PromptTemplate(input_variables=["information"], template=summary_template)
    llm = Ollama(model="llama3")
    chain = summary_prompt_tempate | llm
    linkdcin_data = scrape_linkedin_profile(linkedin_profile_url="https://www.linkedin.com/in/felix-yang-a61abb135/")
    res = chain.invoke(input={"information": linkdcin_data})

    print(res)

