from src.Agents.orchestrator import Orchestrator
from src.tools.qdrant_search_tool import set_collection_name, _CURRENT_COLLECTION

orchestrator = Orchestrator()

# ask user for input
user_question = input("what's your question ? : ")
collection_name = input("which collection to use ? : ")
try:
    set_collection_name(collection_name)
    print(f"DEBUG: _CURRENT_COLLECTION is now: {_CURRENT_COLLECTION}")
except Exception as e:
    print(f"An error occurred: {e}")

# Pass both parameters separately
response = orchestrator.run(user_question)

print("\nAnswer:")
print(response)