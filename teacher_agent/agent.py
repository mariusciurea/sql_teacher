from google.adk.agents import LlmAgent
from teacher_agent.prompt import ROOT_INSTRUCTIONS
from query_agent.sub_agents.prompt_to_sql_agent.agent import prompt_to_sql_agent

root_agent = LlmAgent(
    name="query_agent",
    model="gemini-2.0-flash",
    description="The root agent who delegates tasks to sub-agents",
    instruction=ROOT_INSTRUCTIONS,
    sub_agents=[prompt_to_sql_agent],
)