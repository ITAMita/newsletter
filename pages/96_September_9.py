import streamlit as st
from PIL import Image
import qrcode

st.sidebar.markdown('''
# Sections
- [NATIONAL NEWS :flag-mx:](#national-news)
- [INTERNATIONAL NEWS :earth_africa:](#international-news)
- [COMPANIES NEWS :cityscape:](#companies-news)
- [A GAMECHANGER IN CRYPTOCURRENCIES? :money_with_wings:](#a-gamechanger-in-cryptocurrencies)
- [MARKETS OVERVIEW :chart_with_upwards_trend:](#markets-overview)
- [FOLLOW-ON STORIES :cold_sweat:](#follow-on-stories)
- [Share](#share)
- [Feedback](#feedback)
''', unsafe_allow_html=True)

st.header('WEEKLY NEWSLETTER 4 (Pilot), Sep 5-9, 2022')

st.subheader('NATIONAL NEWS :flag-mx:')

st.markdown("""
***September 5th.*** *Consumer confidence continues its downward trend.*

In the eighth month of the year, the Consumer Confidence Indicator reported a monthly decrease of 0.4 points, its fourth consecutive reduction. Banco de México and INEGI expect consumer confidence to continue to deteriorate due to the adverse economic conditions that have arisen, coupled with the stagnation of the economy in the United States, which influences the Mexican economy.
(*[El Economista](https://www.eleconomista.com.mx/economia/Confianza-de-los-consumidores-mexicanos-disminuyo-por-cuarto-mes-consecutivo-en-agosto-20220905-0044.html)*)

***Tuesday, August 30.*** *Generation of formal employment regained momentum in August and sets a record.*

Compared to August 2021, the generation of formal employment in Mexico increased by 22.1\%. 157,432 jobs were added to the Mexican Social Security Institute (IMSS), and they were given both in permanent and temporary jobs: 107,963 in the first case and 49,469 in the second. In the last twelve months, the IMSS highlighted the creation of 816,043 jobs, which is equivalent to an annual rate of 4.0\%. The report presented by this institution indicates that this annual rate is the fourth highest since data has been recorded.
(*[El Economista](https://www.eleconomista.com.mx/empresas/Empleo-permanente-mejoro-en-agosto-se-sumaron-mas-de-157000-plazas-en-el-IMSS-20220905-0065.html)*)

***September 7th.*** *The recovery in productive investment faces a challenging scenario.*

Productive investment in Mexico rises 0.7\% and has a weak recovery. Given the incessant rise in inflation at the national and international level, stagnant private consumption in the country, the contractionary monetary policies by Banxico and fears of a recession in the United States, productive investment faces a challenging landscape in the upcoming months.
(*El Financiero*)

***September 8th.*** *The 2023 Economic Package seeks to attract foreign direct investment.*

The ministry of Finance and Public Credit (SHCP), Rogelio Ramírez, delivered the 2023 Economic Package to the Congress, which is composed of: General Criteria for Economic Policy, the Federal Income Law, and the Federal Expenditure Budget. On this occasion, none of these projects include tax increases or reductions in social programs. The main objective of the 2023 Economic Package is to prioritize investment in social, health and education terms.
(*[El Economista](https://www.eleconomista.com.mx/economia/Rogelio-Ramirez-de-la-O-entrega-el-Paquete-Economico-2023-a-legisladores-20220908-0071.html)*)
""")

st.subheader('INTERNATIONAL NEWS :earth_africa:')

