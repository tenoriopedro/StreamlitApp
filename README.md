# 🎬 Flix App (Cliente Streamlit)

<p align="center">
  <a href="https://appapp-nn6fq8ue8qikftrqoi9kfm.streamlit.app/">[ 📊 Ver App Interativa ]</a>
</p>

Uma aplicação web interativa construída em **Streamlit** que funciona como um dashboard para gestão de filmes, géneros e críticas.

Este projeto é o **cliente frontend** que consome a [Movie Catalog API (Django REST Framework)](https://github.com/tenoriopedro/flix_api), demonstrando uma arquitetura full-stack desacoplada.

---

### 📊 Dashboard e Funcionalidades

Em vez de *listar* as funcionalidades, aqui está a aplicação em ação.

<p align="center">
  <img src="https://github.com/tenoriopedro/StreamlitApp/blob/main/streamlitapp.gif?raw=true" alt="Demonstração do Dashboard Flix App" width="700"/>
</p>

* **Autenticação Segura:** Login/logout com gestão de sessão (JWT).
* **Operações CRUD:** Gestão completa de Filmes, Géneros, Atores e Críticas.
* **Dashboard Interativo:** Gráficos de estatísticas (via Plotly) e grelhas de dados (via `st_aggrid`).

---

### 🏛️ Arquitetura (Cliente-Servidor)

Este projeto não funciona sozinho. Ele foi desenhado como o "Cliente" num ecossistema Cliente-Servidor.

* **Cliente (Este Projeto):** `Flix App (Streamlit)`
    * Responsável pela interface do utilizador (UI).
    * Gere a sessão e o estado (via `st.session_state`).
    * Faz chamadas HTTP (GET, POST, PUT, DELETE) para a API.

* **Servidor (Projeto Separado):** `Movie Catalog API (DRF)`
    * [Link para o Repositório da API](https://github.com/tenoriopedro/flix_api)
    * Responsável pela lógica de negócio, persistência na base de dados e autenticação (JWT).

O código-fonte do cliente está organizado numa **arquitetura em camadas** para manutenibilidade:
`Page (UI)` → `Service (Lógica da App)` → `Repository (Comunicação API)`

---

### 🛠️ Stack Tecnológico (Cliente)

* [Python](https://www.python.org/)
* [Streamlit](https://streamlit.io/) (Framework da UI)
* [st_aggrid](https://pypi.org/project/streamlit-aggrid/) (Grelhas interativas)
* [Plotly](https://plotly.com/python/) (Visualização de dados)
* [Requests](https://requests.readthedocs.io/) (Consumo da API)
* [python-dotenv](https://pypi.org/project/python-dotenv/)

---

### ⚙️ Instalação (Local)

<details>
  <summary>Clique para ver as instruções de setup local</summary>
  
  <p>Para executar este cliente localmente, você <strong>precisa</strong> de ter a <a href="https://github.com/tenoriopedro/flix_api">Movie Catalog API</a> a correr primeiro.</p>

  <ol>
    <li>Clone este repositório.</li>
    <li>Crie e ative um ambiente virtual e instale as dependências: <code>pip install -r requirements.txt</code></li>
    <li>Copie <code>dotenv_files/.env-example</code> para <code>dotenv_files/.env</code>.</li>
    <li>No ficheiro <code>.env</code>, configure o URL base da sua API (ex: <code>API_URL=http://127.0.0.1:8000/api</code>).</li>
    <li>Execute a aplicação Streamlit:</li>
  </ol>
  
  ```bash
  streamlit run app.py
```

</details>
