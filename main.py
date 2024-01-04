
import os
from llama_index.llms import OpenAI
from llama_index.agent import ReActAgent, OpenAIAgent
from llama_index.tools import FunctionTool
import subprocess
from llama_index.callbacks import LlamaDebugHandler, CallbackManager


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

def open_aplication() -> str:
    """Open an aplication in the computer."""
    try:
        subprocess.call("explorer .", shell=True)
        return "Aplication sucessfully opened"
    except Exception as e:
        print(f"An error occurred: {e}")

def open_browser() -> str:
    """Open browser in the computer."""
    try:
        browser_path = "" #local browser path
        url = "https://www.google.com"
        subprocess.Popen([browser_path, url])
        return "Browser sucessfully opened"
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("Using llamaindex agents.")
    
    # Name of the tools must be the same as the function name
    tool1 = FunctionTool.from_defaults(fn=write_haiku, name="write_haiku")
    tool2 = FunctionTool.from_defaults(fn=count_characters, name="count_characters")
    tool3 = FunctionTool.from_defaults(fn=open_aplication, name="open_aplication")
    tool4 = FunctionTool.from_defaults(fn=open_browser, name="open_browser")

    tools=[tool1, tool2, tool3, tool4]

    llama_debug = LlamaDebugHandler(print_trace_on_end=True)
    callback_manager = CallbackManager(handlers=[llama_debug])

    agent = OpenAIAgent.from_tools(tools=tools, llm=llm, verbose=True, callback_manager=callback_manager)
    res = agent.query("write a haiku about water and then count characters in it, and if count result is more than 70 open aplication, and if is less than 70 open browser")
    print(res)