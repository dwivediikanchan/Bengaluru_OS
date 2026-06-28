from langchain_community.vectorstores import Chroma


from genai.rag.embeddings import get_embeddings




def create_store(documents):


    embeddings = get_embeddings()



    db = Chroma.from_documents(

        documents,

        embeddings

    )



    return db