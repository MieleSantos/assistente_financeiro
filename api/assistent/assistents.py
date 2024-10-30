import os

from dotenv import load_dotenv
from langchain import hub
from langchain.agents import AgentExecutor, Tool, create_react_agent
from langchain.prompts import PromptTemplate
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_experimental.utilities import PythonREPL
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq


class FinancialAssistant:
    def __init__(self, type_ai='groq'):
        """Inicializa o assistente financeiro configurando todas as ferramentas
        necessárias."""
        load_dotenv()
        self._setup_environment_variables()
        self.model = self.get_model(type_ai)
        self.prompt_template = self._create_prompt_template()
        self.tools = self._initialize_tools()
        self.agent_executor = self._create_agent_executor()

    def get_model(self, type_ai):  # noqa: PLR6301
        if type_ai == 'openai':
            return ChatOpenAI(model='gpt-3.5-turbo')
        else:
            return ChatGroq(model='llama3-groq-70b-8192-tool-use-preview')

    def _setup_environment_variables(self):  # noqa: PLR6301
        """Configura as variáveis de ambiente necessárias."""

        groq_api_key = os.getenv('GROQ_API_KEY')
        open_api_key = os.getenv('OPEN_API_KEY')
        if not open_api_key and not groq_api_key:
            raise ValueError(
                "A chave da API 'API_KEY' não foi encontrada nas variáveis de ambiente."
            )
        os.environ['GROQ_API_KEY'] = groq_api_key
        os.environ['OPENAI_API_KEY'] = open_api_key

    def _create_prompt_template(self):  # noqa: PLR6301
        """Cria o template de prompt que será utilizado pelo agente."""
        prompt_text = """
        Você é um assistente financeiro pessoal que fornecerá dicas financeiras e
        de investimentos e assuntos gerais. Responda todas as perguntas em português
        brasileiro.
        Pergunta: {q}
        """
        return PromptTemplate.from_template(prompt_text)

    def _initialize_tools(self):  # noqa: PLR6301
        """Inicializa as ferramentas que serão usadas pelo agente."""
        python_repl = PythonREPL()
        python_repl_tool = Tool(
            name='Python REPL',
            description=(
                'Um shell Python. Use isso para executar código Python. Execute apenas '
                'código Python válido. '
                'Se precisar obter o retorno do código, use a função '
                '"print(...)". Use para realizar cálculos financeiros necessários para'
                'responder às perguntas e dar dicas.'
            ),
            func=python_repl.run,
        )

        search = DuckDuckGoSearchRun()
        duckduckgo_tool = Tool(
            name='Busca DuckDuckGo',
            description=(
                'Útil para encontrar informações e dicas de economia e '
                'opções de investimento. '
                'Você deve sempre pesquisar na internet as melhores dicas usando '
                'esta ferramenta. '
                'Não responda diretamente sem pesquisa. Sua resposta deve informar que'
                'há elementos pesquisados na internet.'
            ),
            func=search.run,
        )

        return [python_repl_tool, duckduckgo_tool]

    def _create_agent_executor(self):
        """Cria o agente com as ferramentas e o modelo configurado."""
        react_instructions = hub.pull('hwchase17/react')
        agent = create_react_agent(
            llm=self.model, tools=self.tools, prompt=react_instructions
        )
        return AgentExecutor(agent=agent, tools=self.tools, verbose=True)

    def search_assistant(self, question: str) -> str:
        """Recebe uma pergunta e utiliza o agente para gerar uma resposta."""
        if not question:
            raise ValueError('A pergunta não pode estar vazia.')

        input_data = {'input': self.prompt_template.format(q=question)}
        output = self.agent_executor.invoke(input_data)
        return output.get('output', 'Sem resposta disponível.')


def search_assistent(question):
    assistant = FinancialAssistant()
    resposta = assistant.search_assistant(question)

    return {'response': resposta}
