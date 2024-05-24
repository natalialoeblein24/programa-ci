# Usar a imagem base do Python
FROM python:3.10-slim

# Definir o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiar o arquivo requirements.txt para o contêiner
COPY requirements.txt .

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todos os arquivos do projeto para o contêiner
COPY . .

# Expor a porta que o Flask usará
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "app.py"]
