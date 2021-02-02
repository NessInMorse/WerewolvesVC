class Role:
        def __init__(self, faction, role, description):
                self.faction = faction
                self.role = role
                self.description = description
                

        def giveDescription(self):
                print(f"{'-'*30}\n"
                      f"Je bent {self.role}\n" +
                      f"Je {self.description}\n" +
                      f"Je wint met {self.faction}")
        

def returnNumber(a: str) -> int:
        if a.isdigit():
                return int(a)
        else:
                return 0

def main():
        town = "de dorpelingen"
        werewolf = "de weerwolven"
        neutral = "de neutrals"
        rolelist = [Role(town, "de Blinde Politieman", "geeft elke nacht een persoon op en krijgt 3 rollen terug"),
                    Role(town, "de oude programmeur", "geeft elke nacht een rol op en krijgt 5 namen terug"),
                    Role(town, "de stalker", "kan elke nacht zien wie iemand bezoekt"),
                    Role(town, "de chatverslaafde", "kan elke nacht 1 bericht bekijken of die waar is"),
                    Role(town, "de PTSS'er", "zal zeker sterven na 5 dagen, maar kan voor die tijd niet dood gaan"),
                    Role(town, "Yeti", "kan 3 keer kiezen om naar buiten te gaan en elke actie een 50% kans geven van falen."),
                    Role(town, "Smid",  "kan elke nacht jezelf of een ander een zwaard geven om jezelf of iemand anders tegen de wolven te verdedigen"),
                    Role(town, "de jageres", "kan twee schieten op mensen in het dorp"),
                    Role(town, "de complotdenker", "kan 3 keer op alert gaan en daarbij iedereen die hem bezoekt vermoorden"),
                    Role(town, "de dokter", "kan elke nacht bij iemand op bezoek en daarbij een gok uitbrengen, dossier wordt uitgebracht bij dood"),
                    Role(town, "de postbode", "kan elke nacht een brief doorgeven van het ene naar het andere persoon"),
                    Role(town, "de medium", "kan elke nacht met de doden praten"),
                    Role(town, "de busbestuurder", "wisselt elke nacht 2 mnesen om, actie faalt als de locker een huis heeft opgesloten"),
                    Role(town, "de locker", "locked een huis compleet af, waardoor geen enkel mens naar binnen of buiten kan komen"),
                    Role(neutral, "Weerhamster","kan elke nacht iemand toevoegen aan je cult, " +
                                "die vervolgens alleen nog met jou kunnen winnen; " +
                                "je kan niet dood door de weerwolven in de nacht"),
                    Role("Lucifer", "Lilith", "kan elke 2 nachten iemand vermoorden om Lucifer kracht te geven, wanneer de weerwolven dood zijn wordt dit elke nacht."),
                    Role("Lilith", "Lucifer", "kan elke nacht met een kracht van Lilith iemand bezoeken en je komt dan achter de exacte rol van die persoon, " +
                                "of je mag iemand genezen ofwel doden."),
                    Role(neutral, "Grave digger", "kan een rol kiezen van iedereen die dood is en je wordt vervolgens die rol" ),
                    Role(neutral, "Hacker", "kan 3 nachten achter elkaar de rol van een individu aanpassen (maar niet de faction), " +
                                "de derde nacht wisselt de hacker met de rol van de laatste persoon en wordt lid van die factie"),
                    Role("alleen", "Dictator", "Kan 1 keer in het spel een gok doen van alle rollen van de mensen die levend zijn. " + 
                                "Als de gok van de dictator goed is dan zal hij als enige het spel winnen. " +
                                "Heeft hij het mis, dan wordt hij een jageres zonder kogels."),
                    Role(werewolf, "Sherlock Wolves", "vindt de exacte rol van een speler",),
                    Role(werewolf, "Rage wolf", "kan 1 keer in het spel opgeven om in 'rage modus' te gaan waarbij iedereen die dat huis bezoekt zal sterven"),
                    Role(werewolf, "Cthulu", "iedereen die hetzelfde persoon bezoekt als cthulu zal de volgende dag niet kunnen praten van angst"),
                    Role(werewolf, "witwasser", "kan elke nacht een van de weerwolven witwassen waarbij de rol op een andere rol lijkt"),
                    Role(werewolf, "OCD wolf", "kan 2 keer in het spel een aanval van de weerwolven cleanen waarbij de rol van de dode onherkenbaar is " +
                                "echter weet jij dan wel welke rol die persoon had"),
                    Role(werewolf, "Welp", "weet in eerste instantie niet wie zijn teamgenoten zijn, maar mag na 3 nachten kiezen welke soort wolf hij wordt"),
                    Role(werewolf, "Knuffelwolf", "mag elke nacht iemand uitkiezen om hun actie te doen laten falen")
                    ]
        player_list = []
        element_list = [[],[],[]]
        b = 0
        while b < 4:
                b = input("Met hoeveel spelers speel je?\n")
                b = returnNumber(b)
        for i in range(b):
                if i == 0:
                        player_list.append("t")
                        element_list[0].append("t")
                elif i % 3 == 0:
                        player_list.append("w")
                        element_list[2].append("w")
                elif i % 5 == 0:
                        player_list.append("n")
                        element_list[1].append("n")
                else:
                        player_list.append("t")
                        element_list[0].append("t")
        print(len(element_list[0]),len(element_list[1]),len(element_list[2]))
        print(element_list)
        #for i in rolelist:
        #        i.giveDescription()
main()
