from random import randint, choice

class Role:
        def __init__(self, faction, role, description):
                self.faction = faction
                self.role = role
                self.description = description


        def giveDescription(self):
                print(f"{'-'*30}\n" + 
                      f"Je bent {self.role}\n" +
                      f"Je {self.description}\n" +
                      f"Je wint met {self.faction}")


def writeRoleNotes(rolenames: list,
                   determined_roles: list,
                   names: list,
                   version: str)\
                   -> print:
        infile = open("GAME.txt", "w", encoding='utf-8')
        volgorde = []
        if version == "L":
                FULL_NAME = {"0ti": "Town Information",
                      "1tk": "Town Killing",
                      "2tp": "Town Protective",
                      "3ts": "Town Support",
                      "4ds": "Random Town",
                      "4rt": "Random Town",
                      "5nt": "Neutral",
                      "5cp": "Neutral",
                      "6wp": "Werewolf Power",
                      "7ws": "Werewolf Support",
                      "Ywr": "Random Werewolf",
                      "9wi": "Werewolf Information",
                      "Zwelp": "Welp"}

        else:
                FULL_NAME = {"0ti": "Town Information",
                      "1tk": "Town Killing",
                      "2tp": "Town Protective",
                      "3ts": "Town Support",
                      "4ds": "Random Town",
                      "4rt": "Random Town",
                      "5nt": "Neutral",
                      "5cp": "Neutral",
                      "6wp": "Werewolf Power",
                      "7ws": "Werewolf Support",
                      "8wd": "Werewolf Deception",
                      "9wi": "Werewolf Information",
                      "Zwelp": "Welp"}
        infile.write(f"HOST{'-'*15}{'LEKEN'*(version=='L')}{'DISCORD'*(version=='D')}{'WHATSAPP'*(version=='W')}{'-'*15}\n")
        infile.write(f"{'SPACE':20}\t{'ROLE':24}\t{'NAME':20}\n{'_'*30}\n")

        for i in range(len(rolenames)):
                name = choice(names)
                names.remove(name)
                volgorde.append(name)
                infile.write(f"{FULL_NAME[rolenames[i]].upper():20}"+
                             f"\t{determined_roles[i].upper():24}" + 
                             f"\t{name}\n")

        infile.write(f"\nPLAYERS{'-'*30}\n")
        infile.write(f"{'SPACE':20}\n{'_'*30}\n")
        for i in range(len(rolenames)):
                infile.write(f"{FULL_NAME[rolenames[i]].upper():20}\n")

        infile.write(f"\n\nSCRIPT{'-'*15}\n")
        infile.write(f"```\n")
        for i in range(len(volgorde)):
                infile.write(f"Beste {volgorde[i].capitalize()}, je bent een {determined_roles[i].capitalize()}\n\n")
        infile.write(f"```")

        infile.close()



