from player import Player
from weapon import Gun
import msvcrt


def hplayer():
    hpinp = int(input("Player HP: "))
    return Player(hpinp)


def hweapon():
    powerinp = int(input("Weapon Power: "))
    ammoinp = int(input("Weapon Ammo: "))
    return Gun(powerinp, ammoinp)


def startgame(pl, gn):
    hp = pl.HP
    power = gn.Power
    ammo = gn.Ammo

    while True:
        if hp > 0 and ammo > 0:
            hp -= power
            ammo -= 1

        if hp <= 0:
            if ammo == 0:
                print("Player died!")
                break
        elif ammo == 0:
            if hp > 0:
                print("Not enough ammo!")
                break
            if hp <= 0:
                print("Player died!")
                break


def main():
    print("Welcome to my first game!\n")
    startgame(hplayer(), hweapon())
    msvcrt.getch()


main()
