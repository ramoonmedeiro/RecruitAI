import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join('..')))
from src.utils import get_text_from_pdf, txt2pdf  # noqa: E402

st.set_page_config(page_title='RecruitAI')

rad = st.sidebar.radio('Browse the items', ['About RecruitAI', 'TXT to PDF', 'Analysis', "Creator"])

if rad == 'About RecruitAI':
    st.title("Welcome to RecruitAI! :nerd_face:")
    st.markdown("""Are you ready to transform the way you find the best talent for your team? Introducing RecruitAI, a revolution in the candidate selection process!""")
    st.title("""What is RecruitAI?""")
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
        st.markdown("Click on the button below to convert the TXT file to PDF")
        txt_str = txt_file.getvalue().decode("utf-8")

        if st.button("Convert"):
            st.markdown(txt_str)
            pdf_output = txt2pdf(
                txt_content=txt_str,
                output_pdf_path=txt_file.name
                )

            st.success("File converted successfully!")

            st.download_button(
                label="Clique aqui para baixar o PDF",
                data=txt_file.name,
                key="download_button",
                args={'key': 'value'},
                help="Clique para baixar o PDF",
                            )

if rad == "Analysis":
    st.markdown("Below, choose a job description and a curriculum file, respectively, to see how RecruitAI works.")

    job_description = st.file_uploader(
        "Choose a job description file",
        type=['pdf', 'txt'],
        accept_multiple_files=False
        )

    curriculum = st.file_uploader(
        "Choose a curriculum file",
        type=['pdf', 'txt'],
        accept_multiple_files=False
        )

    if curriculum is not None and job_description is not None:

        if curriculum.name.split(".")[-1] == 'pdf':
            curriculum_text = get_text_from_pdf(curriculum)

        if job_description.name.split(".")[-1] == 'pdf':
            job_description_text = get_text_from_pdf(job_description)

        if curriculum.name.split(".")[-1] == 'txt':
            pass

        if job_description.name.split(".")[-1] == 'txt':
            pass


if rad == "Creator":
    st.title("Creator: Ramon Medeiro")
    st.markdown("""Hi! I'm Ramon Medeiro, a Data Scientist. I'm a passionate about technology and I love to create new things.""") 
    st.markdown("""I'm always looking for new challenges and i'm creating this project to help people understand how to insert GenAI in different fields of application.""")
    st.markdown("""I created this project also with the intention of participating in the streamlit hackathon about LLMs.""")
    st.markdown("""If you want to know more about me, please visit my [LinkedIn](https://www.linkedin.com/in/ramon-medeiro-767722246/) or my [GitHub](https://github.com/ramoonmedeiro).""")