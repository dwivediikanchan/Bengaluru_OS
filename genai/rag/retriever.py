from genai.rag.vector_store import create_store



def get_retriever(documents):


    db = create_store(

        documents

    )


    return db.as_retriever()