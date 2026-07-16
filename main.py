import os
from google.cloud import bigquery
from datetime import datetime

# 1. Configuração de autenticação
# Certifique-se de que o arquivo 'credenciais.json' está na mesma pasta!
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credenciais.json"

PROJECT_ID = 'projeto-gestao-incidentes'
client = bigquery.Client(project=PROJECT_ID)

def registrar_incidente(tipo, local, gravidade):
    categorias= ["Tabela não atualizada", "Duplicidade de dados", "Tabela Vazia", "Falha de conexão"]
    
    if tipo not in categorias:
        print(f"Atenção: O tipo '{tipo}' não está na lista padrão.")

    table_id = f"{PROJECT_ID}.gestao_incidentes.incidentes"
    
    rows_to_insert = [{
        "tipo_incidente": tipo, 
        "localizacao": local, 
        "gravidade": gravidade, 
        "data_hora": datetime.now().isoformat()
    }]
    
    try:
        errors = client.insert_rows_json(table_id, rows_to_insert)
        if errors == []:
            print(f"Sucesso! Incidente '{tipo}' registrado.")
        else:
            print(f"Erros ao inserir: {errors}")
    except Exception as e:
        print(f"Ocorreu um erro técnico: {e}")

# Teste:
if __name__ == "__main__":
    registrar_incidente("Duplicidade de dados", " Portal do Cliente", "API de Pagamentos",3)