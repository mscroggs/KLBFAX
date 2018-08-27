#!/usr/bin/env python
# -*- coding: utf-8 -*-

from page import Page
from random import shuffle

class HolidayPage(Page):
    def __init__(self, num, place, sights):
        super(HolidayPage, self).__init__(num)
        self.in_index = False
        self.title = place
        self.sights = sights

    def generate_content(self):
        self.print_image(
                        "---------------------------------------------------------------yyyyyyyyyyyyyyyy\n"
                        "---------------------------------------------------------------yyyyyyyyyyyyyyyy\n"
                        "----------------------------------------------------------------yyyyyyyyyyyyyyy\n"
                        "----------------------------------------------------------------yyyyyyyyyyyyyyy\n"
                        "-----------------------------------------------------------------yyyyyyyyyyyyyy\n"
                        "-----------------------------------------------------------------yyyyyyyyyyyyyy\n"
                        "------------------------------------------------------------------yyyyyyyyyyyyy\n"
                        "-------------------------------------------------------------------yyyyyyyyyyyy\n"
                        "--------------------------------------------------------------------yyyyyyyyyyy\n"
                        "---------------------------------------------------------------------yyyyyyyyyy\n"
                        "-----------------------------------------------------------------------yyyyyyyy\n"
                        "-------------------------------------------------------------------------yyyyyy\n"
                        "---------------------------------------------------------------------------yyyy\n"
                        "-------------------------------------------------------------------------------\n")
        self.move_cursor(0,0)
        self.add_title("Holidays",fg="BLACK",bg="ORANGE",font="size4",fill=False)
        self.add_title(self.title,fg="BLACK",bg="GREEN",font="size4bold",fill=False)
        self.add_text("Things to see and do in "+self.title)
        self.add_newline()
        shuffle(self.sights)
        color = "ORANGE"
        for thing in self.sights:
            self.add_wrapped_text(thing, fg=color)
            self.add_newline()
            if color == "GREEN":
                color = "ORANGE"
            else:
                color = "GREEN"

