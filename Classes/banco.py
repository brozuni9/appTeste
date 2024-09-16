import pyodbc

class Bb():
    def __init__(self) -> None:
        pass
    

    def executaQuery(_self,query, commit=False, Params=[]):
        dados_conexao = (
            "Driver={SQL Server};"
            "Server=DESKTOP-761FVLB\\SQLEXPRESS;"
            "Database=ROBO_TRUST;"
        )
        
        try:
            with pyodbc.connect(dados_conexao) as CONEXAO:
                with CONEXAO.cursor() as CURSOR:
                    print(f'QUERY EXC {query}')
                    if len(Params) > 0:
                        CURSOR.execute(query, Params)
                    else:
                        CURSOR.execute(query)
                    if commit:
                        CONEXAO.commit()
                                          
                    return CURSOR.description, CURSOR.fetchall()  # Se você precisar retornar resultados
        except Exception as e:
            print(f"QUERY {query} \n An error occurred: {e}")
        
        return [] 