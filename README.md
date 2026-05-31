# BlogAgentic

An AI-powered blog generation application built using FastAPI, LangGraph, LangChain, and Groq LLMs. The application exposes a REST API that generates blog content from a user-provided topic through a LangGraph workflow.

---

## Features

* FastAPI-based REST API
* LangGraph workflow orchestration
* Groq-powered LLM integration
* LangSmith tracing support
* Pydantic request validation
* Environment-based configuration
* Production-ready project structure

---

## Tech Stack

* Python 3.12+
* FastAPI
* Uvicorn
* LangGraph
* LangChain
* Groq
* LangSmith
* Pydantic
* python-dotenv
* uv

---

## Project Structure

```text
BlogAgentic/
│
├── src/
│   ├── graphs/
│   │   └── graph_builder.py
│   │
│   ├── llms/
│   │   └── groqllm.py
│   │
│   ├── schema/
│   │   └── blog_request.py
│   │
│   └── ...
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
└── pyproject.toml
```

---

## Installation

### Clone the Repository

```bash
git clone <your-repository-url>
cd BlogAgentic
```

### Create Virtual Environment

Using uv:

```bash
uv venv
```

Activate the environment:

**Windows**

```bash
.venv\Scripts\activate
```

**Linux/macOS**

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
uv add -r requirements.txt --link-mode=copy
```

or

```bash
uv sync --link-mode=copy
```

---

## Environment Variables

Create a `.env` file in the project root:

```env
LANGCHAIN_API_KEY=your_langsmith_api_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=BlogAgentic

GROQ_API_KEY=your_groq_api_key
```

---

## Running the Application

Start the FastAPI server:

```bash
python app.py
```

The application will be available at:

```text
http://localhost:8000
```

Swagger UI:

```text
http://localhost:8000/docs
```

---

## API Usage

### Generate Blog

**Endpoint**

```http
POST /blogs
```

**Request Body**

```json
{
  "topic": "Applications of Generative AI in Healthcare"
}
```

**Response**

```json
{
  "data": {
    "topic": "Applications of Generative AI in Healthcare",
    "blog": "Generated blog content..."
  }
}
```

---

## LangSmith Integration

To enable tracing:

```env
LANGCHAIN_API_KEY=your_langsmith_api_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=BlogAgentic
```

After enabling tracing, all LangGraph executions can be monitored through the LangSmith dashboard.

---

## Future Improvements

* Multi-agent workflows
* Blog review and refinement agents
* SEO optimization
* Human-in-the-loop approval
* Database integration
* Docker deployment
* CI/CD pipelines
* Authentication and authorization

---

## Author

Shahreyar Hossain

---

## License

This project is intended for educational and learning purposes.
