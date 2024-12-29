# Use a imagem base do Python
FROM python:3.12-slim

# Instale o Poetry
RUN pip install --no-cache-dir poetry

# Defina o diretório de trabalho
WORKDIR /app

# Copie os arquivos do Poetry para o container
COPY pyproject.toml poetry.lock ./

# Instale as dependências (incluindo as de produção)
RUN poetry install --no-root --no-dev

# Copie o restante do código
COPY . .

# Exponha a porta da aplicação
EXPOSE 8080

# Comando para rodar a aplicação
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
