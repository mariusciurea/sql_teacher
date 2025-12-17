from google.adk.agents import LlmAgent

from backend.teacher_agent.sub_agents.query_explainer_agent.prompt import QUERY_EXPLAINER_INSTRUCTIONS

query_explainer_agent = LlmAgent(
    name="query_explainer_agent",
    model="gemini_2.0-flash",
    description="An agent that explains in detail the SQL queries or commands",
    instruction=QUERY_EXPLAINER_INSTRUCTIONS,
)