def returnGame_Role_list(game_list: list,
                         element_list: list,
                         mode = "D")\
                         -> (list):
        koppel_coin = randint(0,1)
        if koppel_coin and len(element_list[1]) > 1 and mode != "L":
                for i in range(2):
                        game_list[game_list.index("5nt")] = "5cp"
        schaapje_coin = randint(0,7)
        if not schaapje_coin and len(element_list[0]) > 7 and "4rt" in game_list:
                game_list[game_list.index("4rt")] = "4ds"
        elif mode == "L" and randint(0,1) and "4rt" in game_list:
                game_list[game_list.index("4rt")] = "4ds"

        if mode == "W":
                # whatsapp-unique roles: 
                # de medium, de postbode, de chatverslaafde
                ALL_ROLES = {"0ti": ["de blinde politieman", "de oude programmeur", "de stalker", "de chatverslaafde", "de verrekijker"],
                             "1tk": ["de jageres", "de complotdenker", "De Holy Knight"],
                             "2tp": ["de PTSS'er", "Yeti", "Smid"],
                             "3ts": ["de dokter", "de postbode", "de medium", "de busbestuurder","de locker", "de directeur"],
                             "4rt": ["de blinde politieman", "de oude programmeur", "de stalker", "de chatverslaafde",
                                     "de jageres", "de complotdenker",
                                     "de PTSS'er", "Yeti", "Smid",
                                     "de dokter", "de postbode", "de medium",
                                     "de busbestuurder","de locker", "de directeur"],
                             "4ds": ['het dorpsschaapje'],
                             "5nt": ["de weerhamster", "de pyromaan","de grave digger", "de hacker", "de dictator"],
                             "5cp": ["Lilith♥", "Lucifer♥"],
                             "6wp": ["de rage wolf", "Cthulhu"],
                             "7ws": ["knuffelwolf", "Na-aap wolf"],
                             "8wd": ["de witwasser","de hypnowolf", "de OCD wolf"],
                             "9wi": ["Sherlock Wolves", "de schaduw wolf"],
                             "Zwelp": ["Welp"]}
        elif mode == "D":
                # removed roles:
                # de medium, de postbode, de chatverslaafde, Cthulu
                ALL_ROLES = {"0ti": ["de blinde politieman", "de oude programmeur", "de stalker", "de verrekijker"],
                             "1tk": ["de jageres", "de complotdenker", "De Holy Knight"],
                             "2tp": ["de PTSS'er", "Yeti", "Smid"],
                             "3ts": ["de dokter", "de busbestuurder","de locker", "De directeur"],
                             "4rt": ["de blinde politieman", "de oude programmeur", "de stalker",
                                     "de jageres", "de complotdenker",
                                     "de PTSS'er", "Yeti", "Smid",
                                     "de dokter","de busbestuurder","de locker","de directeur"],
                             "4ds": ["het dorpsschaapje"],
                             "5nt": ["de weerhamster", "de pyromaan","de grave digger", "de hacker", "de dictator"],
                             "5cp": ["Lilith♥", "Lucifer♥"],
                             "6wp": ["de rage wolf"],
                             "7ws": ["knuffelwolf", "Na-aap wolf"],
                             "8wd": ["de witwasser","de hypnowolf", "de OCD wolf"],
                             "9wi": ["Sherlock Wolves", "de schaduw wolf"],
                             "Zwelp": ["Welp"]}
        elif mode == "L":
                for i in game_list:
                        ALL_ROLES = {"0ti": ["Sheriff", "stalker", "ooggetuige"],
                                "1tk": ["Soldaat", "complotdenker", "beul"],
                                "2tp": ["Locker", "Yeti"],
                                "3ts": ["vervloekte", "slet"],
                                "4rt": ["Sheriff", "stalker","ooggetuige"
                                        "Soldaat", "Complotdenker","beul"
                                        "Locker", "Yeti",],
                                "4ds": ["dorpsschaapje"],
                                "5nt": ["pyromaan","grave digger", "dienstmeisje"],
                                "6wp": ["rage wolf"],
                                "7ws": ["knuffelwolf"],
                                "Ywr": ["knuffelwolf", "Sherlock Wolves", "schaduw wolf"],
                                "9wi": ["Sherlock Wolves", "schaduw wolf"],
                                "Zwelp": ["Welp"]}


        determined_roles = []
        c = 0 
        for role in game_list:
                if role != "5cp":
                        determined_roles.append(choice(ALL_ROLES[role]))
                else:
                        determined_roles.append(ALL_ROLES[role][c])
                        c += 1 
        return determined_roles


def returnPlayer_Role_list(element_list: list, mode="D") -> (list):
        game_list = []
        #town
        for i in range(len(element_list[0])):
                if i % 8 == 0 and i != 0:
                        game_list.append("3ts")
                elif i % 5 == 0 or i == 0:
                        game_list.append("0ti")
                elif i % 6 == 0 and i != 0:
                        game_list.append("1tk")
                elif i % 7 == 0 and i != 0:
                        game_list.append("2tp")
                else:
                        game_list.append("4rt")

        #neutrals
        for i in range(len(element_list[1])):
                game_list.append("5nt")

        if mode != "L":
                # werewolves
                for i in range(len(element_list[2])):
                        if i == 0:              # power
                                game_list.append("6wp")
                        elif i % 4 == 0:        # special
                                game_list.append("7ws")
                        elif i % 3 == 0:        # deception
                                game_list.append("8wd")
                        elif i % 2 == 0:        # information
                                game_list.append("9wi")
                        else:
                                game_list.append("Zwelp")
        
        else:
                for i in range(len(element_list[2])):
                        if i == 0:              # power
                                game_list.append("6wp")
                        elif i % 4 == 0:        # special
                                game_list.append("7ws")
                        elif i % 3 == 0:        # deception
                                game_list.append("Ywr")
                        elif i % 2 == 0:        # information
                                game_list.append("9wi")
                        else:
                                game_list.append("Zwelp")
        return sorted(game_list)