st.markdown("""
***September 5th.*** *Europe Governments intervene in the power market.*

Governments in Europe are starting to intervene in the power market due to the strain it has presented. Sweden and Finland implemented emergency backstops for their energy producers. The two governments announced liquidity facilities made up of loans and credit guarantees to avoid some power companies going into technical defaults. The goal is to prevent Russia's energy restrictions from causing a financial crisis. Sweden's parliament approved the measure on Monday afternoon.
(*Financial Times*)

Also, on the same day, OPEC+ agrees to cut production by 100K bbl/day. Followed by this decision, crude oil futures went up. The small cut effectively reverses the 100K bbl/day that OPEC+ said it would add to the market last month.
(*[Seeking Alpha](https://seekingalpha.com/news/3880244-opec-agrees-to-cut-production-by-100k-bblday-reports-say)*)

***September 6th.*** *Meet the new UK Prime Minister.*

Liz Truss, from the Conservative Party, becomes Britain’s prime minister succeeding Boris Johnson. She faces a challenging economic situation with a slowing economy, inflation, a high number of people living the workforce and an energy crisis.
(*The Wall Street Journal*)

Also, on the same day, the dollar reached a new maximum since 2002 against the euro driven by the resilience of the United States economy, which is the reason of the continuing adjustments of interest rates by the Federal Reserve (Fed). The US dollar gained 0.21\% on the European currency, which traded at 0.9901 dollars, for the first time since the beginning of December 2002.
(*[Financial Times](https://www.ft.com/content/e24b9e99-fa7c-4145-b7aa-01f3594c33b3)*)

***September 7th.*** *Yen currency in its lowest and Canada yield at its highest.*

The yen fell to its lowest level against the dollar since August 1998 falling 1.7\% to a low of \¥142.97 per dollar. Hedge funds in the US and Europe consider that the Bank of Japan will continue to implement a loose monetary policy of low interest rates (*Financial Times*). 

While, the Bank of Canada raised its rate by 75 basis points to 3.25\%, its highest level in 14 years, as a measure to combat inflation.
(*Financial Times*)

***September 8th.*** *Death of Queen Elizabeth II.*

Queen Elizabeth II, the UK’s longest-serving monarch, has died at Balmoral aged 96, after reigning for 70 years. Stores closed and events cancelled as UK businesses pay respects to Queen. London retailers shut their doors and sports games postponed after death of British monarch. Britain activated Operation London Bridge, the funeral plan that guides the country through the rituals of tribute and mourning culminating with her burial 10 days later.
(*[BBC](https://www.bbc.com/news/uk-61585886)*)(*[ELLE](https://www.elle.com/uk/life-and-culture/culture/a30044076/what-happens-when-queen-dies/)*)""")

img=Image.open('pics/V4P1.jpg')
st.image(img)

st.markdown("""
***September 9th.*** *European Rate Hike.*

The European Central Bank (ECB) raised the interest rate 75 basis points. This represents the second rise this year after a 50 basis points increase in July. The ECB also signaled that further raises are to be expected to contain inflation. Christine Lagarde, president of the ECB, warned that inflation is affecting several sectors besides energy.
(*The Wall Street Journal*)
""")

st.subheader('COMPANIES NEWS :cityscape:')

