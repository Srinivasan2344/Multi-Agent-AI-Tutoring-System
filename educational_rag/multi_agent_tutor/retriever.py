from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def retrieve_context(query):
    loader = PyPDFLoader("../data/sample.pdf")
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(docs)

    for chunk in chunks:
        if any(word.lower() in chunk.page_content.lower()
               for word in query.split()):
            return chunk.page_content

    return "No relevant educational content found."