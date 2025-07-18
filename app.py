import streamlit as st
from resume_parser import extract_text_from_file
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os
import pandas as pd

st.title("🧠 Resume Screening Bot")
st.markdown("Upload a job description and rank resumes from the folder based on relevance.")

jd_text = st.text_area("Paste the Job Description Here")

if st.button("Rank Resumes") and jd_text:
    resumes = []
    names = []

    for file in os.listdir("resumes"):
        if file.endswith(".pdf") or file.endswith(".docx"):
            path = os.path.join("resumes", file)
            content = extract_text_from_file(path)
            resumes.append(content)
            names.append(file)

    if len(resumes) == 0:
        st.warning("No resumes found in the 'resumes' folder.")
    else:
        all_text = [jd_text] + resumes
        tfidf = TfidfVectorizer(stop_words='english')
        vectors = tfidf.fit_transform(all_text)
        scores = cosine_similarity(vectors[0:1], vectors[1:]).flatten()

        results = pd.DataFrame({'Resume': names, 'Score': scores})
        results = results.sort_values(by='Score', ascending=False).reset_index(drop=True)

        st.success("Ranking complete!")
        st.dataframe(results)

        results.to_csv("ranked_results.csv", index=False)
        st.download_button("📥 Download CSV", data=open("ranked_results.csv", "rb").read(), file_name="ranked_results.csv")
