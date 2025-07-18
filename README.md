📄 Resume Screening Bot using NLP & Machine Learning
A smart Resume Screening Bot that uses NLP and a machine learning model to automatically parse resumes, extract relevant skills, and match candidates to a given job description based on similarity scores.

✅ Built with Python, Scikit-learn, Streamlit, and NLP libraries
📥 Upload resumes (PDF, DOCX, or TXT) and get real-time compatibility scores.

🚀 Features
📄 Parse resumes in .pdf, .docx, and .txt formats

🧠 Extract skills and keywords using NLP (e.g., spaCy, docx2txt)

🎯 Compare with job description using cosine similarity

📊 Show candidate match score with explanation

🌐 Easy-to-use Streamlit web app interface

🛠️ Tech Stack
Frontend: Streamlit

Backend: Python, NLP (spaCy, PyPDF2, docx2txt)

ML: TF-IDF, Cosine Similarity

Deployment-ready: Modular structure for Heroku / HuggingFace / Streamlit Cloud


⚙️ How to Run the Project Locally

1. Clone this repository
   
git clone https://github.com/ZULFIQARAHMED27/Resume-Screener-Bot.git
cd Resume-Screener-Bot

2. Create and activate a virtual environment

python -m venv venv
.\venv\Scripts\activate   # On Windows

3. Install dependencies
   
pip install -r requirements.txt

4. Run the app

streamlit run app.py

5. Upload your resume and paste the job description to see your matching score.


