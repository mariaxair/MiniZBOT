# Mini-ZBot

## Project Overview

Mini-ZBot is a multi-agent AI system designed to orchestrate complex queries through a pipeline of specialized agents. Built using the `agno` framework, it separates concerns into routing, retrieval, and generation to provide accurate and context-aware responses.

## Installation

1. Clone the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Set up environment variables (e.g., `OPENAI_API_KEY`) in a `.env` file.

## Usage

1. Run the application using `python main.py`.
2. Interact with the application by providing input or using the available tools.

## Agent Architecture

The system uses a collaborative workflow where agents communicate to resolve user requests:

1.  **RouterAgent**: Determines the domain of the query.
2.  **RetrievalAgent**: Fetches relevant data based on the domain.
3.  **GeneratingAgent**: Synthesizes the final response using the retrieved data.

### 1. RouterAgent

- **Role**: The dispatcher. It analyzes the user's question to decide which knowledge base (Qdrant collection) to query.
- **Tools**: `list_qdrant_collections`
- **Output**: The name of the relevant Qdrant collection.

### 2. RetrievalAgent

- **Role**: The researcher. It retrieves semantic context from the vector database or performs web searches if necessary.
- **Tools**:
  - `qdrant_search_tool`: For searching internal documentation.
  - `web_search_tool`: Fallback for external information.
- **Output**: A list of relevant document snippets or search results.

### 3. GeneratingAgent

- **Role**: The persona and writer. It generates the final answer for the user.
- **Current Configuration**: **Book Recommendation Assistant**.
  - Specializes in literature, themes, characters, and author insights.
  - Maintains a friendly and passionate tone about books.
- **Tools**: `web_search_tool` (used to supplement provided context).
- **Communication**: Receives context from the RetrievalAgent and instructions to base answers on that context.

## Detailed Agent Specifications

### RouterAgent

- **Instruction**: Return ONLY the collection name as a single word/phrase.
- **Fallback**: If unsure, list collections and pick the most relevant one.

### RetrievalAgent

- **Instruction**: Prioritize Qdrant search; fallback to web search if needed.
- **Output Format**: JSON-like list of document contents.

### GeneratingAgent

- **Instruction**:
  - Discuss themes, characters, and plot elements.
  - Be enthusiastic about books.
  - If context is irrelevant, politely decline or pivot.
- **Model**: `openai:gpt-4o-mini`
