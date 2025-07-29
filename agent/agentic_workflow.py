from utils.model_loader import ModelLoader
from langgraph.graph import MessageState, StateGraph, END, START
from langgraph.prebuilt import ToolNode, tools_condition 
from prompt_library.prompt import SYSTEM_PROMT

class GraphBuilder:
    def __init__(self):
        self.tools = [
            

        ] 
    
    def agentic_function(self, state:MessageState):
        """Main agent function """
        user_question = state["messages"]
        input_question = [self.system_prompt] + user_question
        response = self.llm_with_tools.invoke(input_question)
        return {"messages": [response]}

    def build_graph(self):
        graph_builder= StateGraph(MessageState)
        graph_builder.add_node("agent", self.agentic_function)
        graph_builder.add_node("tools", ToolNode(tools = self.tools))
        graph_builder.add_edge(START, "agent")
        graph_builder.add_conditional_edge("agent", tools_condition)
        graph_builder.add_edge("tools","agent")
        graph_builder.add_edge("agent",END)
        self.graph = graph_builder.compile()
        return self.graph
    

