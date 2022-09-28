import streamlit as st
from PIL import Image
import qrcode

st.sidebar.markdown('''
# Sections
- [NATIONAL NEWS :flag-mx:](#national-news)
- [INTERNATIONAL NEWS :earth_africa:](#international-news)
- [COMPANIES NEWS/FOLLOW-ON STORIES :cityscape:](#companies-news-follow-on-stories)
- [MARKETS OVERVIEW :chart_with_upwards_trend:](#markets-overview)
- [DO WE HAVE TO WORRY ABOUT THE FUTURE IN MEXICO? :fearful:](#do-we-have-to-worry-about-the-future-in-mexico)
- [DOS BOCAS: A TALE OF CONTRADICTIONS (ANOTHER ONE) :man_in_business_suit_levitating:](#dos-bocas-a-tale-of-contradictions-another-one)
- [FINTECHS IN ACTION :robot_face:](#fintechs-in-action)
- [TODAYS EDITORS](#todays-editors)
- [Share](#share)
- [Feedback](#feedback)
''', unsafe_allow_html=True)

st.header('WEEKLY NEWSLETTER 3, Aug 29 - Sep 2, 2022')

st.subheader('NATIONAL NEWS :flag-mx:')

st.markdown("""
***Monday, August 29.*** Mexico's president AMLO announced the new director of the state company *LitioMX*: Pablo Taddei. "It has already been decided that a young man who is finishing his doctorate at Harvard on the environment and renewable energy, is going to be the director, because it is proven that the largest deposits of this mineral are in Sonora," he said. "We are developing a plan so that Sonora becomes a state of renewable, clean energy generation and also of lithium battery production to boost the automotive industry in Sonora.
(*[EL PAIS](https://elpais.com/mexico/2022-08-31/lopez-obrador-entrega-la-direccion-de-la-empresa-estatal-litio-para-mexico-al-hijo-del-superdelegado-de-sonora.html)*)

***Tuesday, August 30.*** Interjet entered a process of commercial bankruptcy, after one of the airline’s creditors made the request for this procedure. It is estimated that Interjet’s total debt is around 40 billion pesos, and this procedure has the aim of meeting the airline’s financial obligations. One of the biggest debts the company has is with its workers, who are owed around 1.8 billion pesos, the main reason why they have been on a strike since January 2021. Many of Interjet’s assets have been confiscated and are expected to be liquidated to cover part of the airline’s debt. 
(*[El Financiero](https://www.elfinanciero.com.mx/empresas/2022/08/30/juez-admite-entrada-de-interjet-a-concurso-mercantil/?outputType=amp)*)

***Tuesday, August 30.*** The Encuesta Nacional de Financiamiento de las Empresas (ENAFIN, 2021) revealed that 2 out of 3 companies in Mexico have never requested financing, and the main factor that limits their access is the high interest rates. According to this survey, carried out by INEGI and CNBV, the main problems for companies were the high rates (62\%), requirements (39\%), inaccessible payment terms (30%), too much paperwork (33\%) and the limited ability to pay (14\%). 
(*[El Economista](https://www.eleconomista.com.mx/sectorfinanciero/Mas-de-la-mitad-de-las-empresas-en-Mexico-nunca-han-solicitado-financiamiento-Enafin-20220829-0077.html)*)

***Wednesday, August 31.*** Revenues of Mexican oil companies increased 91.8\% in July, which helped to counteract the impact of the 9.4\% decrease in tax revenues. The public budget income increased by 7.8\% in real terms, according to the SHCP. 
(*[El Financiero](https://www.elfinanciero.com.mx/economia/2022/08/30/petroleo-salva-a-las-finanzas-publicas-ingresos-presupuestarios-crecen-78-en-julio/)*)

***Thursday, September 1.*** . US dollar remittances recorded its highest monthly amount in July by 
Mexican households. According to Banco de México, remittances captured by 4.9 million households in 
Mexico registered an entry of 5,296 million dollars in the month, the highest monthly level ever captured 
for any month. The drivers of these remittances remain in the "generous fiscal transfers" that workers in 
the United States continue to receive, […] and the deep contraction of economic activity and employment that 
prevails in Mexico”, explained the economist for Latin America at Goldman Sachs, Alberto Ramos.
(*[El Economista](https://www.eleconomista.com.mx/economia/Hogares-mexicanos-reciben-5296-mdd-en-remesas-el-nivel-mas-alto-captado-durante-un-solo-mes-20220901-0045.html)*)
""")

