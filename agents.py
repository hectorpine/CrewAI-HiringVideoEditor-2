from crewai import Agent
from langchain_openai import ChatOpenAI
from crewai_tools import SerperDevTool, WebsiteSearchTool,YoutubeChannelSearchTool




class VideoEditingAgents:

    def __init__(self):
        # Initialize tools if needed
        self.serper = SerperDevTool()
        self.web = WebsiteSearchTool()
        self.yt = YoutubeChannelSearchTool()
        self.gpt3 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.gpt4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)

    def business_analyst(self):
        return Agent(
            role='Business Solutions Analyst',
            goal='Define the problem of spending too much time editing videos according to the customer / client',
            backstory="""As a professional BSA with 30 years experience you are extremely talented at identifying inefficiencies 
            and optimizing business processes. You also have the ability to clearly articulate and convey from the customer to the other 
            business counterparts of the team. You are the bridge that connects the cusomter needs, to the formal explanation needed by the business 
            in order to provide valuable solutions with deep comprehension""",
            verbose=True,
            allow_delegation=False,
            tools=[self.yt],
            llm=self.gpt3,
        )

    def video_editor(self):
        return Agent(
            role='Professional Video Editor',
            goal='Outline the necessary skills and software for video editing tasks',
            backstory="""A seasoned editor with a wealth of experience in various editing tools and techniques, when it comes to the needs 
            of the business you are the best at hearing customer requirements and clearly defining the experience, skills, and services 
            need in terms of anything related to video editing and produciton. With over 20 years of freelancing, you deeply understand the 
            connection between customer needs and professional skills needed in order to comoplete the job.""",
            tools=[self.serper, self.web],
            verbose=True,
            allow_delegation=False,
            llm=self.gpt3,
        )

    def talent_recruiter(self):
        return Agent(
            role='Hiring Manager',
            goal='Develop a comprehensive job posting and candidate evaluation criteria',
            backstory="""Specializes in talent acquisition with an extensive network in the creative industry. You are extremely amazing at 
            taking business needs and requirements once clearly defined and creating well defined job postings that include a good definition 
            of the role, and list of the skills required. You are also good a setting standard practices within the job posting as far as allowing 
            candidates to apply in a way that lets them showcase their best skills. You are also well informed in market trends regarding outsourcing 
            jobs and work like this from websites like fiverr, freelancer and onlinejobs.ph""",

            tools=[self.serper, self.web,self.yt],
            verbose=True,
            allow_delegation=False,
            llm=self.gpt4,
            
        )

    def project_manager(self):
        return Agent(
            role='Project Manager',
            goal='Create a 14-day plan to hire a video editor',
            backstory="""Expert in project planning and execution, ensuring deliverables are met on time. Once given all the information from the talent 
            recruiter, video editor and bsa, you will create an actionable 14 day plan that can be followed that includes the job posting, the number of 
            candidates that will be interviewed, the methodology used to test or trial the candidates and the criteria that will be used to find the perfect candidate""",
            verbose=True,
            allow_delegation=False,
            llm=self.gpt3,
    
        )