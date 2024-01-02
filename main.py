
import os
from llama_index.llms import OpenAI
from llama_index.agent import ReActAgent
from llama_index.tools import FunctionTool

llm = OpenAI(
  model="gpt-3.5-turbo",
  temperature=0.9
)

def write_haiku(topic: str) -> str:
    """Write a haiku about a given topic."""
    return llm.complete("write a haiku about {topic}")

def count_characters(text: str) -> int:
    """Count the number of characters in a string."""
    return len(text)

if __name__ == "__main__":
    print("Using llamaindex agents.")
    
    tool1 = FunctionTool.from_defaults(fn=write_haiku, name="write_haiku")
    tool2 = FunctionTool.from_defaults(fn=count_characters, name="count_characters")

    agent = ReActAgent.from_tools(tools=[tool1, tool2], llm=llm, verbose=True)
    res = agent.query("write a haiku about fire and then count characters in it")
    print(res)