import streamlit as st
from PIL import Image
import qrcode


st.header('ITAM Newsletter for Finance and More')

image = Image.open('ITAM_pic.png')

st.image(image, width=600)

st.subheader('What is this?')

st.markdown("""This is a small student newspaper focused on news from the world of finance and beyond.
For our readers we hope to provide information, maybe even stimulation, or just some time savings if they need to catch up on what has been going on.""")

st.subheader('How to use it?')

st.markdown("""On the left you can find the sidebar. 
With it, you can navigate through the news for different weeks, as well as the headings within the news.""")

st.subheader('Who we are?')

st.markdown("""We are a team of ITAM students who are fond of finance. We are writing this paper under the wise 
supervision of ITAM Professor Mathias Josef Schneider. Every week, several people from our group take on the role of editors. 
You can find out who was the editor of the issue you are reading at the bottom of each news page.""")

st.subheader('Where we get our news from?')

st.markdown("""Each of us selects the news that seems most interesting from our own favorite sources.
 Then, at a general meeting, we select the most relevant and credible news, which gets into the final 
 version of the newspaper. Sources are quoted at the end of every news.""")

st.subheader('How to contact us?')

st.markdown("""We will be grateful for any feedback. If you have any criticism of our newspaper or suggestions on how
 we can improve our content, please write to Mathias Josef Schneider (mathias.schneider@itam.mx). Also, if you notice a 
 typo, fake news or content that is offensive to you, then write to the administrator of the online page on email eakhmadu@itam.mx 
 and we will immediately fix the problem found.""")

st.subheader('*SHARE WITH YOUR FRIENDS*')

link = 'https://itamita-newsletter-welcome-page-5jp2re.streamlitapp.com/'

st.write('Share this page using this link: '+ link+ ", or using the QR-code:")

img = qrcode.make(link)

st.image(img)

