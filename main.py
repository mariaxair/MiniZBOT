from src.Agents.orchestrator import Orchestrator

orchestrator = Orchestrator()

# Just ask the question - the router will figure out the collection!
user_question = input("what's your question ? : ")

response = orchestrator.run(user_question)

print("\n" + "="*50)
print("Answer:")
print("="*50)
print(response)