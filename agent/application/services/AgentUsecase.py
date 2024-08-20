from agent.infrastructure.services.LlmCallerService import LlmCallerService
from agent.application.tools.SearchFruitTool import SearchFruitTool


class AgentUsecase:

    def __init__(self) -> None:
        self.llmCaller = LlmCallerService()

    def execute(self, query):
        result = LlmCallerService().execute(
            query=query,
            tools=[SearchFruitTool().tool]
        )
        print(result)
        return "a"
