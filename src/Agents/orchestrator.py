from .retrievalAgent import retrieval_agent
from .generatingAgent import generating_agent


class Orchestrator:
    def __init__(self):
        self.retrieval_agent = retrieval_agent
        self.generation_agent = generating_agent

    def run(self, user_question: str) -> str:
        # 1️⃣ Retrieval
        retrieval_response = self.retrieval_agent.run({"query": user_question})
        context = retrieval_response.content

        # 2️⃣ Generation
        final_prompt = f"""
            Use the following retrieved information to answer the question.

            Context:
            {context}

            Question:
            {user_question}
            """
        final_response = self.generation_agent.run(final_prompt)
        return final_response.content
