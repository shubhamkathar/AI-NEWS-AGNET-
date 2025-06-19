Project Overview:
This project is an AI-powered research assistant that automates the process of gathering and summarizing the latest information on any topic provided by the user. The user inputs a topic through a Streamlit frontend. This request is sent to a Flask backend API which uses a CrewAI multi-agent system. The agents use tools like Serper and BeautifulSoup to search for the latest web content and summarize the findings into a markdown report. The report is displayed on the frontend in a clean and readable format.

![image alt](https://github.com/shubhamkathar/AI-NEWS-AGNET-/blob/e0e046d3d24f3f57ff2e9b09cff57f74fb12ef47/Screenshot%202025-06-19%20200930.png)

Architecture Flow:

The user enters a topic in the Streamlit UI.

The frontend sends a POST request with the topic to the Flask backend at the /research endpoint.

Flask receives the topic and date, then triggers the CrewAI workflow.

Inside the CrewAI flow:

The Researcher agent searches the web using Serper and ScrapeWebsiteTool.

The Reporting Analyst agent summarizes the findings into a paragraph and bullet points.

The output is saved in a markdown file (report.md).

Flask reads this file and sends it back as a JSON response.

The Streamlit frontend receives the JSON and displays the formatted markdown report.

Setup and Installation Instructions:

Create a folder for the project and place all code files inside it.

Open terminal or command prompt and navigate to the project folder.

Create a virtual environment:

python -m venv venv

Activate the virtual environment:

For Windows: venv\Scripts\activate

For macOS/Linux: source venv/bin/activate

Install all dependencies:

pip install -r requirements.txt

Set up environment variables:

Create a .env file in the root folder.

Add your API keys like this:
SERPER_API_KEY=your_key
NVIDIA_API_KEY=your_key

Start the Flask backend:

python app.py

In another terminal, start the Streamlit frontend:

streamlit run frontend.py

Open browser at http://localhost:8501 and test the application.

![image alt](https://github.com/shubhamkathar/AI-NEWS-AGNET-/blob/a19ba37db75e2576fb21b0cd0601a1d1d61a91d4/Streamlit%20to%20AI%20Report%20Generation%20Flowchart.jpg)

Design Choices and Trade-offs:

I chose Serper.dev as the web search tool because it offers a reliable and developer-friendly API for accessing Google search results, and has a free tier that works well for prototyping.

For summarization and agent orchestration, I used CrewAI because it provides a simple yet powerful way to define AI agents with different roles and tools.

The Flask framework was selected for the backend because of its lightweight nature and my prior experience with it.

Streamlit was used for the frontend because it allows for quick development of interactive web applications with minimal boilerplate.

One challenge was handling the output from CrewAI, which by default returns objects that are not JSON serializable. To resolve this, I focused on returning only the markdown content from the report.md file.

Another challenge was coordinating the timing between agent task completion and reading the final report. I ensured the backend waits for the report file before returning a response.

flowchart TD
    A --> [User enters topic in Streamlit UI] --> B[POST request to Flask API /research]
    B --> C[Flask receives topic & date]
    C --> D[Call Reseach_crew().crew().kickoff()]
    D --> E[Agent 1: Researcher uses Serper + Web Scraping]
    E --> F[Agent 2: Reporting Analyst synthesizes summary + key points]
    F --> G[Write output to report.md]
    G --> H[Flask reads report.md content]
    H --> I[Flask sends JSON with report to Streamlit]
    I --> J[Streamlit displays report using st.markdown()]

