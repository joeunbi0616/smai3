import streamlit as st

from MyLLM import save_uploadedfile

# Sidebar
st.sidebar.markdown("Clicked Page 6")

# Page
st.title("Page 6 File Upload")
menu = st.selectbox("파일 타입 선택:", ["IMAGE","PDF","CSV"] )

if menu == "IMAGE":
    st.subheader(menu)
    file = st.file_uploader("이미지를 선택", type=["jpg","png","jpeg"])
    if file:
        save_uploadedfile("img", file, st)
        st.download_button(
            label="파일다운로드",
            data=file,
            file_name=file.name,
            mime="image/jpg"
        )
elif menu == "PDF":
    st.subheader(menu)
    file = st.file_uploader("PFD를 선택", type=["pdf"])
    if file:
        save_uploadedfile("pdf", file, st)
        st.download_button(
            label="파일다운로드",
            data=file,
            file_name=file.name,
            mime="application/pdf"
        )
elif menu == "CSV":
    st.subheader(menu)
    file = st.file_uploader("CSV를 선택", type=["csv"])
    if file:
        save_uploadedfile("csv", file, st)
        st.download_button(
            label="파일다운로드",
            file_name=file.name,
            mime="text/text"
        )










