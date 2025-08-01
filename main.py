from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from agent.agentic_workflow import GraphBuilder
from utils.save_to_document import save_document
from starlette.responses import JSONResponse
import os , datetime
from dotenv import load_dotenv
from pydantic import BaseModel
load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    question: str 

@app.post("/query") 
async def query_ravel_agent(query: QueryRequest):
    try : 
        print(query)
        graph = GraphBuilder()
        app = graph()

        png_graph = app.get_graph().draw_mermaid_png()
        with open("my_graph.png", "wb") as f:
            f.write(png_graph)

        messages = {"messages": [query.question]}
        output = app.invoke(messages)

        if isinstance(output, dict) and "messages" in output:
            final_output = output["messages"][-1].content
        else: 
            final_output = str(output)

        return {"answer": final_output}
    except Exception as e: 
        return JSONResponse(status_code=500, content = {"error": str(e)})
    

