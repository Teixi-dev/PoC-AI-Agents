from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_openai_functions_agent, load_tools
from langchain.agents.format_scratchpad.openai_tools import (
    format_to_openai_tool_messages,
)
from langchain.agents.output_parsers.openai_tools import OpenAIToolsAgentOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain import hub


class LlmCallerService:

    def __init__(self) -> None:
        self.llm = ChatOpenAI(
            base_url="http://localhost:11434/v1",
            api_key="lm-studio",
            model="LM Studio Community/Meta-Llama-3-8B-Instruct-GGUF",
            temperature=0,
            max_tokens=-1
        )

    def execute(self, query, tools):
        messages = [{"role": "user", "content": query}]

        return AgentExecutor(
            agent=self.createAgent(tools=tools),
            tools=tools,
            llm=self.llm,
            verbose=True
        ).invoke({"input": query})

    def createAgent(self, tools):
        return create_openai_functions_agent(self.llm, tools, self.createPrompt())

    def createPrompt(self):
        return hub.pull("hwchase17/openai-functions-agent")