class TravelIndex(Page):
    def __init__(self, num, pagels):
        super(TravelIndex, self).__init__(num)
        self.index_num = "185-199"
        self.title = "Holidays"
        self.pagels = pagels

    def generate_content(self):
        self.print_image(
                        "---------------------------------------------------------------yyyyyyyyyyyyyyyy\n"
                        "---------------------------------------------------------------yyyyyyyyyyyyyyyy\n"
                        "----------------------------------------------------------------yyyyyyyyyyyyyyy\n"
                        "----------------------------------------------------------------yyyyyyyyyyyyyyy\n"
                        "-----------------------------------------------------------------yyyyyyyyyyyyyy\n"
                        "-----------------------------------------------------------------yyyyyyyyyyyyyy\n"
                        "------------------------------------------------------------------yyyyyyyyyyyyy\n"
                        "-------------------------------------------------------------------yyyyyyyyyyyy\n"
                        "--------------------------------------------------------------------yyyyyyyyyyy\n"
                        "---------------------------------------------------------------------yyyyyyyyyy\n"
                        "-----------------------------------------------------------------------yyyyyyyy\n"
                        "-------------------------------------------------------------------------yyyyyy\n"
                        "---------------------------------------------------------------------------yyyy\n"
                        "-------------------------------------------------------------------------------\n"
                        "-------------------------------------------------------------------------------\n"
                        "-------------------------------------------------------------------------------\n"
                        "-------------------------------------------------------------------------------\n"
                        "-------------------------------------------------------------------------------\n"
                        "-------------------------------------------------------------------------------\n"
                        "-----------------------------------------------gggggg--------------------------\n"
                        "----------------------------------------------gggggg---------------------------\n"
                        "---------------------------------------------gggggg----------------------------\n"
                        "--------------------------------------------gggggg-----------------------------\n"
                        "-------------------------------------------gggggg------------------------------\n"
                        "------------------------------------------gggggg-------------------------------\n"
                        "----------------------------ggggggg------gggggg--------------------------------\n"
                        "------------------------ggggggggggggggg-gggggg---------------------------------\n"
                        "-----------------------gggggggggggggggggggggg----------------------------------\n"
                        "----------------------gggggggggg--ooooogggggggggggg----------------------------\n"
                        "---------------------gggggggggg-ooooooooggggggggggggg--------------------------\n"
                        "---------------------gggggggggoooooooooo--ggggggggggggg------------------------\n"
                        "--------------------ggggggggoooooooooooo---ggggggggggggg-----------------------\n"
                        "--------------------ggggggoooooooooooo-------gggggggggggg----------------------\n"
                        "-------------------gggggooooooooooooo---------ggggggggggg----------------------\n"
                        "-------------------gggooooooooooooo------------ggggggggggg---------------------\n"
                        "------------------gggooooooooooooo--------------ggggggggggg--------------------\n"
                        "------------------goooooooooooooo---------------ggggggggggg--------------------\n"
                        "------------------oooooooooooooo-----------------ggggggggggg-------------------\n"
                        "----------------ooooooooooooooo------------------ggggggggggg-------------------\n"
                        "---------------ooooooooooooooo--------------------gggggggggg-------------------\n"
                        "-------------oooooooooooooooo----------------------gggggggggg------------------\n"
                        "------------oooooooooooooooo-------------------------gggggggg------------------\n"
                        "-----------oooooooooooooooo----------------------------ggggggg-----------------\n"
                        "----------ooooooooooooooooo------------------------------ggggg-----------------\n"
                        "---------ooooooooooooooooo---------------------------------gggg----------------\n"
                        "--------oooooooooooooooooo-----------------------------------ggg---------------\n"
                        "-------oooooooooooooooooo-------------------------------------gg---------------\n"
                        "-------oooooooooooooooooo------------------------------------------------------\n"
                        "------ooooooooooooooooooo------------------------------------------------------\n"
                        "------ooooooooooooooooooo------------------------------------------------------\n"
                        "-----ooooooooooooooooooo-------------------------------------------------------\n"
                        "-----ooooooooooooooooooo-------------------------------------------------------\n"
                        "----oooooooooooooooooooo-------------------------------------------------------\n"
                        "----oooooooooooooooooooo-------------------------------------------------------\n"
            )
        self.move_cursor(0,0)
        self.add_title("holidays",fg="BLACK",bg="GREEN",fill=False,font="size4bold")
        for page in self.pagels:
            self.add_text(page.number+" ",fg="ORANGE")
            self.add_text(page.title)
            self.add_newline()

pagels = []

