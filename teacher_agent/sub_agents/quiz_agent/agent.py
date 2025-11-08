from google.adk.agents import LlmAgent
from teacher_agent.sub_agents.quiz_agent.prompt import QUIZ_INSTRUCTIONS
from teacher_agent.sub_agents.schema_designer_agent.agent import schema_designer_agent
from teacher_agent.sub_agents.memory_agent.agent import memory_agent

quiz_agent = LlmAgent(
    name="quiz_agent",
    model="gemini-2.0-flash",
    description="It generates quizzes about SQL so that the user can test his/her knowledge",
    instruction=QUIZ_INSTRUCTIONS,
)