st.markdown("""
***Tuesday, September 6th.*** *Juul Labs will pay to end a corrosive investigation into its advertising.*

Juul Labs will pay \$438.5m to end an investigation of its advertising to underage buyers as it became one of the leading e-cigarette companies in the US. The agreement with more than 30 states also restricts Juul's marketing, for example by prohibiting the use of people under 35 in its ads. The US Food and Drug Administration said in June that it would ban sales of Juul products due to a lack of health impact data. The measure is on hold while the company appeals the decision.
(*[BBC](https://www.bbc.com/news/business-62813896)*)

***Wednesday, September 7th.*** *Cineworld Files for Chapter 11 After Sluggish Ticket Sales.*

Cineworld, the world’s second-largest movie theater chain behind rival AMC Entertainment Holdings Inc., filed a chapter 11 petition in the U.S. Bankruptcy Court in Houston. While movie-theater attendance has recovered somewhat as Covid-19 fears wane, ticket sales still lag behind their prepandemic levels. London-based Cineworld has more than \$5 billion in debt and faces a roughly \$1 billion legal judgment stemming from a soured merger with Canadian cinema chain Cineplex Inc. The chapter 11 filing spotlights how Cineworld’s fate diverged during the pandemic from that of AMC, which became a darling of retail investors who drove its stock to dizzying heights.

Compared with Cineworld, AMC was arguably in worse shape as the pandemic began, according to analysts, but raised roughly \$2.2 billion over the past two years by selling new shares to an enthusiastic investor base who call themselves “apes.” Cineworld Chief Executive Mooky Greidinger acknowledged in an interview with The Wall Street Journal last year that AMC had found a powerful capital-raising advantage through its meme-stock status that London Stock Exchange -listed Cineworld didn’t. “British retail investors just aren’t as cultish as U.S. retail investors are,” said Michael Pachter, an analyst at Wedbush Securities.
(*Wall Street Journal*)

***Thursday, September 8th.*** *Kim Kardashian will launch and investing firm.*

Kim Kardashian announced on Wednesday that she is launching an investment firm called SKKY Partners. According to a post on the company's Instagram account, the firm will focus on "consumer products, e-commerce, digital, media, hospitality and luxury". She founded the company with Jay Sammons, who is a specialist in the sector. Kim specified that she will also work with her mother, Kris Jenner, another figure from her reality show.
(*[El Economista](https://www.eleconomista.com.mx/sectorfinanciero/Kim-Kardashian-lanza-firma-de-inversiones-en-EU-20220907-0053.html)*)
""")

st.subheader('A GAMECHANGER IN CRYPTOCURRENCIES? 	:money_with_wings:')

st.markdown("""

Ethereum will undergo a transformation, called the “Merge”, planned for Sep 15, in its way of operating that not only seeks to reduce the cost of keeping its network secure by reducing energy use, but could also turn ether into a deflationary cryptocurrency, as bitcoin currently is. The current mining mechanism of Ethereum uses “Proof of Work”: which is similar to the mining mechanism of Bitcoin. In the “Merge”, Proof of Work will be replaced by “Proof of Stake”.

The change seeks to reduce the power consumption which also promises to reduce the number of ethers on the network and among its participants. As reported in the Economist, the reduction in Ethereum’s power consumption would equate to the power consumption of the Netherlands on an annualized basis.
""")

img=Image.open('pics/V4P2.png')
st.image(img, caption='US stock markets over the week after Powell’s speech at Jackson Hole')

st.markdown("""
Additionally, the Merge could substantially reduce ether inflation to 0.5\% and even turn it negative, making it a deflationary asset, meaning its supply could be reduced. 

If people use the network a lot, then more supply of ether will be burned because it is going to be part of the fees to do transactions. In that case, you don't have a supply that slowly increases and then stays flat, you can have a supply that decreases, so the more applications are used on the network, the more ether it burns and therefore becomes more valuable, because there is less of it. That is a mechanism that Bitcoin does not have.
(*[El Economista](https://www.eleconomista.com.mx/tecnologia/Ether-puede-ser-una-criptomoneda-deflacionaria-despues-de-The-Merge-Lex-Sokolin-20220910-0001.html)*) 
""")

st.subheader('MARKETS OVERVIEW :chart_with_upwards_trend:')

st.markdown('### The price of the Mexican oil hits its lowest point since January 2022')

img=Image.open('pics/V4P3.png')
st.image(img)

st.markdown("""
Last Wednesday, September 7th, Mexican oil reached its lowest point in 8 months, settling at a price of 78.48 dollars per barrel. This drop in price is due to different factors. Among the most important are the effects on the prices of raw materials due to the risks of new confinements due to COVID19 in China, the speech by the president of the FED Jerome Powell on the continuous rises in interest rates, and the possible agreements between the United States and Iran regarding the market of petroleum products.
(*[Banco De Mexico](https://www.banxico.org.mx/apps/gc/precios-spot-del-petroleo-gra.html)*)

### USD/JPY catapults to new highs since 1998
""")

