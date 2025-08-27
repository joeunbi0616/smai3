from langchain.agents import load_tools, initialize_agent, AgentType
from MyLCH import getOpenAI, getGenAI

if __name__ == '__main__':
    openllm = getOpenAI()
    genllm = getGenAI()

    tools = load_tools( ['wikipedia'], llm=openllm)

    agent = initialize_agent(
        tools,
        openllm,
        agent  =  AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=False,
        handle_parsing_errors=True
    )

    txt = "갤럭시 s25 스펙은?"
    print(agent.run(txt))

