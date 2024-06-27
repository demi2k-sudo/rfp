import os
from utils import get_openai_api_key
from crewai import Agent, Task, Crew
from crewai_tools import PDFSearchTool
from utils import template

os.environ["OPENAI_API_KEY"] = get_openai_api_key()
os.environ["OPENAI_MODEL_NAME"] = 'gpt-3.5-turbo'


senior_agent = Agent(
    role="Senior Manager",
	goal="To make plans for other agent to work on",
	backstory=(
    """
    You are a senior Manager. You have a template and you want to frame a plan that contains all the titles that has to
    be researched by your workers inorder to fill the template. Make sure that you dont miss out on any heading from the 
    template.
    """
	),
	allow_delegation=False,
	verbose=True
)
quality_assurance_agent = Agent(
	role="Quality Assurance Engineer",
	goal="""Checks if the template has the facts from the provided document and prompt if the document doesnt contain everything from the template""",
	backstory=(
    """
     As a QA engineer you ensure that if the document generated by the team is
     formal and has all the informations from the template filled in it
    """
	),
	verbose=True,
	allow_delegation=False
)
markdown_writer_agent = Agent(
    role="Markdown Writer",
    goal="Generate documents that are formatted correctly and effectively using Markdown syntax",
    backstory=(
        """
        As a Markdown writer, you specialize in creating and formatting documents 
        using Markdown syntax, ensuring clarity, consistency, and readability.
        """
    ),
    verbose=True,
	allow_delegation=False
)
researcher_agent = Agent(
    role="Researcher agent",
    goal="To provide valid information about certain topics",
    backstory=(
        """
         As a researcher, you gather and verify information related to specified titles, providing detailed explanations and facts.
        """
    ),
    verbose=True,
	allow_delegation=False
)

def process_file(file_path):
    file_read = PDFSearchTool(pdf=file_path)
    plan = Task(
        description=(
        f"""
            You have a template and you must frame a plan to research all the information to fill it in the given headings in the template
            template : {template}
        """
        ),
        expected_output=(
        """
            A well specified plan with all the headings from the template
            All the headings from the template must be returned
        """
        ),
        agent=senior_agent,
    )
    research = Task(
        description=(
        f"""
        Find facts and research about each element specified in the plan
        Dont leave any information stuff everything together
        even if it is provided it in the content you have to return it
        You can use tools as many times you want 
        use collective keywords when you search information
        Every information should be present 
        You should fill it with the plan 
        You should not say refer to the document or any of that sort
        """
        ),
        expected_output=(
        """
            A detailed report containing the titles and the facts about the elements in the plan
            Every information should be present 
        """
        ),
        tools=[file_read],
        agent=researcher_agent,
    )
    check_task = Task(
        description=(
        f"""
        If some fields are mentioned as not provided try researching again and make sure there really isnt information. You can research as many times as you want
        """
        ),
        expected_output=(
        f"""
            Clear opinion on how to move the work forward
        """
        ),
        agent=researcher_agent,
    )
    markdown_task = Task(
        description=(
        f"""
        Take the facts and write the document in markdown format. The document should contain only the information from the given document
        """
        ),
        expected_output=(
        f"""
            A markdown document with a heading and only one table in the format : {template}
        """
        ),
        agent=markdown_writer_agent,
    )
    QA_task = Task(
        description=(
        f"""
        Ensuring if the document is complete and contain all the information from the template
        """
        ),
        expected_output=(
        f"""
            Quality decision and what needs to be changed if there is a need. Otherwise wave green flag
        """
        ),
        agent=quality_assurance_agent,
    )
    crew = Crew(
        agents=[senior_agent,researcher_agent,markdown_writer_agent,quality_assurance_agent],
        tasks=[plan,research,markdown_task],
        verbose=1,
        memory=True
    )
    result = crew.kickoff()
    return str(result)
    
    