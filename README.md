# 🚀 Full-Stack Flask & Database Sandbox

A multi-project repository showcasing lightweight RESTful APIs, dynamic routing, and database persistence using **Python**, **Flask**, and **SQLite**.

---

## 🛠️ Projects Included

### 1. 🔒 Persistent Data Vault (`vault_app.py`)
A full-stack CRUD (Create, Read, Delete) application that stores entries directly in a local **SQLite database**.

* **Dynamic Web Interface:** Clean UI built with embedded CSS to write and remove notes.
* **Database Persistence:** Uses real SQL `INSERT`, `SELECT`, and `DELETE` queries to store user data in `vault.db`.
* **REST API Endpoint:** Serves stored records as raw JSON for external client consumption.

### 2. ⚡ CYBER_OS Terminal API (`app.py`)
A retro-futuristic Cyberpunk command terminal API that handles simulated system diagnostics and interactive URL commands.

* **Interactive Routes:** Serves static terminal HTML at the root endpoint.
* **Dynamic Parameter Handling:** Parses route IDs and query parameters to execute simulated terminal commands like `override` and `reboot`.

---

## 💻 Technical Stack

* **Language:** Python 3
* **Framework:** Flask
* **Database:** SQLite3
* **Frontend:** HTML5 / CSS3

---

## 📌 Main Endpoints

| Application | Endpoint | Method | Description |
| :--- | :--- | :--- | :--- |
| **Vault** | `/` | `GET` | Main Web Interface for viewing & creating notes |
| **Vault** | `/add` | `POST` | Saves a new record into the SQLite database |
| **Vault** | `/delete/<id>` | `POST` | Deletes a record from the database by ID |
| **Vault** | `/api/notes` | `GET` | REST API returning all stored database notes in JSON |
| **Terminal** | `/api/status` | `GET` | System diagnostics & memory load metrics |
| **Terminal** | `/api/execute` | `GET` | Accepts command inputs via query parameters (`?command=override`) |

---

## 👤 Author

* **Matodzi Nevhutala**
