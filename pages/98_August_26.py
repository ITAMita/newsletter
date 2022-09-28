import streamlit as st
from PIL import Image
import qrcode

st.sidebar.markdown('''
# Sections
- [NATIONAL NEWS :flag-mx:](#national-news)
- [INTERNATIONAL NEWS :earth_africa:](#international-news)
- [FOLLOW-ON STORIES FROM THE PREVIOUS WEEK (August 15-19) :mantelpiece_clock:](#follow-on-stories-from-the-previous-week-august-15-19)
- [COMPANIES NEWS :cityscape:](#companies-news)
- [WHY DON´T YOU LOVE ME ANYMORE? :broken_heart:](#why-don-t-you-love-me-anymore)
- [TODAYS EDITORS](#todays-editors)
- [Share](#share)
- [Feedback](#feedback)
''', unsafe_allow_html=True)

st.header('WEEKLY NEWSLETTER 2 (PILOT), August 22-26, 2022')

st.subheader('National news :flag-mx:')

st.markdown("""
***Monday, August 22.*** *The Consejo Nacional de Evaluación de la Política de Desarrollo Social*
(CONEVAL) reported that the percentage of the population in work poverty decreased at the
national level by 1.6 percentage points. However,
the agency pointed out that the increase in employment is concentrated in jobs whose salary range
is less than the minimum wage. (*[El Financiero](https://www.elfinanciero.com.mx/economia/2022/08/22/con-todo-e-inflacion-pobreza-laboral-baja-16-anual-en-mexico/)*)""")

img=Image.open('pics/V2P1.png')
st.image(img)

st.markdown("""***Monday, August 22*** eparately, the IMSS reported that the reform of the outsourcing law,
which came into effect one year ago, benefitted 2.9 million people as formal contractors became permanent employees 
with an increase in the daily salary from \$469 to \$597 pesos, equivalent to a rise of 27.5\%.

***Tuesday, August 23.*** Foreign Direct Investment (FDI) in Mexico had a strong annual growth
of 49.2 percent in the first half of the year, accumulating an amount of 27 thousand 511.6 million dollars, according to 
preliminary figures from the Ministry of Economy. According to the Ministry’s statement, this amount reflects "extraordinary 
movements, related to the merger of Televisa with Univision and the financial restructuring of Aeroméxico." 
The two transactions represent 6 thousand 875 million dollars of FDI. (*[El Financiero](https://www.elfinanciero.com.mx/economia/2022/08/22/fusion-televisaunivision-y-reestructura-de-aeromexico-dispara-inversion-entranjera-en-mexico/)*)

***Thursday, August 25.*** The *Instituto Nacional de Estadística y Geografía* (INEGI) published
the final GDP data for the second quarter. The economy achieves an annual advance of 1.9%, the highest of the last three records. (*[El Economista](https://www.eleconomista.com.mx/economia/PIB-de-Mexico-hilo-tres-trimestres-consecutivos-de-avance-pero-modera-dinamica-20220825-0023.html)*)
""")

st.subheader('International news :earth_africa:')

st.markdown("""
***Tuesday 23 Aug.*** The Chinese Yuan slides to a 2-year low as the currency traded at more
than 6.86 to the dollar in China’s tightly controlled onshore market. The latest selloff in the yuan, also known as the renminbi, was partly a result of the U.S. dollar’s continued march higher. It was also fueled by a series of recent data releases that appeared to show China’s economy in poor health.
(*[The Wall Street Journal](https://www.wsj.com/articles/chinas-yuan-slides-to-a-two-year-low-as-economy-stumbles-dollar-soars-11661247002)*)

***Wednesday 24. August.*** President Biden announces plans to forgive up to \$20,000 in
federal student loan debt for tens of millions of Americans, a move that will provide unprecedented relief for 
borrowers but is certain to draw legal challenges and political pushback. Independent estimates suggest the plan 
will cost more than \$300 billion over 10 years. (*[The Wall Street Journal](https://www.wsj.com/articles/biden-to-announce-student-loan-forgiveness-plan-11661331600)*)

***Friday 26 August.*** Dow falls 1,000 points after FED chairman’s remarks. Stocks declined
sharply after Jerome Powell said the Fed must continue raising rates and hold them at a higher 
level until it is confident inflation is under control. The S&P 500 closed 3.4\% lower, and the 
Nasdaq dropped 3.9\%. See graph at end. (*[The Wall Street Journal](https://www.wsj.com/articles/global-stocks-markets-dow-update-08-26-2022-11661510470)*)
""")

img=Image.open('pics/V2P2.png')
st.image(img)

st.write('As you can see in the above graph, volatility is not constant over the three days Aug 24-26. The course *Modelos Financieros 1* in the dirección financiera is all about models of dynamic volatility and changing risk.')

st.subheader('FOLLOW-ON STORIES FROM THE PREVIOUS WEEK (August 15-19) :mantelpiece_clock:')

