import google.generativeai as genai

# Configure API
genai.configure(api_key="AIzaSyA1Z8PlzWolq2cQu-5W-IgC3IAfqw8KXyc")

# Use a lightweight model
model = genai.GenerativeModel("models/gemini-flash-lite-latest")


def ask_agent(question, data):

    prompt = f"""
You are a Business Intelligence Analyst.

Below is a dataset extracted from Monday.com.

DATA:
{data}

QUESTION:
{question}

Provide clear insights based only on the data.
Keep the answer short and structured.
"""

    try:
        response = model.generate_content(prompt)

        if response.text:
            return response.text
        else:
            return "No response generated."

    except Exception as e:
        return f"AI Error: {str(e)}"