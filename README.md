# Mini-ZBot

## Description

A brief description of your project, including its purpose and key features.

## Installation

1. Clone the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Set up any necessary environment variables.

## Usage

1. Run the application using `python main.py`.
2. Interact with the application by providing input or using the available tools.

## Agents

### RouterAgent

#### Description

An agent that determines which Qdrant collection to search based on the user's question.

#### Instructions

1. Use the `list_qdrant_collections` tool to see what collections are available.
2. Based on the question topic, choose the most relevant collection.
3. Return ONLY the collection name as a single word/phrase, nothing else.

#### Collection Selection Guidelines

- If unsure, list the collections and pick the one that seems most relevant.

#### Example Response

```
yizumi-electrical-docs
```

### RetrievalAgent

#### Description

An agent that retrieves information from Qdrant or web search based on user queries.

#### Instructions

1. Use the `qdrant_search_tool` tool to search for relevant information in a specific Qdrant collection.
2. If Qdrant search fails, you can fallback to `web_search_tool`.

#### Example Response

```
[
  {
    "content": "Relevant document content 1",
    ...
  },
  {
    "content": "Relevant document content 2",
    ...
  },
  ...
]
```

### GeneratingAgent

#### Description

An agent that generates information from Qdrant or web search based on user queries.

#### Instructions

1. Use the `qdrant_search_tool` tool to search for relevant information in a specific Qdrant collection.
2. If Qdrant search fails, you can fallback to `web_search_tool`.
3. Use the retrieved information to generate a response.

#### Example Response

```
Generated response based on retrieved information.
```

---

Feel free to customize this template to fit your project's specific details and structure.