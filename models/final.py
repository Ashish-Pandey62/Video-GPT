import streamlit as st
from qna import main as qna_video
from compare import main as compare_videos

def main():
    st.sidebar.title("Navigation")
    page_options = ["QNA with YT Videos", "Compare 2 YT Videos"]
    selected_page = st.sidebar.radio("Go to", page_options)

    if selected_page == "QNA with YT Videos":
        qna_video()
    elif selected_page == "Compare 2 YT Videos":
        compare_videos()
    

if __name__ == "__main__":
    main()
