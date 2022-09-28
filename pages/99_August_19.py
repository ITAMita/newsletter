import streamlit as st
from PIL import Image
import qrcode

st.sidebar.markdown('''
# Sections
- [NATIONAL NEWS :flag-mx:](#national-news)
- [INTERNATIONAL NEWS :earth_africa:](#international-news)
- [MARKET AND OTHER TRENDS :chart_with_upwards_trend:](#market-and-other-trends)
- [WHAT ELSE HAS BEEN GOING ON? :rainbow:](#what-else-has-been-going-on)
- [KNOWLEDGE TRANSFER AND CHALLENGE :face_with_monocle:](#knowledge-transfer-and-challenge)
- [TODAYS EDITORS](#todays-editors)
- [Share](#share)
- [Feedback](#feedback)
''', unsafe_allow_html=True)

st.header('WEEKLY NEWSLETTER 1 (PILOT), August 14-19, 2022')

st.subheader('NATIONAL NEWS :flag-mx:')

st.markdown("""
***Sunday, August 14.*** Mexico's oil company Pemex requested \$6.5 billion USD more for
the funding of the “Dos Bocas” refinery. According to documents and other sources, the
additional funding would take the refinery’s cost to \$14.6 billion USD. That is, far above
the original budget of \$8.9 billion USD. (*[Forbes](https://www.forbes.com.mx/refineria-de-dos-bocas-pide-6500-mdd-mas-al-gobierno-reuters/)*)

***Monday, August 15.*** The prices of milk and soda keep going up. Big companies such as Lala and Coca Cola announced that their prices would rise between \$.90 and \$1.90 MXN, even though just in July the prices of fresh milk and soda went up 13\% and 9\%
respectively. (*[El Financiero](https://www.elfinanciero.com.mx/economia/2022/08/14/lala-y-coca-cola-se-encarecen-cuanto-y-cuando-subiran-de-precio-sus-productos/)*)

***Tuesday, August 16.*** Even though the Afores reported capital gains above \$127 billion MXN pesos in July, the returns on Afores reported a negative balance of \$233,679 million MXN over the first seven months of the year. Nonetheless, it is expected that the gains of
July could be the start of positive returns that last until the end of the year. (*[El Financiero](https://www.elfinanciero.com.mx/economia/2022/08/15/buen-mes-para-los-godinez-afores-reportan-plusvalias-por-mas-de-127-mil-mdp-en-julio/)*)

***Wednesday, August 17.*** According to the Mexican Competitive Institute (IMCO), only about 52\% of the 3,686 state institutions which are required to inform their expenses of public resources, registered this information on the National Transparency Platform (PNT). Valeria Moy, director of IMCO and ITAM professor, explained that this could be
attributed to the lack of consequences for not complying with the law. (*[IMCO](https://imco.org.mx/wp-content/uploads/2022/08/Presentacion-compras-estatales-2022.pdf)*)

***Thursday,August18.*** The Public Accountant Association (IMCP) in Mexico is working on a tax reform initiative for 2023. The IMCP is looking for better definitions and more
clarification on some concepts. (*[IMCP](https://imcp.org.mx/reforma-fiscal-2023-imcp-hara-propuesta-para-aliviar-economia-de-los-contribuyentes/)*)

***Friday, August 19.*** The Mexican economy isn't taking off. According to INEGI, the
economy suffered a fall of 0.1\% of GDP compared to June and has only grown about
1.5\% compared to July 2021. Expectations for the following months aren’t optimistic.
(*[INEGI](https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2022/pib_eo/pib_eo2022_01.pdf)*)
""")

st.subheader('INTERNATIONAL NEWS :earth_africa:')

st.markdown("""
***Monday, August 15.*** As opposed to most western economies, China lowers its interest
rate 10 basis points to 2.75%. This measure was taken because the data about the
production of its factories and retail sector was lower than what was expected. China’s
lagging economy is the main reason for the downturn in oil prices over recent months.
(*[Diario Financiero](https://www.df.cl/internacional/economia/china-sorprende-con-una-baja-de-las-tasas-de-interes-mientras-las-cifras#:~:text=Por%3A%20Bloomberg%20%7C%20Publicado%3A%20Lunes,inmobiliaria%20cada%20vez%20m%C3%A1s%20profunda.)*)

***Tuesday, August 16.*** There is a high probability of a recession in the Eurozone where energy scarcity is driving inflation. Futures for gas at a trading hub in the Netherlands, the benchmark in northwest Europe, rose 3.2% to €233.56 a megawatt-hour, about $237. That is the highest price ever in euros, surpassing the record set on March 7, shortly after
Russia invaded Ukraine. (*Wall Street Journal August 15.*)

***Wednesday, August 17.*** Boom meme: Bed Bath & Beyond’s stock soared 300% this month. The stock price was \$5.77 USD at the beginning of the month, and today it's \$25.19. This reflects a daily rise of 21.50\%. These stock price movements create the risk of a “boom and download”, which is when investors create an artificial demand and then
sell at a high price. (*[Washington Post](https://www.washingtonpost.com/business/2022/08/19/bed-bath-beyond-stock-ryan-cohen/)*)

***Wednesday, August 17.*** The minutes of the Fed’s July 26-27 policy meeting were released. Both at the July and the June meetings rates were raised by 0.75 percentage points in an effort to control US inflation which decreased from a 40-year high of 9.1% in June to 8.5% in July. While rates might still be raised more than currently anticipated, officials acknowledged they might also run the risk of raising borrowing costs more than needed. After the meeting, Fed Fund Futures prices implied a 60% probability of a 0.50 percentage point increase versus 40% of a 0.75 percentage point increase at the next
Fed meeting in September. (*Wall Street Journal August 17.*) 
""")

