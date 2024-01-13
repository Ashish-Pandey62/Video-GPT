import streamlit as st
import sys
from  openai import OpenAI
import os




client = OpenAI(api_key="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")


def ask_gpt3(prompt, context):
    # Use GPT-3 to generate an answer
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"{context}\n{prompt}"},
        ],
    )
    # return response["choices"][0].message["content"].strip()
    return response.choices[0].message.content
def main():
    st.title("Question Answering with Youtube Videos")

    # User input
    uploaded_text = st.text_area("Upload your text here:", "")

    # Display a placeholder for the text and questions
    result_placeholder = st.empty()

    # Checkbox to control the loop with a unique key
    ask_question = st.checkbox("Ask Question", key="ask_question_checkbox")

    # Allow the user to ask questions until they uncheck the checkbox
    while ask_question:
        question = st.text_input("Enter your question:")

        # Display a spinner during inference
        with st.spinner("Analyzing..."):
            if question:
                # Run GPT-3 for question-answering
                result = ask_gpt3(prompt=question, context=uploaded_text)

                # Display the result
                result_placeholder.subheader("Answer:")
                result_placeholder.write(result)
            else:
                result_placeholder.warning("Please enter a question.")

        # Update the checkbox state
        ask_question = st.checkbox("Ask Question", key="ask_question_checkbox")

if __name__ == "__main__":
    main()