st.subheader('INTERNATIONAL NEWS :earth_africa:')

st.markdown("""
***Monday, August 29.*** *Asian market plunge 2\%.*

After the drops of 3\% to 4\% of the U.S. stock markets following Jason Powell´s statement on Friday August 26th, 
the Asian stock market started the week with losses of 2\%. We will have to keep watch on US employment data that 
will be published later this week because Powell pointed out that the FED needs to see the evolution of both the 
labor market, the GDP and inflation to determine its next move at the meeting on September 21 and 22.
(*[El Financiero](https://www.pressreader.com/mexico/el-financiero/20220829/textview)*)""")

img=Image.open('pics/V3P1.png')
st.image(img)

st.markdown("""***Tuesday, August 30.*** *Stock futures rise.*

U.S. equity markets were primed for a positive open Tuesday, which would come as a relief after Friday’s brutal selloff and Monday’s declines. Oil futures, meanwhile, declined early Tuesday after Monday’s rally. Investors are looking for a path forward after Fed Chairman Jerome Powell’s remarks Friday. 
(*[CNBC](https://www.cnbc.com/2022/08/30/5-things-to-know-before-the-stock-market-opens-tuesday-august-30.html)*)

***Wednesday, August 31.*** *Inflation Tightens Its Grip on Europe*

Euro inflation beat its inflation record since its implementation as a common currency. In August the inflation rate reached a level of 9.1\%, 0.2\% greater than the one reported in July. Some countries (mostly the ones in the East) have reported double digit numbers. Main reason is the increase in the cost of energy due to the Russian invasion of Ukraine.
(*[The New York Times](https://www.nytimes.com/2022/08/31/business/eurozone-inflation.html)*)

***Thursday, September 1.*** *The US economy is starting to cool, but the job market is on fire.*

In July, employment growth was expected to around 250,000 jobs, decreasing open positions to 10.5 million. Instead, 528,000 jobs were added, and available jobs increased to 11.2 million. Members of the Federal Reserve view this as a threat to its attempts to tame inflation. The high demand for jobs drives wages up, which in turn increases prices. Many technology companies have laid off employees, but many other industries need workers and have increased available job positions.
(*[CNN](https://edition.cnn.com/2022/09/01/economy/us-jobs-report-august-preview/index.html)*)

***Friday, September 2.*** *USA businesses created 315,000 jobs in August.*

Businesses are hiring beyond expectations although the unemployment rate in the USA increased to 3.7\%. That is, the unemployment rate is above the minimum reached before the pandemic of 3.5\%.
(*[El Economista](https://www.eleconomista.com.mx/economia/EU-creo-315000-empleos-en-agosto-y-recupera-niveles-previos-a-la-pandemia-20220902-0041.html)*) 
""")

st.subheader('COMPANIES NEWS/FOLLOW-ON STORIES :cityscape:')

