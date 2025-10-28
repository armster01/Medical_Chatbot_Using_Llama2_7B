from langchain_core.prompts import PromptTemplate

prompt_template = """

use the following piece of information to answer the user's question.

If you don't know the answer, just say that you don't know, don't try to make up the answer.





Context: {context}

Question: {question}



Only return the helpful answer below and nothing else.

Helpful answer:

"""

PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])