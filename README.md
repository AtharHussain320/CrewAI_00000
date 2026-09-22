# Generic CrewAI Gemini Q&A

A simple and general-purpose AI Question & Answer application built with **Python, CrewAI, Google Gemini, and Streamlit**.

The application allows users to ask questions on any general topic through a clean chat interface. **Streamlit** provides the frontend, **CrewAI** manages the AI workflow, and **Google Gemini** works as the Large Language Model.

## Features

- General-purpose AI Question & Answer
- Ask questions on any topic
- Google Gemini LLM integration
- CrewAI agent-based backend
- Streamlit chat-based frontend
- Dynamic user questions
- Conversation interface
- Simple and clean user experience
- Python-based application
- Secure API key configuration using `.env`
- Configurable Gemini model
- Easy to understand and maintain
- Easy to deploy
- No hard-coded questions or answers

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| CrewAI | Backend AI framework and agent orchestration |
| Google Gemini | Large Language Model |
| Streamlit | Frontend and user interface |
| python-dotenv | Environment variable management |
| `.env` | Secure API key and configuration storage |

## Application Architecture

```text
User
  |
  v
Streamlit Frontend
  |
  v
CrewAI Backend
  |
  v
CrewAI Agent
  |
  v
Gemini LLM
  |
  v
Generated Answer
  |
  v
Streamlit Frontend
