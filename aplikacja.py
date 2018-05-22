from flask import Flask
from flask import render_template

aplikacja=Flask(__name__)

@aplikacja.route("/")
def stronaStartowa():
    pytanie1={'ans':"Płeć",'odp':["Kobieta","Mężczyzna"]}
    pytanie2={'ans':"Wiek",'odp':[]}
    pytanie3={'ans':"Waga[kg]",'odp':[]}
    pytanie4={'ans':"Wzrost[cm]",'odp':[]}
    pytanie5={'ans':"Jak oceniasz swój sposób odżywiania?",
              "odp":["Bardzo dobrze","Poprawnie","Mogłoby być lepiej","Źle"]}
    pytanie6={'ans':"Jak często uprawiasz sport?",
              'odp':["Codziennie","3-5 razy w tygodniu","2-3 razy w tygodniu","Sporadycznie","Nigdy, nie mam czasu na trening"]}
    pytanie7={'ans':"Czy prowadzisz stresujący tryb życia",
              'odp':["Zdecydowanie tak","Raczej tak","Raczej nie","Zdecydowanie nie"]}
    pytanie8={'ans':"Czy palisz papierosy nałogowo?",
              'odp':["Tak","Nie"]}
    pytanie9={'ans':"Czy pijesz alkohol?",
              'odp':["Zdecydowanie nie","Piję tylko w wyjątkowych sytuacjach","Piję zawsze kiedy mam okazję","Piję nałogowo"]}
    pytanie10={'ans':"Czy korzystasz z innych używek?",
              'odp':["Tak","Nie"]}
    pytanie11={'ans':"Czy masz problemy z układem krążeniowym",
              'odp':["Tak","Nie"]}
    pytanie12={'ans': "Czy w Twojej rodzinie ma ktoś problemy z układem krążeniowym",
                'odp': ["Tak","Nie"]}
    pytanie13={'ans': "Czy przeszedłeś chorobę nowotworową?",
                'odp': ["Tak","Nie" ]}
    pytanie14={'ans': "Czy ktoś z rodziny przeszedł chorobę nowotworową?",
                'odp': ["Tak","Nie" ]}
    pytanie15={'ans': "Czy w rodzinie bywały przypadki zachorowań na Alzheimera?",
                'odp': ["Tak", "Nie"]}
    pytanie16= {'ans': "Czy doznałeś kiedyś urazu głowy?",
                'odp': ["Tak", "Nie"]}
    pytanie17={'ans': "Wykształcenie",
                'odp': ["podstawowe nieukończone i bez wykształcenia","podstawowe ukończone","zasadnicze zawodowe","średnie zawodowe",
                        "średnie ogólnokształcące","policealne","wyższe" ]}
    pytania=[pytanie1,pytanie2,pytanie3,pytanie4,pytanie5,pytanie6,
             pytanie7,pytanie8,pytanie9,pytanie10,pytanie11,
             pytanie12, pytanie13, pytanie14, pytanie15, pytanie16, pytanie17]

    return render_template('ankietaStrona.html',pytania=pytania)



if __name__ == '__main__':
    aplikacja.run(debug=True)