pagels.append(HolidayPage("186","Paris",["The Louvre","Musée d'Orsay","Eiffel Tower","Notre-Dame de Paris","Palace of Versailles","Hôtel des Invalides","Musée de l'Orangerie","Centre Georges Pompidou","Arc de Triomphe","Sainte-Chapelle","Musée Marmottan Monet","Place de la Concorde","Place des Vosges","Musée Rodin","Sacré-Coeur","Musée de Cluny","Musée Jacquemart-André","Petit Palais","Palais Garnier","Jardin du Luxembourg","Jardin des Tuileries","Musée du Quai Branly","Catacombs","Coulée Verte René-Dumont","Tour Montparnasse","Père Lachaise Cemetery","Musée des Arts Décoratifs","Musée Nissim de Camondo","Panthéon","Jardin des Plantes","Musée des Arts et Métiers","Bois de Vincennes","Saint-Germain-des-Prés","Grand Palais","Le Marais","Canal Saint-Martin","Montmartre","Église Saint-Sulpice","Latin Quarter","Les Passages Couverts","Jardin d'Acclimatation","Fondation Louis Vuitton","Pont Neuf","Musée Albert Kahn","Guimet Museum","Saint-Germain-l'Auxerrois","Cour Carrée","Sèvres – Cité de la Céramique","Parc de Saint-Cloud","Pont Alexandre III","Île Saint-Louis","Parc des Buttes Chaumont","Musée des Arts Forains","Galeries Lafayette Haussmann","Parc Monceau","Marché d'Aligre","Basilica of Saint-Denis","La Défense","Marché Poncelet","Cité de l'Architecture et du Patrimoine","Saint-Eustache","La Cinémathèque Française","Stade de France","Conciergerie","Faubourg Saint-Germain","Marché Bastille","Seine River Trip","Rue Crémieux","Palais-Royal","Musée Picasso","Rue Saint-Honoré","Marché aux Puces de Saint-Ouen","Rue des Martyrs","Disneyland and Walt Disney Studios Park","Palais de Tokyo"]))
pagels.append(HolidayPage("187","New York",["Bay Plaza Shopping Center","Bronx Library Center","Bronx Terminal Market","Bronx Zoo","Crotona Park","Fordham Plaza, Bronx","New York Botanical Garden","Orchard Beach","South County Trailway","Woodlawn Cemetery","Atlantic Terminal","Billie Holiday Theatre","Brooklyn Academy of Music","Brooklyn Book Festival","Brooklyn Brewery","Brooklyn Bridge","Brooklyn Heights Promenade","Brooklyn Public Library","Brooklyn–Queens Greenway","Duff's Brooklyn","Gateway Center","The Invisible Dog Art Center","Kings Plaza","Music Hall of Williamsburg","New York Aquarium","Plumb Beach, Brooklyn","Prospect Park Zoo","Riegelmann Boardwalk","Roulette Intermedium","92nd Street Y","Aaron Davis Hall","African Burial Ground National Monument","Apollo Theater","Brooklyn Bridge","Chelsea Piers","Chrysler Building","Empire State Building","Federal Hall","Fifth Avenue","Governors Island","Grand Army Plaza","Grand Central Terminal","Grant's Tomb","The Great Saunter","Hamilton Grange National Memorial","Headquarters of the United Nations","Icahn Stadium","Irish Hunger Memorial","Lincoln Center for the Performing Arts","Little Red Lighthouse","Macy's Herald Square","Madame Tussauds New York","New York City Half Marathon","Puerto Rican Day Parade","Rockefeller Center","Staten Island Ferry Whitehall Terminal","Statue of Liberty","Theodore Roosevelt Birthplace National Historic Site","Times Square","UAE Healthy Kidney 10K","Vessel","Washington Square Arch","Washington Square Park","James Watson House","Brooklyn–Queens Greenway","Curley's Atlas Hotel and Baths","Marine Pavilion","Poppenhusen Institute","Queens Center","Queens Library","Queens Place Mall","Queens Zoo","Rego Center","Rockaway Beach Hotel","Water Taxi Beach","Battery Weed","Beachland Amusements","Empire Outlets","Francis the Praying Mantis","Happyland Amusement Park","New York Wheel","Postcards","Staten Island Mall","Staten Island Zoo"]))
pagels.append(HolidayPage("188","Venice",["See St Mark's basilica","See Doge's Palace","Get around in a gondola","Tour the Venetian masters of art","Drink like a Venetian – and go on a secret wine tour","Get a bird's-eye view of Venice","Take a trip down the Grand Canal","Get a taste for true Venetian cuisine","Be seduced by the contemporary art scene","Experience (well-played) Vivaldi in Venice","Cool down with a delicious gelato","Go back to school","Walk in James Bond's footsteps","Try on some prison threads","Eat seafood you've never seen before","Pick up a serenissima souvenir","Slip on a mask and join the Carnevale","Take a waterside-bar break","Head out of town on a quick yonder-window break","Take some aperitivo time","Get kitted out in Italian elegance"]))
pagels.append(HolidayPage("189","Rome",["The Colosseum in Rome","Centrale Montemartini","Cimitero cattolico","Stadio Olimpico","Galleria Borghese","Capella Sistina","Auditorium-Parco della Musica","Villa Ada Roma Incontra il Mondo","Museo delle Mura","Nuovo Mercato Esquilino District","Le Domus Romane","San Luigi dei Francesi","Ostia Antica","Terme di Caracalla","Santa Cecilia in Trastevere","Austin Keys","Rome Marathon","Orto Botanico","Palazzo Doria Pamphilj","Vittoriano","Festa de Noantri"]))
pagels.append(HolidayPage("190","Berlin",["Get the train from Potsdamer Platz","Sit in the Dschungel on Nürnberger Strasse","Cross Bösebrücke"]))
pagels.append(HolidayPage("191","Rio de Janeiro",["Christ the Redeemer","Jardim Botânico","Tijuca National Park","Ipanema Beach","Sugar Loaf Mountain (Pão de Açúcar)","Lapa","Prainha","Copacabana Beach","Santa Teresa","Barra da Tijuca","Grumari Beach","Ilha Fiscal"]))
pagels.append(HolidayPage("192","Tokyo",["Yayoi Kusama Museum","Shinjuku Gyoen National Garden","Ginza Six","Senso-ji","Tsukiji Fish Market","Shibuya Crossing","Golden Gai","Nakameguro","Tokyo National Museum","Nezu Museum","Sumo at Ryoguku Kokugikan","Bring friends to Karaoke Kan","Yoyogi Park","Tokyo Skytree","Edo Museum","Bohemian Tokyo in Shimokitazawa","Cat Cafe MOCHA","Origami Kaikan","Kappabashi Street","Yakatabune Harumiya Cruise","Kit Kat Chocolatory","Artificial island of Odaiba","Purikura no Mecca"]))
pagels.append(HolidayPage("193","Brighton",["Brighton Palace Pier","The Lanes","Royal Pavilion","Sea Life Brighton","Brighton Pride party","British Airways i360","Sail into the sunset","Brighton helicopter ride","Brighton Centre","Brighton Toy and Model Museum","Globalls","Brighton Museum & Art Gallery","Brighton Dome"]))
pagels.append(HolidayPage("194","Ibiza",["Dalt Vila UNESCO site","Ibiza Cathedral","Playa d'en Bossa","San Antonio","Talamanca","Santa Eulalia","Punta d'es Moscarter","Cala Comte","Island of Es Vedrà","Spas","Water activities","Food and drink","Aquarium Cap Blanc","Family fun","Formentera"]))
pagels.append(HolidayPage("195","Sydney",["Sydney Harbour Bridge Climb","Carriageworks Farmers Markets","Manly to Spit coastal walk","Saint Peter","Balloon Aloft Camden Valley","Young Henrys","Dharawal National Park Walking Tours","Museum of Contemporary Art (MCA)","Ester Restaurant and Bar","Bondi Icebergs Pool","The Lansdowne Hotel","Sydney HeliTours","Ciccone and Sons Gelateria","Sydney Opera House backstage tour","Love Tilly Devine","Gordon's Bay","Hermitage Foreshore Walk","Continental Deli Bar Bistro","Carriageworks","Sydney Skydivers","Courthouse Hotel","Bondi to Coogee coastal walk","White Rabbit","Watsons Bay Boutique Hotel","Bills","Taronga Zoo","Momofuku Seiobo","The Boathouse Balmoral","The Unicorn Hotel","Sydney by Kayak","Mr Wong","Royal National Park","The Enmore Theatre","Manly Ferry","El Jannah","Wendy's Secret Garden","Let's Go Surfing","Hubert","Clovelly Bowling Club","Din Tai Fung","Camp Cove","Royal Botanic Gardens Sydney","Bare Island","Art Gallery of NSW","Sydney Dance Company","Earl's Juke Joint","Strand Arcade","Sydney Seaplanes","Spice Alley"]))
pagels.append(HolidayPage("196","Toronto",["Toronto Islands","Distillery District","St. Lawrence Market","Harbourfront Centre","Kensington Market","Hockey Hall of Fame","Toronto Zoo","Casa Loma","CN Tower","Royal Ontario Museum","Ontario Science Centre","Fort York"]))
pagels.append(HolidayPage("197","London",["The London Eye","Hampstead Heath","Big Ben","The Docklands Light Railway","London Hackspace","The Houses of Parliament","Trafalgar Square","Leicester Square","King's Cross Platform 9 3/4","The Thames","Oxford Street","Regents Park","Hyde Park","Victoria Park","Buckingham Palace","Luton Airport"]))
pagels.append(HolidayPage("198","Los Angeles",["Venice Beach","Stroll along the stars in Hollywood","Shop in style on Rodeo Drive","Museum of Jurassic Technology","Los Angeles County Museum of Art (LACMA)","Griffith Observatory","Disneyland","The Broad Museum","Watts Towers Arts Center","Walt Disney Concert Hall","Amoeba Music","Cruise along Mulholland","Japanese American National Museum","Huntington Library"]))
pagels.append(HolidayPage("199","Ledbury",["Electromagnetic Field 2018"]))


page1 = TravelIndex("185",pagels)
