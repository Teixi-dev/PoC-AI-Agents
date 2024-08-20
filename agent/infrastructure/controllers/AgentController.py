from fastapi import APIRouter, HTTPException
from agent.infrastructure.models.AgentRequest import AgentRequest
from agent.application.services.AgentUsecase import AgentUsecase


class AgentController:
    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route("/agent", self.execute, methods=["POST"])
        self.usecase = AgentUsecase()

    async def execute(self, query: AgentRequest):
        if not query.query:
            raise HTTPException(
                status_code=400, detail="Query cannot be empty")
        return self.usecase.execute(query.query)
