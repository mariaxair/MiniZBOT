from src.Agents.orchestrator import Orchestrator

orchestrator = Orchestrator()

print("="*60)
print("📚 Welcome to BookBot - Your Personal Book Assistant!")
print("="*60)
print("\nI can help you:")
print("  • Find book recommendations")
print("  • Discover books by genre")
print("  • Learn about authors and their works")
print("  • Get insights about specific books")
print("\nType 'quit' or 'exit' to leave\n")
print("="*60)

while True:
    user_question = input("\n💬 How can i help you ? ")
    
    if user_question.lower() in ['quit', 'exit', 'bye']:
        print("\n👋 Happy reading! Come back anytime!")
        break
    
    if not user_question.strip():
        print("❌ Please ask a question about books!")
        continue
    
    try:
        response = orchestrator.run(user_question)
        
        print("\n" + "="*60)
        print("📖 Here's what I found:")
        print("="*60)
        print(response)
        print("="*60)
        
    except Exception as e:
        print(f"\n❌ Oops! Something went wrong: {e}")
        print("Please try asking in a different way.")