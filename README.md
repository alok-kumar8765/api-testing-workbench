# ⚡ API Testing Workbench

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-FF4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-150458.svg?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Plotly](https://img.shields.io/badge/Plotly-5.0%2B-3F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

A lightweight, interactive, web-based **API Testing Workbench** built with Python, Streamlit, Requests, Pandas, and Plotly. Designed for developers, QA engineers, and beginners who need a fast, dependency-light alternative to Postman for dispatching HTTP requests, inspecting payloads, analyzing latency trends, and converting JSON responses into tabular structures.

---

## 📋 Table of Contents

- [✨ Key Features](#-key-features)
- [💻 System Requirements](#-system-requirements)
- [⚙️ Installation & Setup Guide](#️-installation--setup-guide)
- [🎓 Beginner's Guide: HTTP Methods & How They Work](#-beginners-guide-http-methods--how-they-work)
  - [1. GET Request](#1-get-fetch-data)
  - [2. POST Request](#2-post-create-new-data)
  - [3. PUT Request](#3-put-replace-existing-data)
  - [4. PATCH Request](#4-patch-partially-update-data)
  - [5. DELETE Request](#5-delete-remove-data)
- [📖 User Manual & Feature Walkthrough](#-user-manual--feature-walkthrough)
  - [Quick Presets & Session History](#quick-presets--session-history)
  - [Request Configuration Tabs](#request-configuration-tabs)
  - [Response Inspector & Tabular View](#response-inspector--tabular-view)
  - [Performance & Latency Analytics](#performance--latency-analytics)
- [📐 System Architecture & Diagrams](#-system-architecture--diagrams)
  - [📁 Directory / File Structure](#-directory--file-structure)
  - [🔄 Data Flow Diagram (DFD)](#-data-flow-diagram-dfd)
  - [🗄️ Entity-Relationship / Data Schema Diagram](#️-entity-relationship--data-schema-diagram)
- [⚖️ Pros, Cons & Limitations](#️-pros-cons--limitations)
- [🛡️ Known Issues & Security Considerations](#️-known-issues--security-considerations)
- [🚀 Future Updates & Roadmap](#-future-updates--roadmap)
- [⭐ Contributing & Acknowledgments](#-contributing--acknowledgments)
- [📜 License](#-license)

---

## ✨ Key Features

- **🚀 Full HTTP Method Support:** Dispatch `GET`, `POST`, `PUT`, `PATCH`, and `DELETE` requests with custom headers, query parameters, and JSON payloads.
- **⚡ Presets for Rapid Testing:** Built-in one-click templates (JSONPlaceholder GET/POST, Httpbin Delay Simulation) to quickly verify endpoints.
- **📜 Interactive Request History:** Track all dispatched requests across the session with one-click reload capabilities.
- **📊 Response Inspector:** Inspect HTTP status codes, exact response times (ms), and payload character counts instantly.
- **📋 Automatic Tabular Flattening:** Powered by Pandas, automatically converts complex nested JSON lists and dictionaries into readable DataFrames.
- **📈 Real-Time Analytics:** Plotly line charts and status code histograms track performance and latency trends across your testing session.

---

## 💻 System Requirements

- **Operating System:** Windows 10/11, macOS, or Linux
- **Python Version:** Python 3.8, 3.9, 3.10, 3.11, or 3.12
- **Web Browser:** Any modern browser (Google Chrome, Mozilla Firefox, Microsoft Edge, Safari)

---

## ⚙️ Installation & Setup Guide

### 1. Clone the Repository
```bash
git clone https://github.com/alok-kumar8765/api-testing-workbench.git
cd api-testing-workbench
```

### 2. Set Up a Virtual Environment (Recommended)

**On Windows:**
```cmd
python -m venv venv
venv\Scripts\activate
```

**On macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install streamlit requests pandas plotly
```

*(Alternatively, run `pip install -r requirements.txt` if available).*

### 4. Run the Application
```bash
streamlit run app.py
```

The app will launch in your browser at `http://localhost:8501`.

---

## 🎓 Beginner's Guide: HTTP Methods & How They Work

If you are new to APIs, HTTP methods (verbs) tell the remote server what action you wish to perform on a resource.

---

### 1. GET (Fetch Data)
- **Purpose:** Used to retrieve data from a server without modifying anything.
- **How to use in Workbench:**
  1. Set **Method** dropdown to `GET`.
  2. Enter the URL (e.g., `https://jsonplaceholder.typicode.com/posts/1`).
  3. *(Optional)* Add URL query parameters in the **Query Params** tab (e.g., `{"userId": 1}`).
  4. Click **🚀 Send Request**.

---

### 2. POST (Create New Data)
- **Purpose:** Used to send data to the server to create a new record.
- **How to use in Workbench:**
  1. Set **Method** dropdown to `POST`.
  2. Enter the target endpoint URL (e.g., `https://jsonplaceholder.typicode.com/posts`).
  3. Click the **📦 Body (JSON)** tab and enter the new data structure:
     ```json
     {
       "title": "My New Article",
       "body": "This is the content of the article.",
       "userId": 1
     }
     ```
  4. Click **🚀 Send Request**.

---

### 3. PUT (Replace Existing Data)
- **Purpose:** Replaces an entire existing resource with new data. If fields are omitted, the server usually overwrites them with nulls.
- **How to use in Workbench:**
  1. Set **Method** dropdown to `PUT`.
  2. Target the specific item ID in the URL (e.g., `https://jsonplaceholder.typicode.com/posts/1`).
  3. Provide the full replacement payload in **📦 Body (JSON)**:
     ```json
     {
       "id": 1,
       "title": "Completely Updated Title",
       "body": "Completely updated body content.",
       "userId": 1
     }
     ```
  4. Click **🚀 Send Request**.

---

### 4. PATCH (Partially Update Data)
- **Purpose:** Modifies only specific fields of an existing resource without overwriting the entire record.
- **How to use in Workbench:**
  1. Set **Method** dropdown to `PATCH`.
  2. Target the item URL (e.g., `https://jsonplaceholder.typicode.com/posts/1`).
  3. Provide only the fields you wish to modify in **📦 Body (JSON)**:
     ```json
     {
       "title": "Only Change The Title"
     }
     ```
  4. Click **🚀 Send Request**.

---

### 5. DELETE (Remove Data)
- **Purpose:** Deletes a specific resource from the server.
- **How to use in Workbench:**
  1. Set **Method** dropdown to `DELETE`.
  2. Target the item ID in the URL (e.g., `https://jsonplaceholder.typicode.com/posts/1`).
  3. Body payload is typically left empty (`{}`).
  4. Click **🚀 Send Request**. Expect a status code like `200 OK`, `202 Accepted`, or `204 No Content`.

---

## 📖 User Manual & Feature Walkthrough

### Quick Presets & Session History
- **Presets:** Select pre-configured templates from the sidebar dropdown (e.g., *JSONPlaceholder POST*) to auto-populate request settings.
- **History:** Every request sent is saved in the sidebar. Click any history button to reload its response details into the **Response Inspector**.
- **Clear History:** Click **Clear History** to clear past logs and reset the session state.

### Request Configuration Tabs
- **📦 Body (JSON):** Input valid JSON payloads for `POST`, `PUT`, or `PATCH`.
- **📋 Headers:** Specify HTTP request headers (defaults to `{"Content-Type": "application/json"}`). An automated fallback `User-Agent` is injected if missing.
- **🔍 Query Params:** Supply key-value parameters formatted as JSON. They are automatically appended to your URL string.

### Response Inspector & Tabular View
- **Metrics Bar:** View the HTTP Status Code (e.g., `200`, `201`, `404`, `500`), Latency in milliseconds, and Payload Size.
- **📄 JSON Response:** Clean, syntax-highlighted JSON viewer.
- **📋 Tabular View (Pandas):** Converts array responses or dictionaries into an interactive, sortable Pandas DataFrame table.

### Performance & Latency Analytics
- **Latency Trend:** A line graph tracking request latency (ms) across the current testing session.
- **Status Code Breakdown:** Histogram displaying distribution of response statuses categorized by HTTP method.

---

## 📐 System Architecture & Diagrams

### 📁 Directory / File Structure

```
api-testing-workbench/
│
├── app.py               # Main Streamlit application file (UI, execution logic, state management)
├── README.md            # Comprehensive project documentation
└── requirements.txt     # List of required Python packages
```

### 🔄 Data Flow Diagram (DFD)

```
 +------------------+            Method, URL, Headers, Body, Params
 |                  | ---------------------------------------------------+
 |   User Browser   |                                                    |
 |    (Frontend)    | <------------------------------------+             |
 +------------------+      Status, Response, Latency, Data |             v
                                                           |   +-------------------+
                                                           |   | Streamlit Engine  |
                                                           |   |     (app.py)      |
                                                           |   +-------------------+
                                                           |             |
                                         Render Data &     |             | HTTP Request
                                         Analytics Charts  |             v
                                                 +-------------------------------+
                                                 |        Remote REST API        |
                                                 |       (External Server)       |
                                                 +-------------------------------+
```

### 🗄️ Entity-Relationship / Data Schema Diagram

```
+-------------------------------------------------------+
|                    SESSION STATE                      |
+-------------------+---------------+-------------------+
| Key               | Type          | Description       |
+-------------------+---------------+-------------------+
| history           | List[Dict]    | Request history   |
| last_response     | Dict          | Active response   |
+-------------------+---------------+-------------------+
          |
          | Stores multiple items of
          v
+-------------------------------------------------------+
|                    HISTORY ITEM                       |
+-------------------+---------------+-------------------+
| Field             | Type          | Example           |
+-------------------+---------------+-------------------+
| timestamp         | string        | 2026-10-26 19:59  |
| method            | string        | POST              |
| url               | string        | https://api.com   |
| status            | integer       | 200               |
| time_ms           | float         | 124.50            |
| response          | dict/list     | {"id": 1}         |
| headers           | dict          | {"Content-Type"}  |
+-------------------+---------------+-------------------+
```

---

## ⚖️ Pros, Cons & Limitations

### Pros
- **Zero External Dependencies:** No account creation or bulky native installations required.
- **Built-in Visualizations:** Automatically maps latency and HTTP status code distribution.
- **DataFrame Exporting:** Converts messy nested JSON lists into tables.

### Cons & Limitations
- **Session-Based Persistence:** Closing or refreshing the browser tab resets request history.
- **Single Request Focus:** Designed for ad-hoc API testing; does not support automated collection runs or chain scripts out-of-the-box.
- **Local CORS Restrictions:** Subject to client machine network constraints and corporate proxy rules.

---

## 🛡️ Known Issues & Security Considerations

- **Invalid JSON Formatting:** Malformed JSON in Headers, Query Params, or Body inputs will throw a parsing warning. Ensure standard JSON formatting (e.g., use double quotes `"` instead of single quotes `'`).
- **Sensitive Key Exposure:** Avoid testing sensitive API credentials (bearer tokens, secret keys) on public or hosted Streamlit instances, as history resides in browser session state.

---

## 🚀 Future Updates & Roadmap

- [ ] **Export to Postman Collection:** Convert test sessions into importable Postman JSON collections.
- [ ] **Bearer Token / OAuth2 Tab:** Dedicated authentication tab supporting Bearer, Basic Auth, and API Key headers.
- [ ] **Persistent Storage:** Add SQLite/Local File export options for request history.
- [ ] **cURL Import/Export:** Paste raw cURL commands to auto-fill methods, headers, and payloads.

---

## ⭐ Contributing & Acknowledgments

Contributions, bug reports, and feature requests are welcome!

1. **Fork** the repository.
2. **Create** your feature branch (`git checkout -b feature/NewFeature`).
3. **Commit** your changes (`git commit -m 'Add NewFeature'`).
4. **Push** to the branch (`git push origin feature/NewFeature`).
5. **Open** a Pull Request.

### Show Your Support

If you find this project useful, please consider giving it a ⭐ on GitHub!

Developed with ❤️ by [Alok Kumar](https://github.com/alok-kumar8765).

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).