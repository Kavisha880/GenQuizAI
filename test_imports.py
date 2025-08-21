try:
    import openai
    import langchain
    import streamlit
    import PyPDF2
    import dotenv

    print("✅ All required packages are installed and working!")
except Exception as e:
    print("❌ Import failed:", e)
