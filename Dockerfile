# # Use a imagem base do Python
# FROM python:3.12-slim

# # Instale o Poetry
# RUN pip install --no-cache-dir poetry
# ENV PATH="/root/.local/bin:$PATH" 
# # Defina o diretório de trabalho
# WORKDIR /app

# # Copie os arquivos do Poetry para o container
# COPY pyproject.toml poetry.lock ./

# # Instale as dependências (incluindo as de produção)
# RUN poetry install --no-root

# # Copie o restante do código
# COPY . .

# # Exponha a porta da aplicação
# EXPOSE 8080

# # Comando para rodar a aplicação
# CMD ["poetry", "run", "uvicorn", "backend/main:app", "--host", "0.0.0.0", "--port", "8080"]

FROM python:3.12-slim


# Installing poetry
RUN pip install --upgrade pip poetry && pip cache purge
ENV PATH="/root/.local/bin:$PATH" 
ENV PYTHONUNBUFFERED=1 

# Enabling environment and transfering files
WORKDIR /app
COPY ./poetry.lock ./pyproject.toml ./
RUN poetry config virtualenvs.create false \
    && poetry install --only main --no-cache
COPY . ./