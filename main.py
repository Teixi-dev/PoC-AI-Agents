from fastapi import FastAPI
from dotenv import load_dotenv
from agent.infrastructure.controllers.AgentController import AgentController

app = FastAPI()
load_dotenv()
app.include_router(AgentController().router)
