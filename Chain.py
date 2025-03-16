import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()  # ✅ Correct way to load environment variables

class Chain:
    def __init__(self):
        self.llm=ChatGroq(
            model="llama-3.3-70b-versatile",
    temperature=0,
    groq_api_key=os.getenv("Groq_api")
        )
    def extract_job(self,cleaned_text):
        prompt_template = PromptTemplate.from_template("""
        SCRAPED TEXT FROM WEBSITE:
        {pg}
        ### INSTRUCTION:
        The scraped text is from the career's page of a website.
        Your job is to extract the job postings and return them in JSON format containing the 
        following keys: `role`, `experience`, `skill` and `description`.
        Only return the valid JSON.
        ### VALID JSON (NO PREAMBLE):"""
                                              )
        chain_extract=prompt_template|self.llm
        res=chain_extract.invoke(input={'pg':cleaned_text})
        try:
            res=JsonOutputParser().parse(res.content)
        except OutputParserException:
            raise OutputParserException("The job is too big to parse. Please try again with a smaller job.")
        return res if isinstance(res,list) else [res]

    def write_mail(self,job,Links):
        prompt_email=PromptTemplate.from_template(
        """
        ### JOB DESCRIPTION:
        {job_description}
        
        ### INSTRUCTION:
        You are Glenn, a business development executive at xyz. xyz is an AI & Software Consulting company dedicated to facilitating
        the seamless integration of business processes through automated tools. 
        Over our experience, we have empowered numerous enterprises with tailored solutions, fostering scalability, 
        process optimization, cost reduction, and heightened overall efficiency. 
        Your job is to write a cold email to the client regarding the job mentioned above describing the capability of AtliQ 
        in fulfilling their needs.
        Also add the most relevant ones from the following links to showcase xyz's portfolio: {link_list}
        Remember you are Glenn, BDE at xyz. 
        Do not provide a preamble.
        Have formatting and spacing while generating the email.
        ### EMAIL (NO PREAMBLE):
        
        """
)
        chain_ext=prompt_email | self.llm
        respo=chain_ext.invoke({'job_description':str(job),'link_list':Links})
        return respo.content

if __name__ == "__main__":
    print(os.getenv("Groq_api"))  # ✅ Fetch API key properly
