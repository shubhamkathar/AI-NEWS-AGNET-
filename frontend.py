import streamlit as st
import requests

st.set_page_config(page_title="AI Research Assistant", page_icon="🔍")
st.title("🤖 AI Research Assistant")

# Input field for the topic
topic = st.text_input("Enter a topic to research", "")

# Button to trigger research
if st.button("Run Research"):
    if topic.strip() == "":
        st.warning("Please enter a topic before running.")
    else:
        with st.spinner("Contacting AI Agents and generating report..."):
            try:
                # Send POST request to Flask backend
                response = requests.post(
                    "http://127.0.0.1:5000/research",
                    json={"topic": topic}
                )

                # Handle response
                if response.status_code == 200:
                    data = response.json()
                    report = data.get("report", "")

                    st.success("✅ Research completed!")
                    st.markdown("### 📄 Research Report")
                    st.markdown(report, unsafe_allow_html=True)

                else:
                    error_msg = response.json().get("error", "Unknown error.")
                    st.error(f"🚫 Error from backend: {error_msg}")

            except requests.exceptions.RequestException as e:
                st.error(f"🚫 Could not reach backend: {e}")
