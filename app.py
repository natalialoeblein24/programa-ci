from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Leitura do arquivo CSV com a primeira linha como cabeçalho
df = pd.read_csv('final.csv')

# Convertendo as colunas para float
for coluna in ['CRIAÇÃO', 'FINALIZAÇÃO', 'SUPERVISÃO', 'TOTAL']:
    df[coluna] = df[coluna].astype(float)

# Função para calcular o valor e o desconto
def calcular(item, tipo, desconto):
    linha = df[df['ID'] == int(item)]
    if linha.empty:
        return "Item não encontrado no DataFrame", None
    
    if tipo == '1':
        valor_criacao = linha['CRIAÇÃO'].values[0]
        valor_finalizacao = linha['FINALIZAÇÃO'].values[0]
        valor_supervisao = linha['SUPERVISÃO'].values[0]
        total = valor_criacao * 0.5 + valor_finalizacao + valor_supervisao
        percentual = total * (desconto / 100)  # Calcula a porcentagem de desconto
        desconto_final = total - percentual
        return (total, desconto_final, linha, valor_criacao, valor_finalizacao, valor_supervisao, 'Refação')
    elif tipo == '2':
        valor_criacao = linha['CRIAÇÃO'].values[0]
        valor_finalizacao = linha['FINALIZAÇÃO'].values[0]
        valor_supervisao = linha['SUPERVISÃO'].values[0]
        total = valor_criacao + valor_finalizacao + valor_supervisao
        percentual = total * (desconto / 100) # Calcula a porcentagem de desconto
        desconto_final = total - percentual
        return (total, desconto_final, linha, valor_criacao, valor_finalizacao, valor_supervisao, 'Criação')
    elif tipo == '3':
        valor_finalizacao = linha['FINALIZAÇÃO'].values[0]
        valor_supervisao = linha['SUPERVISÃO'].values[0]
        total = valor_finalizacao + valor_supervisao
        percentual = total * (desconto / 100)  # Calcula a porcentagem de desconto
        desconto_final = total - percentual
        return (total, desconto_final, linha, None, valor_finalizacao, valor_supervisao, 'Ajuste')
    else:
        return "Opção inválida", None

    resultado = {
        'total': total_com_desconto,
        'valor_desconto': valor_desconto,
        'valor_criacao': valor_criacao,
        'valor_finalizacao': valor_finalizacao,
        'valor_supervisao': valor_supervisao,
        'tipo_descricao': tipo_descricao
    }
    return resultado

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['GET', 'POST'])
def calcular_rota():
    if request.method == 'POST':
        item = request.form['item']
        tipo = request.form['tipo']
        desconto = float(request.form['desconto'])
        resultado = calcular(item, tipo, desconto)
        return render_template('resultado.html', resultado=resultado)
    return render_template('index.html')

@app.route('/lista')
def lista():
    lista_itens = df.to_dict(orient='records')
    return render_template('lista.html', lista_itens=lista_itens)

if __name__ == '__main__':
    app.run(debug=True, port=5000)