st.markdown("""
### Bed Bath & New Plan?

The company announced on Wednesday the swift and significant steps it is taking to try to revive its struggling business, including layoffs, store closures and a shake-up of the brands on its shelves. On a call with investors, the New Jersey-based retailer laid out details of its latest turnaround push. It said it has started closing about 150 of its “lower producing” namesake stores. It will also slash costs by shrinking head count by about 20\% across its corporate and supply chain workforce. To strengthen its balance sheet, the company said it secured more than \$500 million in new financing, including a loan.
(*[CNBC](https://www.cnbc.com/2022/08/31/bed-bath-beyond-announces-500-million-in-new-financing-plans-for-layoffs.html)*)

### Elon vs Twitter, the battle continues.

Elon Musk has seized on a whistleblower report by Twitter’s former security chief to bolster his legal fight to terminate his \$44bn deal to buy the social media company. Musk’s legal team wrote to Twitter executives on Monday, according to a filing released on Tuesday, claiming that, if true, Peiter Zatko’s allegations breach several aspects of the merger agreement struck in April, which the billionaire has been seeking to abandon.
(*[Financial Times](https://www.ft.com/content/a77d4001-628f-4d13-b864-f68d89b340b4)*)

### BMV close to get delisted from the its own index

BMV could be removed from the S&P/BMV IPC index for not complying with the required volume of transactions. The main Mexican stock market is one the candidates to drop from the main stock index of the country which has suffered the worst performance among its peers in the region, a decline in trading volume and an increase in the delisting of companies. The S&P/BMV IPC index has fallen more than 15\% this year and on Wednesday officially entered bear market territory. 
(*[El Economista](https://www.eleconomista.com.mx/amp/mercados/Grupo-BMV-podria-salir-del-indice-SP-BMV-IPC-por-no-cumplir-con-volumen-de-transacciones-20220901-0069.html)*) 

### TMEC

On Monday August 29 the Mexican president reproached the US government for the energy controversy of the past April. At the beginning of the Consultation rounds of USMCA in energy matters, the Mexican president in his morning meeting Conferencia Mañanera pointed out that his proposal about energy production from his Constitutional reform initiative of past April was rejected by the Mexican Congress. The president also claimed that the US government acted to protect the interests of private energy companies in México, even through legal means, which from his point of view “was an attempt to destroy the commission (CFE) and give all the production to the private companies”.
(*[El Financiero](https://www.elfinanciero.com.mx/nacional/2022/08/29/amlo-reprocha-a-eu-controversia-en-t-mec-por-politica-energetica-no-tienen-llenadera/)*) 

""")

st.subheader('MARKETS OVERVIEW :chart_with_upwards_trend:')

img=Image.open('pics/V3P2.png')
st.image(img, caption='US stock markets over the week after Powell’s speech at Jackson Hole')

st.markdown("""


### Currencies YTD 

The graph below shows the weak performance against the US dollar of the Euro, British pound and the Korean wong due to high energy costs this year, while the Mexican Peso has remained stable to strong.
(*[Yahoo!Finance]()*) 
""")

img=Image.open('pics/V3P3.png')
st.image(img)

st.subheader('DO WE HAVE TO WORRY ABOUT THE FUTURE IN MEXICO? :fearful:')

st.markdown("""
On Wednesday August 31, Banco de Mexico’s Board of Governors cut the expected GDP growth rate for 2023 from 2.4\% to 1.6\%. From the perspective of the current Governor, Victoria Rodriguez, this cut does not imply that there exists a risk of recession. In fact, any of the members of the Board expect a recession in the US not in Mexico. For this year, the expected GDP growth rate is 2.2\%, within a range between 1.7\% and 2.7\%. 

The principal reasons for this cut are the negative effects of the deceleration of the US economy and the effects of the restrictive monetary policy to avoid inflation. In the first case, the Governor pointed out that there are indicators of deceleration in the neighboring country, for example the downfall in the external demand for Mexican products. Related to the second case, it is not a surprise that internal consumption in both countries has a downward trend, since Central Banks are still managing the inflation problem by raising interest rates. 

With respect to inflation, the Board expects that the peak of inflation will be reached in the third trimester of the current year, when it is expected to reach 8.5\%. From that point the Banco de México expects the rate to take a downward trend until it achieves the inflation target rate of 4\%. Until then, it is expected that the Bank continues following the Fed about raising interest rates, in words of Banco de México’s governor Jonathan Heath: “We have to follow the Fed to avoid large capital outflows and the weakening of the Mexican Peso against the USD”. 
(*[El Financiero](https://www.elfinanciero.com.mx/economia/2022/08/31/banxico-da-tijeretazo-a-pronostico-de-crecimiento-para-2023-pasa-de-24-a-16/)*) (*[El Financiero](https://www.elfinanciero.com.mx/economia/2022/08/29/fed-se-pone-ruda-analiza-subir-tasa-de-eu-en-75-puntos-base/)*) 

""")