st.subheader('MARKET AND OTHER TRENDS :chart_with_upwards_trend:')

st.markdown("""
***August 15***""")

img=Image.open('pics/V1P1.png')
st.image(img)

st.markdown("""There was a decline in oil prices on Monday due to discouraging economic forecasts of the USA and China, the world's largest oil importer. This prompted investors to move away from other risky assets.

As a result of the real estate crisis and the industrial and retail activity repressed by Beijing's zero COVID policy the Chinese economy has suffered a slowdown. Therefore, the Central Bank cut interest rates to revive demand.

***August 17***""")

img=Image.open('pics/V1P2.png')
st.image(img)

st.markdown("""To expand on the national news from Wednesday, August 17: the IMCO stated that it is relevant to monitor public acquisitions made by the states in order to prevent corruption. The chart above depicts the percentage of state’s governments with a register of the public acquisitions they made during 2021.
""")

st.subheader('WHAT ELSE HAS BEEN GOING ON? :rainbow:')

st.markdown("""
### T-MEC

The T-MEC is still a current topic. Following Canada’s and USA’s complaints about Mexico’s compliance with the T-MEC regarding energy policy there have been speculations what this might mean for the T-MEC. Mexico has passed laws that favor Pemex and CFE over foreign energy companies. Some worry that in a political statement about nationalism, Mexico’s president might want to withdraw from the T-MEC. However, in an editorial this week in El Financiero, Enrique Quintana mentions that he does not consider it likely that Mexico will withdraw from the T-MEC. Enrique considers that if the president hopes for his party to continue in power it is unlikely that he will cause an economic disaster in the year before the elections. Furthermore, on Wednesday August 17 Valeria Moy interviewed Juan Carlos Baker, director and founding partner of Ansley International Consultants, in her podcast *Peras y Manzanas* regarding the T-MEC and Mexico’s energy policy. Juan Carlos mentioned that he considered it unlikely that Mexico would withdraw from the T-MEC. However, he conceded that it was a possibility. He considered that if by some reason Mexico did withdraw from the T-MEC the consequences would be far more severe than in the economic crisis of 1994 or with the bank nationalization in 1982.
""")

st.subheader('KNOWLEDGE TRANSFER AND CHALLENGE :face_with_monocle:')

st.markdown("""
Our newsletter is eager to point out connections between the news and the syllabus at ITAM. Our first knowledge transfer relates to the international news of August 17 which stated [...] *Fed Fund Futures prices implied a 60\% probability of a 0.50 percentage point increase versus 40\% of a 0.75 percentage point increase at the next Fed meeting in September.*

Prof. Felix Matthys who teaches the Fixed Income course in the Dirección Financiera has provided the following link to how probabilities of rate increases/decreases can be implied from Fed Fund Futures prices:

"Expected target rate moves: Evidence from fed funds futures", see FedWatch Tool here: https://www.cmegroup.com/trading/interest-rates/countdown-to-fomc.html

Challenge: Can one of our readers calculate the implied probability and size of the change in the rate at the next Banco de México meeting? The starting point should be the TIIE futures: https://www.cmegroup.com/trading/interest-rates/mexican-funding-tiie-futures.html.

We will be proud to publish the first correct solution of the challenge and share the knowledge!

""")

st.subheader('TODAYS EDITORS')

st.markdown('''
*Grisell Diaz Villasana*

*Georgina Cassandra Cadena Garrido*
''')

st.subheader('***Share***')

link = 'https://itamita-newsletter-welcome-page-5jp2re.streamlitapp.com/August_19'

st.write('Share this page using this link: '+ link+ ", or using the QR-code:")

img_1 = qrcode.make(link)

img_byte_arr = io.BytesIO()

img_1.save(img_byte_arr, format='PNG')

img_byte_arr = img_byte_arr.getvalue()

st.image(img_byte_arr)

st.subheader('*Feedback*')

st.write('Here you can leave anonymous review.')

comment=st.text_input('Please, comment here')

grade=st.slider('Rate this episode on a scale of 1 to 5', 1, 5)

button=st.button('Submit')

if button:
    st.success("Your feedback was submited. Thank you! :heartbeat:")
    review='\n August 19 got one grade = '+ str(grade) +' with a comment: ' + comment
    with open('feedback.txt', 'a') as f:
        f.write(review)