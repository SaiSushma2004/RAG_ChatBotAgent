🤖 RAG Chatbot – Cloud Deployed Generative AI Application
📌 Project Overview

This project is a Retrieval-Augmented Generation (RAG) based Chatbot that allows users to ask questions from their own documents.
It combines document retrieval with LLM-based answer generation to provide accurate, context-aware responses.
The application is built using Python, LangChain, Vector Databases, and deployed as a web application using Streamlit Cloud.

🧠 Key Features

Upload and query documents using RAG architecture
Uses vector embeddings for semantic search
Context-aware answers generated using an LLM
Displays source documents for transparency
Simple and interactive Streamlit UI
Fully cloud deployed and publicly accessible

🏗️ Tech Stack

Language: Python
Framework: Streamlit
LLM Orchestration: LangChain
Vector Store: FAISS / Chroma (as used in project)
Embeddings: OpenAI / HuggingFace (based on your implementation)

Deployment Platform: Streamlit Cloud
☁️ Cloud Deployment Details
🔹 Cloud Platform Used

Streamlit Cloud
🔗 https://streamlit.io/cloud

🔹 Why I Chose Streamlit Cloud

I chose Streamlit Cloud because it is:
Specifically optimized for ML & GenAI applications
Extremely easy to deploy Python-based apps
Free tier available for student & learning projects
Direct integration with GitHub repositories
No DevOps or server management required
This makes it ideal for deploying RAG, LLM, and AI demo applications quickly.

🚀 Deployment Process (Step-by-Step)

Prepare the Project
Ensure app.py is the entry file
Add requirements.txt
Keep secrets (API keys) outside the code

Push Code to GitHub

git add .
git commit -m "Deploy RAG Chatbot"
git push origin main

Create Streamlit Cloud App
Go to: https://share.streamlit.io
Click New App
Select GitHub repository
Choose:
Branch: main
File path: frontend/app.py
Add Secrets (if required)
In Streamlit Cloud → App Settings → Secrets
Add API keys securely

Deploy
Click Deploy

App builds automatically and becomes live 🎉

🌐 Live Application Link

🔗 RAG Chatbot (Streamlit Cloud):
https://ragchatbotagent-faxidgsxcv5rxznkcp7q.streamlit.app

👍 Pros of Streamlit Cloud

✅ Free and fast deployment
✅ Perfect for AI / ML / GenAI demos
✅ GitHub integration
✅ Automatic rebuilds on code changes
✅ Secure secrets management
✅ No infrastructure setup needed

⚠️ Cons of Streamlit Cloud

❌ Limited resources on free tier
❌ Not ideal for high-traffic production apps
❌ Cold start delays sometimes
❌ Less customization compared to AWS/GCP/Azure

🎯 Use Cases

Generative AI demos
RAG-based document assistants
AI interview/showcase projects
Learning and experimentation with LLMs

🔮 Future Enhancements

Multi-document upload support
Chat history persistence
Authentication
Deployment on AWS / GCP
Model switching support

🙌 Conclusion

This project demonstrates end-to-end development and cloud deployment of a Generative AI RAG system, showcasing practical skills in LLMs, retrieval systems, and cloud deployment.

👩‍💻 Author

M.Sai Sushma 
B.Tech CSE (AI & ML)
AI | Machine Learning | Cloud Deployment
🔗 LinkedIn: https://www.linkedin.com/in/sai-sushma-maruboyina-382b34334?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app
