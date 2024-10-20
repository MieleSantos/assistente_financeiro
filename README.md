
# Assistente Financeiro Inteligente

### projeto desenvolvido no curso IA Master

Este projeto é um **Assistente Financeiro Inteligente** baseado em **LangChain**, integrando agentes de IA como **Python REPL**, **DuckDuckGo** para consultas web e **OpenAI** para modelagem de linguagem natural, oferecendo suporte a perguntas e cálculos financeiros em tempo real. O objetivo é criar um assistente que responda dúvidas financeiras, execute cálculos complexos e realize pesquisas sobre informações econômicas e financeiras de forma eficiente.

## Funcionalidades

- **Consultas Financeiras**: Faz consultas diretas sobre tópicos financeiros, como tendências de mercado, taxas de câmbio, e informações sobre ativos.
- **Cálculos Financeiros**: Usa o agente Python REPL para realizar cálculos de juros compostos, simulações de investimento e outras operações matemáticas.
- **Consultas Web**: Integração com o DuckDuckGo para buscar informações financeiras atualizadas.
- **Suporte a Linguagem Natural**: Usa o OpenAI para interpretar perguntas em linguagem natural e devolver respostas adequadas.

## Tecnologias Utilizadas

- **LangChain**: Framework para desenvolver aplicativos que utilizam modelos de linguagem.
- **Python**: Linguagem principal para lógica do agente e cálculos.
- **OpenAI API**: Utilizado para interpretar as consultas em linguagem natural e gerar respostas.
- **DuckDuckGo API**: Para realizar consultas de busca na web e obter informações financeiras atualizadas.
- **Python REPL**: Agente para execução de cálculos financeiros em tempo real.

## Pré-requisitos

Para rodar este projeto localmente, você precisará ter:

- Python 3.8+ instalado
- API key do OpenAI
- API key do DuckDuckGo (se aplicável)
- Dependências do projeto listadas no `pyproject.toml`

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/mielesantos/assistente-financeiro.git
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd assistente-financeiro
   ```

3. Instale as dependências:
   ```bash
   poetry install 
   ```

4. Configure suas chaves de API no arquivo `.env` ou diretamente no código:
   ```
   OPENAI_API_KEY=<sua_openai_api_key>
   ```

## Uso

### Execução do Assistente

Após configurar as chaves de API, você pode rodar o assistente da seguinte forma:

```bash
python main.py
```

Isso iniciará uma interface onde você pode fazer perguntas financeiras, como:

- "Qual é a taxa de câmbio atual do dólar?"
- "Qual será o retorno de um investimento de R$ 10.000 em 5 anos com uma taxa de 7% ao ano?"
- "Quais são as ações mais valorizadas atualmente?"

### Exemplo de Fluxo

1. O usuário faz uma pergunta em linguagem natural.
2. O LangChain distribui a tarefa para os agentes apropriados (Python REPL ou DuckDuckGo).
3. O Python REPL é usado para cálculos financeiros e o DuckDuckGo para consultas web.
4. A resposta é processada e devolvida ao usuário.


![image\result.jpg](image\result.jpg)