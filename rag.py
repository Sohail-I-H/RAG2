import os
import pandas as pd

from langchain_core.documents import Document

from langchain_community.document_loaders import PyPDFLoader

from langchain_community.vectorstores import FAISS

from config import (
    FAQ_FILE,
    embeddings,
    PERSONAS,
    CHAT_MODEL,
    groq_client
)

# ==========================================================
# VECTOR STORE
# ==========================================================

vectorstore = None


# ==========================================================
# LOAD DOCUMENTS
# ==========================================================

def load_documents(uploaded_files=None):

    global vectorstore

    docs = []

    if uploaded_files:

        for file_path in uploaded_files:

            extension = os.path.splitext(file_path)[1].lower()

            if extension == ".pdf":

                loader = PyPDFLoader(file_path)

                docs.extend(loader.load())

            elif extension in [".xlsx", ".xls"]:

                df = pd.read_excel(file_path)

                for _, row in df.iterrows():

                    docs.append(

                        Document(

                            page_content=" | ".join(

                                [

                                    f"{c}: {v}"

                                    for c, v in row.items()

                                ]

                            ),

                            metadata={

                                "source": os.path.basename(file_path)

                            }

                        )

                    )

    if os.path.exists(FAQ_FILE):

        df = pd.read_excel(FAQ_FILE)

        for _, row in df.iterrows():

            docs.append(

                Document(

                    page_content=" | ".join(

                        [

                            f"{c}: {v}"

                            for c, v in row.items()

                        ]

                    ),

                    metadata={

                        "source": FAQ_FILE

                    }

                )

            )

    vectorstore = FAISS.from_documents(

        docs,

        embeddings

    )

    return len(docs)


# ==========================================================
# RETRIEVE CONTEXT
# ==========================================================

def retrieve_context(question):

    retriever = vectorstore.as_retriever(

        search_kwargs={

            "k": 4

        }

    )

    docs = retriever.invoke(question)

    return "\n\n".join(

        [

            d.page_content

            for d in docs

        ]

    )


# ==========================================================
# CHAT COMPLETION
# ==========================================================

def generate_response(

    question,

    persona,

    language,

    history

):

    context = retrieve_context(question)

    system_prompt = f"""

{PERSONAS[persona]["prompt"]}

===================================================

Retrieved Context

{context}

===================================================

IMPORTANT

Answer ONLY in {language}.

Never answer outside the retrieved context.

If the answer is unavailable,

say you don't know.

"""

    messages = [

        {

            "role":"system",

            "content":system_prompt

        }

    ]

    messages.extend(history)

    messages.append(

        {

            "role":"user",

            "content":question

        }

    )

    completion = groq_client.chat.completions.create(

        model=CHAT_MODEL,

        messages=messages,

        temperature=0.3

    )

    return completion.choices[0].message.content
