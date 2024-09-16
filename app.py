from flask import Flask, render_template
import pandas as pd
from Classes.banco import Bb

app = Flask(__name__)




@app.route('/')
def home():
    ab =" TESTE DE TEXTO PASSADO DIFERENTE "
    brind= '''             ''' f'{ab}' '''          '''    
    print(brind)

    c,query_results = Bb().executaQuery(" exec PROJETO_FOREX.P_INSERIR_PRINCIPAL ")

    # Obtendo os nomes das colunas
    nomes_colunas = [descricao[0] for descricao in c]
    
    #print(nomes_colunas)
    print(query_results)
    
    #= CASE WHEN RECOMENDACAO = 1 THEN '📈' ELSE '📉' END
    
    return render_template('index.html', nomes_colunas=nomes_colunas, query_results = query_results)



@app.route('/pg1')
def pg1():
    return render_template('pagina1.html')


@app.route('/pgEx')
def pgEx():
    return render_template('exemploDATATABLE.html')


@app.route("/fetch")
def fetch():
    # Criando o DataFrame
    data = {
        "codigo": [101, 102, 103],
        "Juncao": ["Dept A", "Dept B", "Dept Ccc"],
        "Juncao": ["Dept A1", "Dept B", "Dept C123"],
        "Juncao": ["Dept A2", "Dept B", "Dept Cas12"],
        "nm_func": ["Alice", "Bob", "Carlos"]
    }
    
    df = pd.DataFrame(data)
    # Exibindo o DataFrame
    print(df)

    return df.to_json(orient='records')


@app.route("/usuario/<usuario>")
def validaUsuario(usuario):
    return render_template("Usuario.html", nm_usu = usuario) 



if __name__ == '__main__':
    app.run(debug=True)

    






