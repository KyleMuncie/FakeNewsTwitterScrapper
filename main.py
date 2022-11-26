import pandas as pd

data = pd.read_csv(r'C:\Users\Kyle\PycharmProjects\pythonProject1\test.csv')
df = pd.DataFrame(data, columns=['Country (mentioned)', 'Claim', 'Source', 'Fact-checked Article'])
cols_as_np = df[df.columns[0]].to_numpy()

# Country keys
countriesZero = ["Africa",
                 "Albania",
                 "Algeria",
                 "Almeria",
                 "Bangladesh",
                 "Barbados",
                 "Belarus",
                 "Bolivia",
                 "Bulgaria",
                 "Burundi",
                 "CÃ´te d'Ivoire",
                 "California",
                 "Cameroon",
                 "Costa Rica",
                 "Democratic Republic of Congo",
                 "Democratic Republic of the Congo",
                 "Ecuador",
                 "El Salvador",
                 "Ethiopia",
                 "European",
                 "Georgia",
                 "Ghana",
                 "Gibraltar",
                 "Guinea",
                 "Haiti",
                 "Honduras",
                 "Iran",
                 "Jakarta",
                 "Jamaica",
                 "Korea",
                 "Laos",
                 "Liberia",
                 "Madagascar",
                 "Malawi",
                 "Martinique",
                 "Morocco",
                 "Myanmar",
                 "Nepal",
                 "Palestinian Territory",
                 "Paraguay",
                 "Puerto Rico",
                 "Rwanda",
                 "Saudi Arabia",
                 "Senegal",
                 "Slovakia",
                 "South African",
                 "South Sudan",
                 "Syria",
                 "Tunisia",
                 "Uganda",
                 "United Arab Emirates",
                 "United Statets",
                 "Uruguay",
                 "Vaccine",
                 "Vatican City",
                 "world wide",
                 "World wide",
                 "worldwide",
                 "Worldwide",
                 "Zimbabwe"]
countriesOne = ["Bosina"
                "Lebanon"
                "Qatar"
                "Scotland"
                "Seychelles"
                "United KIngdom"]
countriesTwo = ["Antarctica"]
countriesThree = ["Guinea-Bissau"]
sourceZero = ["audio recording"
              "bernie sanders"
              "daily expose"
              "email"
              "emmanuel macron"
              "facbook"
              "fake document"
              "flÃ¡vio bolsonaro"
              "flavio bolsonaro"
              "Harry Roque"
              "health department"
              "Jair Bolsonaro"
              "joÃ£o doria"
              "lord sumption"
              "michaÅ‚ dworczyk"
              "michael yeedon"
              "multiple persons"
              "Multiple sources"
              "multiplie sources"
              "multple sources"
              "mutliple sources"
              "news website"
              "nick donnelly"
              "scam"
              "social networks"
              "sophia dorinskaya"
              "steven hotze"
              "tayyip erdogan"
              "telegram"
              "telegraph"
              "various authors"
              "viral image"
              "websites"
              "whataspp"]
sourceOne = ["andrÃ©s manuel lÃ³pez obrador"
             "carlos bolsonaro"
             "government source"
             "ione belarra"
             "michael \"mike\" defensor"
             "narendra modi"
             "Several sources"
             "Social Networking Media Users"]
sourceTwo = ["government party"
             "pereson"]
sourceThree = ["anthony fauci"
               "doctors for life"
               "reddit"]
urlZero = ["http://aosfatos.org"
           "http://checkyourfact.com"
           "https://aajtak.intoday.in"
           "https://annielab.org"
           "https://aosfatos.org"
           "https://az.teyit.org"
           "https://cinjenice.afp.com"
           "https://efectococuyo.com"
           "https://fit.thequint.com"
           "https://ghanafact.com"
           "https://hindi.asianetnews.com"
           "https://hindi.boomlive.in"
           "https://hindi.thequint.com"
           "https://kalimasada.turnbackhoax.id"
           "https://kannada.asianetnews.com"
           "https://malayalam.samayam.com"
           "https://maldita.es"
           "https://namibiafactcheck.org.na"
           "https://navbharattimes.indiatimes.com"
           "https://observador.pt"
           "https://observers.france24.com"
           "https://oglobo.globo.com"
           "https://proveri.afp.com"
           "https://rappler.com"
           "https://sciencefeedback.co"
           "https://scroll.in"
           "https://srilanka.factcrescendo.com"
           "https://tamil.factcrescendo.com"
           "https://telugu.newsmeter.in"
           "https://tfc-taiwan.org.tw"
           "https://timesofindia.indiatimes.com"
           "https://verifica.efe.com"
           "https://verificado.com.mx"
           "https://verificat.afp.com"
           "https://www.aajtak.in"
           "https://www.abc.net.au"
           "https://www.altnews.in"
           "https://www.animalpolitico.com"
           "https://www.aosfatos.org"
           "https://www.asianetnews.com"
           "https://www.bbc.com"
           "https://www.boatos.org"
           "https://www.boombd.com"
           "https://www.boomlive.in"
           "https://www.cbsnews.com"
           "https://www.dogrulukpayi.com"
           "https://www.efe.com"
           "https://www.ellinikahoaxes.gr"
           "https://www.factchecker.in"
           "https://www.factcrescendo.com"
           "https://www.factrakers.org"
           "https://www.faktisk.no"
           "https://www.fastcheck.cl"
           "https://www.malumatfurus.org"
           "https://www.mygopen.com"
           "https://www.newsstate.com"
           "https://www.noz.de"
           "https://www.oneindia.com"
           "https://www.thequint.com"
           "https://www.thip.media"
           "https://www.tjekdet.dk"
           "https://www.voachinese.com"
           "https://youturn.in"
           "https://zimfact.org"]
urlOne = ["https://comprovem.afp.com"
          "https://evrimagaci.org"
          "https://www.eltiempo.com"
          "https://www.nytimes.com"]
urlTwo = ["https://www.faitscovid19.ca"
          "https://www.poynter.org"]


def checkURL(urlArray, url):
    temp = 0
    for full in urlArray:
        if full.find(url) != -1:
            temp = 1
    return temp


for index, row in df.iterrows():
    if row['Country (mentioned)'] in countriesZero:
        print(0)
    elif row['Country (mentioned)'] in countriesOne:
        print(1)
    elif row['Country (mentioned)'] in countriesTwo:
        print(2)
    elif row['Country (mentioned)'] in countriesThree:
        print(3)
    elif row['Source'] in sourceZero:
        print(0)
    elif row['Source'] in sourceOne:
        print(1)
    elif row['Source'] in sourceTwo:
        print(2)
    elif row['Source'] in sourceThree:
        print(3)
    elif checkURL(urlZero, row['Fact-checked Article']) == 1:
        print(0)
    elif checkURL(urlOne, row['Fact-checked Article']) == 1:
        print(1)
    elif checkURL(urlTwo, row['Fact-checked Article']) == 1:
        print(2)
    else:
        print(row)