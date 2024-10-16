import os

from dotenv import load_dotenv
from langchain import hub
from langchain.agents import Tool, create_react_agent, AgentExecutor
from langchain.prompts import PromptTemplate
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_experimental.agents.agent_toolkits import create_python_agent
from langchain_experimental.utilities import PythonREPL
from langchain_openai import ChatOpenAI

load_dotenv()

os.environ['OPENAi_API_KEY'] = os.environ['API_KEY']

model = ChatOpenAI(model='gpt-3.5-turbo')

prompt = """
Como assistente financeiro pessoal que responderá as perguntas dadno dicas financeiras
e de investimentos.
Responda tudo em português brasileiro.
Perguntas: {q}
"""

prompt_template = PromptTemplate.from_template(prompt)

python_repl = PythonREPL()
prython_repl_tool = Tool(
    name='Python REPL',
    description='Un shell Python. Use isso para executar códigos Python.Execute apenas'
    + ' códigos Python válidos. Se precisa opbter o retorno do código, use a função'
    + ' "print(...)".Use para realizar cálculos financeiros necessários para responder'
    + ' as perguntas e da dicas',
    func=python_repl.run,
)

search = DuckDuckGoSearchRun()
duckduckgo_tool = Tool(
    name='Busca DuckuDuckGo',
    description='Útil para encontrar informações e dicas de economia e opções de '
    + 'investimento. Você sempre deve pesquiser na internet as melhores dicas usando'
    + ' esta ferramenta, não responda diretamente.Sua resposta deve infromaer que'
    + ' há elementos pesquisados na internet',
    func=search.run,
)


react_instructions = hub.pull('hwchase17/react')
# print(react_instructions)

tools = [prython_repl_tool, duckduckgo_tool]
# criando o agente
agent = create_react_agent(llm=model, tools=tools, prompt=react_instructions)

# criando o executor para executar o agente
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# question = """
# Minha renda é de R$10000 por mês, o total de minhas dispoesas e de R$8500 mais 1000 de aluguel.
# Quais dica de investimenro você me dá?
# """

# question = """
# Minha renda é de R$10000 por mês, tenho muitos cartões de crédito no total de R$12000 por mês.
# Quero fazer ma renda extra para sair ds dívidas.
# Quais dica de investimenro você me dá?
# """

question = input('Qual sua duvida:')
output = agent_executor.invoke({'input': prompt_template.format(q=question)})

print(output.get('output'))
