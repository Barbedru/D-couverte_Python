import random


def choix_joueur() -> str:
    while True:
        choix = input("Faites votre choix (pierre, feuille, ciseaux) : ")
        if valider_saisie(choix):
            return choix
        print("Choix invalide, réessayez.\n")


def valider_saisie(choix_joureur: str) -> bool:
    choix_valide = choix_joureur in ["pierre", "feuille", "ciseaux"]
    return choix_valide


def choix_ordi() -> str:
    choix_ordi = random.choice(["pierre", "feuille", "ciseaux"])
    return choix_ordi


def comparer(choix_joueur: str, choix_ordi: str) -> str:
    if choix_joueur == choix_ordi:
        return "Égalité"
    if (
        (choix_joueur == "pierre" and choix_ordi == "ciseaux")
        or (choix_joueur == "feuille" and choix_ordi == "pierre")
        or (choix_joueur == "ciseaux" and choix_ordi == "feuille")
    ):
        return "Gagné"
    else:
        return "Perdu"


if __name__ == "__main__":
    choix = choix_joueur()
    if valider_saisie(choix):
        ordi = choix_ordi()
        resultat = comparer(choix, ordi)
        print(f"Ordi a choisi : {ordi}")
        print(f"Resultat : {resultat}")
