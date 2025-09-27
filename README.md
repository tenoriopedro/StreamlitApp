# 🎬 Flix App

**Flix App** is an interactive web application built with **Python** and **Streamlit**, providing a complete dashboard for **managing movies, genres, actors/actresses, and reviews**.
It consumes data from an **external RESTful API** and combines a **well-structured architecture** (JWT authentication, layered design, API consumption) with an **intuitive, modern interface**.

This project serves both as a **practical tool** and as a **portfolio showcase**, demonstrating strong technical implementation and clean UI design.

---

## 🚀 Key Features

* **Secure authentication** with JWT (login/logout and session control).
* **Full CRUD operations** for:

  * Movies
  * Genres
  * Actors/Actresses
  * Reviews
* **Interactive dashboard** with movie statistics (charts powered by Plotly).
* **User-friendly interface** built with Streamlit and interactive grids via **st_aggrid**.
* **Layered architecture** (Page → Service → Repository), enabling maintainability and scalability.

---

## 🏗️ Project Structure

```
├── app.py             # Streamlit entry point
├── api/               # Authentication and API integration
├── actors/            # Actor/actress management
├── genres/            # Genre management
├── movies/            # Movie management
├── reviews/           # Review management
├── home/              # Dashboard and statistics
├── login/             # Login and session handling
├── utils/             # Utilities (e.g., API path)
├── dotenv_files/      # Environment configs (.env, .env-example)
├── requirements.txt   # Project dependencies
└── .flake8            # Linting configuration
```

Each domain (`actors`, `genres`, `movies`, `reviews`) follows a modular structure:

* `page.py` → user interface (Streamlit)
* `service.py` → application logic
* `repository.py` → API communication

---

## ▶️ Usage

Run the application with:

```bash
streamlit run app.py
```

The app will open in your default browser with a sidebar menu for:

* **Login**
* **Dashboard (Home)**
* **Genre Management**
* **Actor/Actress Management**
* **Movie Management**
* **Review Management**

---

## 📊 Dashboard Examples

* Movie distribution by genre (pie chart)
* Total number of movies
* Total number of reviews
* Overall average star rating

---

## 🛠️ Tech Stack

* [Python](https://www.python.org/)
* [Streamlit](https://streamlit.io/)
* [st_aggrid](https://pypi.org/project/streamlit-aggrid/)
* [Plotly](https://plotly.com/python/)
* [Requests](https://requests.readthedocs.io/)
* [python-dotenv](https://pypi.org/project/python-dotenv/)

---

## 🔍 Technical Notes

* The system depends on an **external API** configured in `.env`.
* Session and authentication are managed via `st.session_state`.
* On **401 Unauthorized** responses, the app forces logout for security.
* Areas for future improvement: automated testing, enhanced error handling, consistent naming conventions.

---

## 📄 License

This project is open-source and available for study, demonstration, and portfolio purposes.
