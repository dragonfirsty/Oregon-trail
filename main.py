from villagers.villager import Villager,Mage

def main():
    roberto = Villager('Roberto')
    #dados do villager roberto
    print(vars(roberto))
    #Checando vida do villager roberto
    print(roberto.check_health(10))
    print(roberto.health)

    jorge = Mage('Jorge')
    #dados do mago jorge
    print(vars(jorge))


if __name__ == '__main__':
    main()
