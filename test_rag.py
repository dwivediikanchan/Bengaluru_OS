from genai.context import load_city_documents


docs = load_city_documents()


print(len(docs))


print(docs[0])