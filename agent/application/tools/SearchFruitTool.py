from langchain.tools import Tool


class SearchFruitTool:
    def __init__(self):
        self.fruits = ["manzana", "banana", "cereza"]
        self.tool = Tool(
            name="search_fruit",
            func=self.execute,
            description="Busca una fruta que contenga el texto dado."
        )

    def execute(self, query):
        return [fruit for fruit in self.fruits if query.lower() in fruit.lower()]
