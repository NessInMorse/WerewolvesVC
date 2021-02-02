class Role:
        def __init__(self, faction, role, description):
                self.faction = faction
                self.role = role
                self.description = description
                

        def giveDescription(self):
                print(f"{'-'*30}\n"
                      f"You are {self.role}\n" +
                      f"You {self.description}\n" +
                      f"You win with the {self.faction}")
        

def main():
        rolelist = [Role("Werewolves","Sherlock Wolves","will search for the exact role of a town person each night",),
                    Role("Neutrals","Lucifer","can ignite someone each odd night, gives charges to Lilith"),
                    Role("Neutrals","Lilith","can decide to heal or kill someone each night with charges from Lucifer")
                    ]
        for i in rolelist:
                i.giveDescription()
        print(rolelist)
main()