st.subheader('DOS BOCAS: A TALE OF CONTRADICTIONS (ANOTHER ONE) :man_in_business_suit_levitating:')

st.markdown("""
On Tuesday August 30, it was reported that the Pemex Administration Council authorized a budget expansion of 5.617 billion USD. With this addition, the cost of the Dos Bocas refinery reaches an amount of 20 billion USD, which is more than double of the original 8.9 billion USD forecasted budget. President AMLO admitted that the cost will be more than the initial estimates because PEMEX had not included the construction of equipment that will be needed to operate, among them a pipeline.

However, the president claims it will only be of 2 to 4 billion pesos over the budget and that it is a lower amount than what other foreign companies would have charged. He also claims the Mexican population to be patient with the project “There is no corruption, these are not the past times. Rocío Nahle is an honest and integer woman.”

After the president admitted the raise in the total costs, some analysts warn that we should expect more adjustments because of the volatility of the Mexican peso, inflation, and logistics. Other analysts said this increase in costs was expected since the initial forecasted cost by the government was not realistic. 
(*[El Financiera](https://www.elfinanciero.com.mx/nacional/2022/09/01/cuarto-informe-de-gobierno-de-amlo-dos-bocas-la-refineria-que-no-refina-y-que-salio-mas-cara/?outputType=amp)*) (*[El Economista](https://www.eleconomista.com.mx/empresas/Preven-mas-sobrecostos-en-Dos-Bocas-por-inflacion-20220831-0012.html)*) (*[El Universal](https://www.eluniversal.com.mx/cartera/amplian-recursos-refineria-olmeca-costara-20-mil-mdd)*)

""")

st.subheader('FINTECHS IN ACTION :robot_face:')

st.markdown("""
Strengthening the financial sector in rural areas is crucial to improve food security and the generation of more stable income. Consequently, this contributes to sustainable economic development. In Mexico, the largely informal agricultural sector, with 5.5 million farmers, represents 3.8\% of the country’s GDP. More than 90\% of the people who make up this sector cannot access credit or formal financial services which limits their ability to improve operations or adopt new technologies to increase yields and break cycles of poverty. They usually pay for their inputs in cash transactions and are paid for their harvests in the same way. 

Also, there is no traceability of the money. Moreover, farming, being cyclical, only sees money leaving the farm while waiting for a cash gain after the harvest but in most cases, farmers need some type of financing or debt to overcome those months without liquidity. Verqor aims to digitize the operation, management and obtaining credit for Mexican farmers. Subsequently crop buyers will obtain purchasing data from farmers and use it to make data-driven decisions and implement sustainable practices. With a B2B2C model, its financial platform does not grant cash, but rather offers products such as seeds, insecticides, machinery, fertilizers, irrigation equipment, agrochemicals, among others, through an online catalog. Once the farmer is harvesting the crops, Verqor connects him with companies that buy products directly from the farmers, such as AB InBev, Heineken. Also, payment is made through the Verqor platform, thus eliminating between three or four intermediaries. 
(*[El Heraldo De Mexico](https://heraldodemexico.com.mx/nacional/2022/8/25/verqor-la-fintech-que-busca-soluciones-de-impacto-ambiental-al-digitalizar-la-industria-agroalimentaria-433712.html)*)

""")

st.subheader('TODAYS EDITORS')

st.markdown('''
*Barbra Bala García*

*Raúl Manzano Cabrera*
''')

st.subheader('***Share***')

link = 'https://itamita-newsletter-welcome-page-5jp2re.streamlitapp.com/September_2'

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