def returnPlayer_list(n: int) -> list:
        element_list = [[],[],[]]
        for i in range(n):
                if i == 0:
                        element_list[0].append("t")
                elif i % 3 == 0:
                        element_list[2].append("w")
                elif i % 5 == 0:
                        element_list[1].append("n")
                else:
                        element_list[0].append("t")
        return element_list


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
                    Role(town, "de PTSS'er", "zal zeker sterven na 5 dagen, maar kan voor die tijd niet dood gaan, "+
                                "als je wordt aangevallen / opgehangen mag je iemand aanwijzen die in plaats van jou zal sterven"),
                    Role(town, "Yeti", "kan 3 keer kiezen om naar buiten te gaan en elke actie een 50% kans geven van falen."),
                    Role(town, "Smid",  "kan elke nacht jezelf of een ander een zwaard geven om jezelf of iemand anders tegen de wolven te verdedigen"),
                    Role(town, "de jageres", "kan twee schieten op mensen in het dorp"),
                    Role(town, "de complotdenker", "kan 3 keer op alert gaan en daarbij iedereen die hem bezoekt vermoorden"),
                    Role(town, "de Holy Knight", "kan elke nacht iemand 'unworthy' verklaren, waarbij die persoon niet mag stemmen de komende dag"),
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
                    Role(werewolf, "de schaduw wolf", "kan elke nacht van twee personen zien wie ze bezoeken"),
                    Role(werewolf, "Rage wolf", "kan 1 keer in het spel opgeven om in 'rage modus' te gaan waarbij iedereen die dat huis bezoekt zal sterven"),
                    Role(werewolf, "Cthulu", "iedereen die hetzelfde persoon bezoekt als cthulu zal de volgende dag niet kunnen praten van angst"),
                    Role(werewolf, "witwasser", "kan elke nacht een van de weerwolven witwassen waarbij de rol op een andere rol lijkt"),
                    Role(werewolf, "De hypnowolf", "Kan elke nacht iemand bezoeken met misinformatie, zoals dat iemand is bestuurd door de busbestuurder " +
                                        "of is aangevallen, maar dat de smid hun leven heeft gered." ),
                    Role(werewolf, "OCD wolf", "kan 2 keer in het spel een aanval van de weerwolven cleanen waarbij de rol van de dode onherkenbaar is " +
                                "echter weet jij dan wel welke rol die persoon had"),
                    Role(werewolf, "Welp", "weet in eerste instantie niet wie zijn teamgenoten zijn, maar mag na 3 nachten kiezen welke soort wolf hij wordt"),
                    Role(werewolf, "Knuffelwolf", "mag elke nacht iemand uitkiezen om hun actie te doen laten falen"),
                    Role(werewolf, "de Na-aap wolf", "kan elke nacht iemand nadoen en krijgt vervolgens de informatie die die persoon heeft verworven" +
                                "Je ziet er dus voor informatierollen hetzelfde eruit als de echte rol die je bezoekt, ook in het graf zal je er zo uit zien")
                    ]
        while True:
                document = open("name.txt","r")
                names = [i.upper() for i in document.read().split("\n")]
                document.close()
                print(names)


                gamemode = "fill"
                while gamemode not in "WDL" or len(gamemode) != 1:
                        gamemode = input("Welke vorm van het spel wil je spelen? Whatsapp [W], Discord [D] of Leken Editie [L]\n" +
                                        "(De discord versie is gelimiteerder door het gebruik van voice chat en minder tijd)\n").upper()

                element_list = returnPlayer_list(len(names))
                player_list = returnPlayer_Role_list(element_list, gamemode)
                # print(player_list)
                determined_roles = returnGame_Role_list(player_list, element_list, gamemode)
                # for i in rolelist:
                #        i.giveDescription()
                # print(len(element_list[0]),len(element_list[1]),len(element_list[2]))
                # print(element_list)
                # print(player_list)
                # print(determined_roles)
                writeRoleNotes(player_list, determined_roles, names, gamemode)
main()
