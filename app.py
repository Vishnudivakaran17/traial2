from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(page_title="My webpage", page_icon=":tada:",layout="wide")
def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
local_css("style/style.css")

lottie_coding = load_lottieurl("https://lottie.host/69e2d97d-b6ea-4db5-9619-6ddf76443186/1oPPULfA9v.json")
image_clamp=Image.open("images/2.png")
image_skf=Image.open("images/1.png")

with st.container():
    st.subheader("Hi, i am Vishnu Divakaran :wave:")
    st.title ("Mechanical Engineer")
st.write("")

with st. container():
    st.write("---")
    st.header("About ME")
    left_column,right_column =st.columns((2,1))
    
    st.write("##")
    
    with left_column:
        st.write("""
             I am a Mechanical engineer with designing and fabrication skills together with critical thinking and problem
            solving abilities. I am passionate about researching plus learning new technologies and that made me
            acquire knowledge in python programing as well as its implementation in Machine learning, Data science. I
                am currently pursuing the subject Artificial Intelligence along with my work""")
    with right_column:
        st.lottie(lottie_coding, height=300, key="coding")

    with st. container():
        st.write("---")
        st.header("Projects i have been part of")
        st.write("##")
    image_column,text_column =st.columns((1,1))
    with image_column:
        st.image(image_clamp)


    with text_column:
        st.subheader (" Fabrication of  On-line Leak sealing clamps")
        st.write(
            """
            Online leak sealing is a technique used to repair leaks in pipelines or equipment while they are in operation. This is achieved by injecting a sealant material directly into the leak sealing clamp that is installed over the defected area/the leaking area, which creates a permanent seal.
            """
        )

    with st. container():
        
        st.write("##")
    image_column,text_column =st.columns((1,2))
    with image_column:
        st.image(image_skf)


    with text_column:
        st.subheader ("Lasershaft Alignment")
        st.write(
            """
            Laser shaft alignment (commonly known as coupling alignment) is the process of aligning two or more rotating shafts in a straight line.
            """
        )
        with st. container():
            st.write("---")
            st.write("###")
            st.header("Get in touch with me!")
            st.write("##")

    contact_form= """
<form action="https://formsubmit.co/vishnuivakarank@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="False">
     <input type="text" name="name" placeholder ="Your name" required>
     <input type="email" name="email" placeholder ="Your email ID"required>
     <textarea nmae="message" placeholder="your message here"required></textarea>
     <button type="submit">Send</button>
</form>

    """  

left_column,right_column =st.columns(2)
with left_column:
    st.markdown(contact_form,unsafe_allow_html=True)
with right_column:
    st.empty()