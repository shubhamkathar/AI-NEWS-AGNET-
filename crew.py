from crewai import Agent, Crew, Process, Task , LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
import os
from dotenv import load_dotenv
load_dotenv()

NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY")



nvidia_llm= LLM (

    model="nvidia/llama-3.1-nemotron-70b-instruct",
    base_url = "https://integrate.api.nvidia.com/v1",
    api_key = NVIDIA_API_KEY
)

@CrewBase
class Reseach_crew:
	

	@agent
	def researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher'],
			tools=[SerperDevTool(), ScrapeWebsiteTool()],
			llm=nvidia_llm,
			#allow_delegation=True,
			verbose=True
		)

	@agent
	def reporting_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['reporting_analyst'],
			llm=nvidia_llm,
			#allow_delegation=True,
			verbose=True
		)

	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
		)

	@task
	def reporting_task(self) -> Task:
		return Task(
			config=self.tasks_config['reporting_task'],
			output_file='report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Day03 crew"""
		return Crew(
			agents=self.agents,
			tasks=self.tasks, 
			process=Process.sequential,
			llm=nvidia_llm,
			verbose=True,
		)