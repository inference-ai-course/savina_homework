# Example: Using LCEL to reproduce a "Basic Prompting" scenario
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_ollama import ChatOllama 
import gradio as gr

# 2. Define the prompt
prompt = PromptTemplate.from_template(
    "What is the capital of {topic}?"
)

# 3. Define the model
model = ChatOllama(model = "llama3")  # Using Ollama 

# 4. Chain the components together using LCEL
chain = (
    # LCEL syntax: use the pipe operator | to connect each step
    {"topic": RunnablePassthrough()}  # Accept user input
    | prompt                          # Transform it into a prompt message
    | model                           # Call the model
    | StrOutputParser()               # Parse the output as a string
)

# 5. Execute
def ask_ai(quesiton):
    result = chain.invoke({"Question":quesiton})
    return result


# Create a Gradio interface for the function
iface = gr.Interface(
    fn=ask_ai,
    inputs="text",
    outputs="text",
    title="What is the capital city of the country?",
    description="Enter country, and this app will tell the capital city.",
)

# Launch the Gradio app
iface.launch()

