import streamlit as st
import sys
import os
from dotenv import load_dotenv, find_dotenv
sys.path.append(os.path.abspath(os.path.join('..')))
from src.recruitai import RecruitAI  # noqa: E402

# Find env vars.
load_dotenv(find_dotenv())
openai_api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title='RecruitAI')

recruit_ai = RecruitAI(openai_api_key=openai_api_key)
rad = st.sidebar.radio(
    'Browse the items',
    [
        "About RecruitAI",
        "TXT to PDF",
        "Analysis",
        "Creator"
    ]
)

if rad == 'About RecruitAI':
    st.title("Welcome to RecruitAI! :nerd_face:")
    st.markdown("""Are you ready to transform the way you find the best talent for your team? Introducing RecruitAI, a revolution in the candidate selection process!""")
    st.subheader("""What is RecruitAI?""")
    st.markdown("""RecruitAI is a powerful and innovative PDF resume analysis tool designed to simplify and streamline the candidate screening process. With cutting-edge artificial intelligence and an intuitive interface, RecruitAI lets you identify ideal candidates efficiently and accurately.""")
    st.markdown("""Explore in the following items and discovery how RecruitAI can help you! :star-struck:""")

if rad == "TXT to PDF":

    st.title("Choose the TXT file to convert to PDF")
    txt_file = st.file_uploader(
        "Choose a TXT file",
        type=['txt'],
        accept_multiple_files=False
        )

    if txt_file:
        st.markdown("""
            We know that many CVs and job descriptions are delivered in TXT
            format. Therefore, this tab is for you to be able to convert the
            TXT file to PDF. It's super easy, try it below:
            """)
        st.markdown("Click on the button below to convert the TXT file to PDF")
        txt_str = txt_file.read()

        if st.button("Convert"):
            pdf_bytes = recruit_ai.text2pdf(
                txt_content=txt_str
                )

            st.success("File converted successfully!")
            name_pdf = txt_file.name.split(".")[0] + ".pdf"

            st.download_button(
                label="Click to download the pdf file",
                data=pdf_bytes,
                file_name=name_pdf,
                key="pdf"
                )

    else:
        st.warning("Please, choose a TXT file")

if rad == "Analysis":
    st.markdown("""Below, choose a job description and a curriculum file,
                respectively, to see how RecruitAI works.
                """)

    col1, col2 = st.columns(2)

    with col1:
        job_description = st.file_uploader(
            "Choose a job description file",
            type=['pdf'],
            accept_multiple_files=False
            )

    with col2:
        curriculum = st.file_uploader(
            "Choose a curriculum file",
            type=['pdf'],
            accept_multiple_files=False
            )

    if job_description and curriculum:
        job_description_str = recruit_ai.get_text_from_pdf(job_description)
        curriculum_str = recruit_ai.get_text_from_pdf(curriculum)
        analyze = st.button("Analyze")
        st.markdown("Below, you can see the analysis of the curriculum file.")
        st.markdown("The analysis is based on the job description file.")

        if analyze:

            messages = recruit_ai.get_prompt(
                requirements=job_description_str,
                curriculum=curriculum_str
                )

            response = recruit_ai.llm(messages)
            response_pdf = recruit_ai.text2pdf(txt_content=response.content)
            st.download_button(
                        label="Click to download the pdf file",
                        data=response_pdf,
                        file_name="results.pdf",
                        key="pdf"
                        )


if rad == "Creator":
    st.title("Creator: Ramon Medeiro")
    st.markdown("""Hi! I'm Ramon Medeiro, a Data Scientist. I'm a passionate about technology and I love to create new things.""") 
    st.markdown("""I'm always looking for new challenges and i'm creating this project to help people understand how to insert GenAI in different fields of application.""")
    st.markdown("""I created this project also with the intention of participating in the streamlit hackathon about LLMs.""")
    st.markdown("""If you want to know more about me, please visit my [LinkedIn](https://www.linkedin.com/in/ramon-medeiro-767722246/) or my [GitHub](https://github.com/ramoonmedeiro).""")
