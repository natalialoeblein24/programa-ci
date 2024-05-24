# Usar a imagem base do Python
FROM python:3.10-slim

# Atualizar o pip para a versão mais recente
RUN pip install --no-cache-dir --upgrade pip

# Definir o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiar o arquivo requirements.txt para o contêiner
COPY requirements.txt .

# Criar e ativar um ambiente virtual
RUN python -m venv venv
ENV PATH="/app/venv/bin:$PATH"

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todos os arquivos do projeto para o contêiner
COPY . .

# Expor a porta que o Flask usará
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["python", "app.py"]
