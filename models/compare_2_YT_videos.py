import streamlit as st
from openai import OpenAI
from youtube_transcript_api import YouTubeTranscriptApi
import sys

def get_captions(video_url):
    try:
        video_id = video_url.split("v=")[1]
        captions = YouTubeTranscriptApi.get_transcript(video_id)
        return captions
    except Exception as e:
        print(f"Error: {e}")
        return None

client = OpenAI(api_key="")

def ask_gpt3(prompt, context1, context2):
    # Use GPT-3 to generate an answer
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"{context1}\n{prompt}"},
            {"role": "assistant", "content": f"{context2}"}
        ],
    )
    return response.choices[0].message.content

def main():
    st.title("Comparing 2 YT videos")

    # User input -1 
    uploaded_video_1 = st.text_area("Upload your video 1 ID here:", "")
    captions1 = get_captions(uploaded_video_1)
    
    # User input -2 
    uploaded_video_2 = st.text_area("Upload your video 2 ID here:", "")
    captions2 = get_captions(uploaded_video_2)

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
                
                result = ask_gpt3(prompt=question, context1=captions1, context2=captions2)

                # Display the result
                result_placeholder.subheader("Answer:")
                result_placeholder.write(result)
            else:
                result_placeholder.warning("Please enter a question.")

        # Update the checkbox state
        ask_question = st.checkbox("Ask Question", key="ask_question_checkbox")

if __name__ == "__main__":
    main()