img=Image.open('pics/V4P4.png')
st.image(img)

st.markdown("""

On Wednesday, September 7th, the USD/JPY reached a maximum level of 144.98. The main reason is the interest rate spread between US Treasuries and Japanese Government Bonds, which has widened this year. The immediate effect has been a sharp depreciation in the value of the yen, as the Bank of Japan has been slower in raising its interest rates compared to the US Federal Reserve.
(*Yahoo Finance*) 
""")

st.subheader('FOLLOW-ON STORIES :cold_sweat:')

st.markdown("""
### DOS BOCAS: A TALE OF CONTRADICTIONS (TO BE CONTINUED)

The Federal Expenditure Budget delivered last Thursday by the Ministry of Finance and Public Credit (SHCP) foresees that the Dos Bocas refinery will receive another 47 thousand 200 million pesos during 2023.

At the beginning of the year, the Treasury Department planned to spend 47 thousand 200 million pesos during 2022, which has been doubled by SHCP. However, it is estimated that by December of the current year, the annual spending could be three times higher than estimated: 153 thousand 600 million pesos.

Despite this, Leonardo Cornejo Serrano, director of the Dos Bocas project, told to the newspaper El Financiero that the total cost of the Dos Bocas refinery would be approximately 13.7 billion dollars. Therefore, he considered as exaggerated the estimates made by various business circles who believe that the total cost of the project will be 20 billion dollars.

Cornejo Serrano pointed out that the refinery's cost overruns are due to the increase in prices of various materials, as well as additional works that were not previously contemplated. "Currently, the refinery is 97 percent complete. No more equipment is needed because 100 percent is already installed on site and we expect the first refined barrel to come out in the first quarter of 2023," he concluded.
(*[El Finaciero](https://www.elfinanciero.com.mx/economia/2022/09/08/paquete-economico-2023-proponen-nueva-inyeccion-a-dos-bocas-por-47-mil-200-mdp/)*)

### BED, BATH & BEYOND: AN IRREPARABLE LOSS

Gustavo Arnal, Chief Financial Officer of Bed Bath & Beyond, died after falling from a skyscraper in the Tribeca neighborhood of Manhattan on September 2nd. Days earlier, Arnal was among Bed Bath & Beyond executives who provided details on the company's restructuring plan, which included cutting 20 percent of jobs in its corporate and supply chain operations, as well as the closure of 150 production stores. The plan also called for new financing projects and the sale of up to 12 million shares.
(*[El Finaciero](https://www.elfinanciero.com.mx/mundo/2022/09/05/gustavo-arnal-director-financiero-de-bed-bath-beyond-se-suicida-en-nueva-york/)*)

His death leaves Bed Bath & Beyond, which has been searching for a permanent chief executive officer, with a leadership gap at a time when vendors and investors have been worried about its operations. The company has been burning through cash reserves in recent quarters, ending May with just about \$100 million. Also, its market value has fallen below \$1 billion from a peak of more than \$17 billion a decade ago.

Arnal was one of several parties, including Bed Bath & Beyond, named in a securities fraud civil lawsuit filed in august 23rd in Washington’s, D.C. Federal Court. The lawsuit alleged that from March to August of this year, the parties artificially inflated Bed Bath & Beyond's shares price. However, the company responded last week saying that the lawsuit didn’t have any merit and declined to comment further on the litigation.
(*[ProQuest](http://proquest.itam.elogim.com/newspapers/bed-bath-amp-beyond-finance-chief-gustavo-arnal/docview/2709596085/se-2)*)
""")

st.subheader('TODAYS EDITORS')

st.markdown('''
*María José Sarabia Lujano*

*Gloria María Cabrera Martínez*
''')

st.subheader('***Share***')

link = 'https://itamita-newsletter-welcome-page-5jp2re.streamlitapp.com/September_9'

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

