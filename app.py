import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import json
import time
from datetime import datetime

# Page Configuration
st.set_page_config(
    page_title="API Testing Workbench",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize Session State for History
if "history" not in st.session_state:
    st.session_state.history = []

st.title("⚡ API Testing Workbench")
st.markdown("A lightweight, interactive API testing tool built with Python & Streamlit.")

# ==========================================
# SIDEBAR: Presets & Request History
# ==========================================
with st.sidebar:
    st.header("🗂️ Navigation & History")
    
    # Sample API Presets
    st.subheader("🚀 Quick Presets")
    preset = st.selectbox(
        "Load Sample API",
        ["Custom", "JSONPlaceholder (GET)", "JSONPlaceholder (POST)", "Httpbin (Delay Simulation)"]
    )
    
    default_url = "https://jsonplaceholder.typicode.com/todos/1"
    default_method = "GET"
    default_payload = "{}"
    
    if preset == "JSONPlaceholder (GET)":
        default_url = "https://jsonplaceholder.typicode.com/posts/1"
        default_method = "GET"
    elif preset == "JSONPlaceholder (POST)":
        default_url = "https://jsonplaceholder.typicode.com/posts"
        default_method = "POST"
        default_payload = json.dumps({"title": "foo", "body": "bar", "userId": 1}, indent=2)
    elif preset == "Httpbin (Delay Simulation)":
        default_url = "https://httpbin.org/delay/1"
        default_method = "GET"

    st.divider()
    st.subheader("📜 Request History")
    if st.session_state.history:
        if st.button("Clear History", use_container_width=True):
            st.session_state.history = []
            if "last_response" in st.session_state:
                del st.session_state.last_response
            st.rerun()
        
        for idx, item in enumerate(reversed(st.session_state.history)):
            btn_label = f"[{item['method']}] {item['url'][:28]}... ({item['status']})"
            if st.button(btn_label, key=f"hist_{idx}"):
                st.session_state.last_response = item
    else:
        st.info("No requests sent yet.")

# ==========================================
# MAIN REQUEST BUILDER
# ==========================================
col1, col2 = st.columns([1, 4])
with col1:
    methods = ["GET", "POST", "PUT", "DELETE", "PATCH"]
    method_idx = methods.index(default_method) if default_method in methods else 0
    method = st.selectbox("Method", methods, index=method_idx)
with col2:
    url = st.text_input("Request URL", value=default_url)

# Request Configuration Tabs
req_tab1, req_tab2, req_tab3 = st.tabs(["📦 Body (JSON)", "📋 Headers", "🔍 Query Params"])

with req_tab1:
    payload_input = st.text_area("JSON Payload", value=default_payload, height=140)
        
with req_tab2:
    headers_input = st.text_area("Headers (JSON format)", value='{\n  "Content-Type": "application/json"\n}', height=100)

with req_tab3:
    params_input = st.text_area("Query Params (JSON format)", value='{}', height=80)

# Execute Request Button
# Execute Request Button
if st.button("🚀 Send Request", type="primary", use_container_width=True):
    try:
        # Parse configurations safely
        headers = json.loads(headers_input) if headers_input.strip() else {}
        params = json.loads(params_input) if params_input.strip() else {}
        
        # Add a default User-Agent if not provided, to prevent server blocking
        if "User-Agent" not in headers:
            headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) API-Testing-Workbench/1.0"

        data = None
        if method in ["POST", "PUT", "PATCH"] and payload_input.strip():
            data = json.loads(payload_input)

        start_time = time.time()
        
        # Dispatch Request based on Method
        if method == "GET":
            response = requests.get(url, headers=headers, params=params, timeout=15)
        elif method == "POST":
            response = requests.post(url, headers=headers, params=params, json=data, timeout=15)
        elif method == "PUT":
            response = requests.put(url, headers=headers, params=params, json=data, timeout=15)
        elif method == "DELETE":
            response = requests.delete(url, headers=headers, params=params, timeout=15)
        elif method == "PATCH":
            response = requests.patch(url, headers=headers, params=params, json=data, timeout=15)
            
        elapsed_time = round((time.time() - start_time) * 1000, 2) # Latency in milliseconds
        
        # Safely Parse Response Body
        if response.text and response.text.strip():
            try:
                resp_json = response.json()
            except json.JSONDecodeError:
                # If it's not valid JSON, wrap raw text
                resp_json = {"raw_text": response.text}
        else:
            resp_json = {"warning": "Server returned a 200 OK status, but the response body was completely empty."}

        # Store History Item
        history_item = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "method": method,
            "url": url,
            "status": response.status_code,
            "time_ms": elapsed_time,
            "response": resp_json,
            "headers": dict(response.headers)
        }
        
        st.session_state.history.append(history_item)
        st.session_state.last_response = history_item
        st.success(f"Request completed in {elapsed_time} ms with status code {response.status_code}")

    except json.JSONDecodeError as jde:
        st.error(f"JSON Parsing Error in Payload/Headers/Params: {str(jde)}")
    except Exception as e:
        st.error(f"Error executing request: {str(e)}")
# ==========================================
# RESPONSE INSPECTOR & ANALYTICS
# ==========================================
if "last_response" in st.session_state:
    res = st.session_state.last_response
    
    st.divider()
    st.header("📊 Response Inspector")
    
    # Key Metrics Bar
    col_m1, col_m2, col_m3 = st.columns(3)
    with col_m1:
        st.metric("HTTP Status Code", res["status"])
    with col_m2:
        st.metric("Response Time", f"{res['time_ms']} ms")
    with col_m3:
        st.metric("Payload Size", f"{len(str(res['response']))} chars")

    # Detailed Response Tabs
    resp_tab1, resp_tab2, resp_tab3, resp_tab4 = st.tabs([
        "📄 JSON Response", 
        "📋 Tabular View (Pandas)", 
        "🗂️ Response Headers", 
        "📈 Performance Analytics"
    ])

    with resp_tab1:
        st.json(res["response"])

    with resp_tab2:
        st.markdown("Flattened tabular data representation:")
        try:
            data_to_frame = res["response"]
            if isinstance(data_to_frame, list):
                df = pd.DataFrame(data_to_frame)
            elif isinstance(data_to_frame, dict):
                df = pd.json_normalize(data_to_frame)
            else:
                df = pd.DataFrame({"Value": [data_to_frame]})
            
            if not df.empty:
                st.dataframe(df, use_container_width=True)
            else:
                st.info("Response is empty or cannot be converted into a table.")
        except Exception as e:
            st.warning(f"Could not render table view: {e}")

    with resp_tab3:
        st.json(res["headers"])

    with resp_tab4:
        if len(st.session_state.history) > 0:
            hist_df = pd.DataFrame(st.session_state.history)
            
            st.subheader("Latency Trend Across Session")
            fig_latency = px.line(
                hist_df, 
                x=hist_df.index, 
                y="time_ms", 
                markers=True, 
                labels={"index": "Request Index", "time_ms": "Latency (ms)"},
                title="Response Time History"
            )
            st.plotly_chart(fig_latency, use_container_width=True)
            
            st.subheader("Status Code Distribution")
            fig_status = px.histogram(
                hist_df, 
                x="status", 
                color="method",
                title="HTTP Status Breakdown",
                labels={"status": "HTTP Status Code"}
            )
            st.plotly_chart(fig_status, use_container_width=True)
        else:
            st.info("Send more requests to populate analytics charts.")