import uvicorn
from fastapi import FastAPI
from src.graphs.graph_builder import GraphBuilder
from src.llms.groqllm import GroqLM
from src.schema.blog_request import BlogRequest
import os
from dotenv import load_dotenv
load_dotenv()


app = FastAPI()

LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")

if not LANGCHAIN_API_KEY:
    raise ValueError("LANGCHAIN_API_KEY not found")

os.environ['LANGCHAIN_API_KEY'] = LANGCHAIN_API_KEY

# Get the LLM object
groqllm = GroqLM()
llm = groqllm.get_llm()

# Get the Graph
graph_builder = GraphBuilder(llm)
graph = graph_builder.setup_graph(usecase='topic')

    
    
# Api
@app.post('/blogs')
async def create_blogs(request: BlogRequest):
    topic = request.topic
    
    state = graph.invoke({'topic': topic})
    
    return {'data': state}


if __name__  == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)