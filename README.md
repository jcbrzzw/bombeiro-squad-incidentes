# 🚒 Automação de Incidentes

Este projeto tem como objetivo automatizar o registro de incidentes de Qualidade de Dados (Data Quality). Ele detecta falhas em pipelines de dados e registra automaticamente no Google BigQuery, permitindo monitoramento e análise de tendências de incidentes.

## 🚀 Funcionalidades

- Insere incidentes diretamente no BigQuery.
- Validação de tipos de erro para manter a integridade dos dados.
- Pronto para ser integrado com ferramentas de notificação Slack/Trello.

## 🛠️ Tecnologias Utilizadas

- Python
- Google BigQuery
- Google Cloud Platform (IAM & Service Accounts)

## ⚙️ Como configurar e rodar
1. Clone o repositório:

```Bash
git clone https://github.com/jcbrzzw/bombeiro-squad-incidentes.git
cd bombeiro-squad-incidentes
```

2. Crie um ambiente virtual e instale as dependências:
```Bash
python -m venv venv
# No Windows:
.\venv\Scripts\activate
# No Mac/Linux:
source venv/bin/activate

pip install google-cloud-bigquery
```
3. Configuração do Google Cloud:
- Crie uma Service Account no seu projeto GCP com a permissão BigQuery Data Editor.
- Baixe a chave em formato JSON.
- Salve o arquivo na raiz do projeto como credenciais.json.

4. Execute o sistema:
```Bash
python main.py
 ```

## 🗺️ Roadmap (Próximos Passos)
- [ ] **Integração com Trello:** Automatizar a criação de cards para gestão de tarefas.
- [ ] **Notificações no Slack:** Enviar alertas em tempo real para a squad quando um incidente crítico for registrado.
- [ ] **Dashboard no Looker Studio:** Criar um painel visual para monitorar a frequência de incidentes por categoria.

## 📊 Status do Projeto
O projeto está em fase de implementação. Abaixo, um exemplo de como a estrutura da tabela é apresentada no Google BigQuery:

<img width="1274" height="384" alt="image" src="https://github.com/user-attachments/assets/1d226be2-1411-4ace-8fb1-7d669de27350" />



