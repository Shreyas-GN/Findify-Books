import streamlit as st
from googlesearch import search

# Function to perform Google search
def find_books(query):
    search_query = f'intext:"{query}" filetype:pdf OR filetype:epub OR filetype:mobi'
    results = search(search_query, num_results=15)
    return results

# Streamlit page configuration
st.set_page_config(page_title="FindifyBooks", page_icon="📚", layout="centered")

# Set custom colors
primary_color = "#3399FF"  # Green
secondary_color = "#246BCE"  # Celtic Blue
title_color = "#2B7A78"  # Teal
subheading_color = "#FFFFFF"  # White
paragraph_color = "#FFFFFF"  # White for the paragraph

# Set Streamlit styles
st.markdown(
    f"""
    <style>
    .stButton>button {{
        background-color: {primary_color};
        color: white;
        font-size: 18px;
        padding: 12px;
        border-radius: 8px;
        border: none;
        width: 100%;
        cursor: pointer;
    }}
    .stButton>button:hover {{
        background-color: {secondary_color};
    }}
    .stTitle {{
        color: {title_color};
    }}
    .stTextInput {{
        border-color: {primary_color};
    }}
    .subheading {{
        color: {subheading_color};
        font-size: 18px;
        font-weight: normal;
    }}
    .paragraph {{
        color: {paragraph_color};
        font-size: 14px;
        text-align: center;
        margin-top: 30px;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Set page title and subheading with custom colors
st.markdown(f"<h1 style='color:#3399FF;'>FindifyBooks 📚</h1>", unsafe_allow_html=True)
st.markdown(f"<h2 class='subheading'>Find Free Books Instantly!</h2>", unsafe_allow_html=True)

# Input field for book search
book_query = st.text_input("Enter the book title you want to search for:")

# Search button
if st.button("Search Books"):
    if book_query:
        with st.spinner("Searching for free books..."):
            search_results = find_books(book_query)
            
            if search_results:
                st.subheader("Found books:")
                for i, result in enumerate(search_results, 1):
                    st.write(f"{i}. [{result}]( {result} )")
            else:
                st.error("No results found.")
    else:
        st.error("Please enter a book title to search.")

# Custom paragraph text with details about FindifyBooks in white
paragraph_text = """
Made with ❤️ by Shreyas GN

At FindifyBooks, I believe knowledge should be free for everyone. Our tool helps students, researchers, and readers 
easily find free book resources—textbooks, academic papers, and novels.

With our user-friendly interface, discover a world of literature across various genres.

Explore and Enrich Your Mind with FindifyBooks!

© 2024 FindifyBooks. All rights reserved.
"""
st.markdown(f'<div class="paragraph">{paragraph_text}</div>', unsafe_allow_html=True)