st.markdown("""
***Monday 22 Aug*** Gas prices in Europe are rocketing as prices increased by 15\% as Gazprom announced a planned closure of the NordStream pipeline. The gas crisis has pulled the euro to parity 
with the dollar over recent months, down from \$1.15 per euro at the start of the year. (*[The Wall Street Journal](https://www.wsj.com/news/author/joe-wallace)*)

***Tuesday 23 Aug.*** Last week Enrique Quintana, financial columnist, and Juan Carlos Baker, subsecretario of the ministry of economy, concluded that it is very unlikely that Mexico will withdraw from the T-MEC, but there is a very 
small possibility that it will happen. This week the consultations for the T-MEC began and will last 75 days. Experts in international treaties consider 
that Mexico has given positive messages, but has not shown a willingness to change elements of the electricity and hydrocarbons law to 
reach a favorable solution with the USA and Canada. (*[El Financiero](https://www.elfinanciero.com.mx/economia/2022/08/24/consultas-por-el-t-mec-arrancan-con-el-pie-izquierdo-por-sector-energetico/)*)

***Thursday 25 Aug.*** The prices of milk and soda went up last Friday and, in relation to last week’s news, this week we saw the effects on inflation which rose to 8.6\%. Analysts predict that the Índice de Precios al Consumidor (IPC) will remain above 8\% until November. 
Food prices are a major worry and could generate an additional boost to the inflation rate.  (*[El Financiero](https://www.elfinanciero.com.mx/economia/2022/08/25/alimentos-devoran-a-la-inflacion-y-la-elevan-a-86-en-agosto/)*)
""")

st.subheader('COMPANIES NEWS :cityscape:')

st.markdown("""
### The Effects of Normalization

As we know, the performance of a company depends on the external context and firms have to adapt to changing situations. During the pandemic businesses faced a lot of changes in demand, supply, costs, etc. Nonetheless, some companies in the technology and personal fitness sector, like Nvidia, Zoom and Peloton, did really well. 
Now, as the economy starts to normalize, these companies find it difficult to adapt. 

***Monday 22 Aug.*** *ZOOM*

Zoom’s share price has fallen around 46\% since the beginning of the year caused by the return of the workers to offices and students to classrooms. While it is true that remote work has not disappeared yet and it seems that it will not, the videoconference market has a lot of suppliers in direct competition with Zoom such as Microsoft Teams, WebEx, etc. 
(*[El Confidencial](https://www.elconfindencial.com/empresas/2022-08-24/guru-tech-cathie-wood-rebajas-zoom-invierte-millones-prepandemia-3480121/)*)""")

img=Image.open('pics/V2P3.png')
st.image(img)

st.markdown("""***Wednesday 24 Aug.*** *Nvidia*

One of the world’s leading chip companies, released its financial results on Wednesday. As expected, they are grim (the firm even offered a preview earlier this month, hoping to dampen the shock to the markets). The Californian company reported revenues of \$6.7bn in the second financial quarter ended in July, up just 3\% from a year ago and down by 19\% from the previous quarter. The figure is 17\% lower than the \$8.1bn Nvidia had forecast in May. 
(*[The Economist](https://www.economist.com/business/2021/08/01/will-nvidias-huge-bet-on-artificial-intelligence-chips-pay-off)*)

***Thursday 25 Aug.*** *Pelotón*

The normalization effect has also affected other industries such as personal fitness. Peloton’s brand is now history in consumers’ minds. On Thursday, the stock dropped 4.41\% and for the period that ended on June 30, its revenue fell 28\% from a year earlier. The bigger existential threat to Peloton is that its customers are getting tired of the brand.
(*[Financial Times](https://www.ft.com/content/b3693cfe-ad2a-44d5-a447-46fc4edf6937)*)

### Work-life balance

***Monday 22 Aug.*** *Apple*

Apple employees seek to negotiate to be able to continue with hybrid work after the company announced that it plans to go back fully to presencial work. However, Apple´s management tries to reinstate the collaborative presencial work environment that it considers a key part of its culture. The employees argue that they have proven during the pandemic that they are capable of performing excellent quality work by working remotely. 
(*[Financial Times](https://www.ft.com/content/e40ba5a2-9dbd-4f88-87f1-c92e412ac132)*)
""")

st.subheader('WHY DON´T YOU LOVE ME ANYMORE? :broken_heart:')

st.markdown("""
### Monex (et. al.) and the BMV""")

img=Image.open('pics/V2P4.png')
st.image(img)

st.markdown("""

***Wednesday 24 Aug*** *Monex* seeks to exit the BMV. Grupo Financiero Monex is one of the largest providers of foreign exchange in the world. Over the last months, several companies such as Bachoco, Grupo Lala, Biopappel, Elementia Materiales, IEnova and Pochteca have sought to exit the BMV. One of the main reasons behind these companies wanting to leave the BMV is that there is a gap between large Mexican companies like Bimbo and Gruma and others like Lala and Bachoco. It is hard for the valuation of small companies to be at the level of big ones. The market does not favor the small ones because of their small cash flows, expectations of limited growth, low number of investors in the country and the fact that most of these companies are more family companies than large corporations.
(*El Financiero August 22*)(*[El Heraldo de México](https://www.heraldobinario.com.mx/empresas/2022/3/30/que-empresas-salieron-de-la-bolsa-mexicana-valores-las-razones-detras-del-exodo-en-la-bmv-24709.html)*)

*Thank you to Dra Sandra Minaburo who pointed out the larger story beyond Monex in El Heraldo.*

""")

st.subheader('TODAYS EDITORS')

st.markdown('''
*Diego Aurelio Zugasti Pacheco*

*Juan Martín Olivares Campos*
''')

st.subheader('***Share***')

link = 'https://itamita-newsletter-welcome-page-5jp2re.streamlitapp.com/August_26'

st.write('Share this page using this link: '+ link+ ", or using the QR-code:")

img = qrcode.make(link)

st.image(img)

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