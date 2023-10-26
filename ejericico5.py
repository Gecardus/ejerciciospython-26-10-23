jugador1=input("Jugador 1 digues si treus pedra,paper o tisores: ")
jugador2=input("Jugador 2 digues si treus pedra,paper o tisores: ")
tisores="tisores"
pedra="pedra"
paper="paper"
if jugador1==pedra and jugador2==tisores:
    print("Guanya jugador 1")
elif jugador1==tisores and jugador2==paper:
    print("Guanya jugador 1")
elif jugador1==paper and jugador2==pedra:
    print("Guanya jugador 1")
elif jugador2==pedra and jugador1==tisores:
    print("Guanya jugador 2")
elif jugador2==tisores and jugador1==paper:
    print("Guanya jugador 2")
elif jugador1==jugador2:
    print("Hi ha hagut un empat")
else:
    print("Guanya jugador 2")