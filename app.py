import faiss
import pickle
import pandas as pd
import streamlit as st
from sentence_transformers import SentenceTransformer
from vector_engine.utils import vector_search

ui_data = []

@st.cache
def read_data(data="vt_corpus.csv"):
    """Read the data from local."""
    return pd.read_csv(data)


@st.cache(allow_output_mutation=True)
def load_bert_model(name="distilbert-base-nli-stsb-mean-tokens"):
    """Instantiate a sentence-level DistilBERT model."""
    return SentenceTransformer(name)


@st.cache(allow_output_mutation=True)
def load_faiss_index(path_to_faiss="faiss_index.pickle"):
    """Load and deserialize the Faiss index."""
    with open(path_to_faiss, "rb") as h:
        data = pickle.load(h)
    return faiss.deserialize_index(data)



def main(query):
    # Load data and models
    global ui_data
    ui_data.clear()
    data = read_data()
    model = load_bert_model()
    faiss_index = load_faiss_index()

    st.title("Vector-based searches with Sentence Transformers and Faiss")

    # User search
    user_input = st.text_area("Search box", query)

    # Filters
    st.sidebar.markdown("**Filters**")
    filter_year = st.sidebar.slider("Publication year", 2010, 2021, (2010, 2021), 1)
    filter_citations = st.sidebar.slider("Citations", 0, 250, 0)
    num_results = st.sidebar.slider("Number of search results", 10, 50, 10)

    # Fetch results
    if user_input:
        D, I = vector_search([user_input], model, faiss_index, num_results)
        for id_ in I.flatten().tolist():
            if id_ in set(data.id):
                f = data[(data.id == id_)]
                ui_data.append(f.to_json(orient="records"))
                print("-------------", ui_data)
            else:
                continue

            st.write(
                f"""**{f.iloc[0].Title}**  
            **Abstract**
            {f.iloc[0].Content}
            """
            )
        print("-------------", ui_data)

def get_ui_data():
    global ui_data
    return ui_data

if __name__ == "__main__":
    main()
    #streamlit run app.py
