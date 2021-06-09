from api_cube.models import Algorithm

pll = {
    'Aa Perm': "x L2 D2 L' U' L D2 L' U L'",
    'Ab Perm': "x' L2 D2 L U L' D2 L U' L",
    'Ga Perm': "R2 U R' U R' U' R U' R2 U' D R' U R D'",
    'Gb Perm': "R' U' R U D' R2 U R' U R U' R U' R2 D",
    'Gc Perm': "R2 U' R U' R U R' U R2 U D' R U' R' D",
    'Gd Perm': "R U R' U' D R2 U' R U' R' U R' U R2 D'",
    'Ja Perm': "x R2 F R F' R U2 r' U r U2",
    'Jb Perm': "R U R' F' R U R' U' R' F R2 U' R'",
    'Ra Perm': "R U' R' U' R U R D R' U' R D' R' U2 R'",
    'Rb Perm': "R2 F R U R U' R' F' R U2 R' U2 R",
    'Na Perm': "R U R' U R U R' F' R U R' U' R' F R2 U' R' U2 R U' R'",
    'Nb Perm': "R' U R U' R' F' U' F R U R' F R' F' R U' R",
    'Ua Perm': "M2 U M U2 M' U M2",
    'F Perm': "R' U' F' R U R' U' R' F R2 U' R' U' R U R' U R",
    'U Perm': "M2 U' M U2 M' U' M2",
    'T Perm': "R U R' U' R' F R2 U' R' U' R U R' F'",
    'E Perm': "x' L' U L D' L' U' L D L' U' L D' L' U L D",
    'V Perm': "R' U R' U' y R' F' R2 U' R' U R' F R F",
    'Y Perm': "F R U' R' U' R U R' F' R U R' U' R' F R F'",
    'H Perm': "M2 U M2 U2 M2 U M2",
    'Z Perm': "M' U M2 U M2 U M' U2 M2",
}

oll = {
    'Oll 1': "R U2 R2 F R F' U2 R' F R F'",
    'Oll 2': "r U r' U2 r U2 R' U2 R U' r'",
    'Oll 3': "r' R2 U R' U r U2 r' U M'",
    'Oll 4': "M U' r U2 r' U' R U' R' M'",
    'Oll 5': "l' U2 L U L' U l",
    'Oll 6': "r U2 R' U' R U' r'",
    'Oll 7': "r U R' U R U2 r'",
    'Oll 8': "l' U' L U' L' U2 l",
    'Oll 9': "R U R' U' R' F R2 U R' U' F'",
    'Oll 10': "R U R' U R' F R F' R U2 R'",
    'Oll 11': "r U R' U R' F R F' R U2 r'",
    'Oll 12': "M' R' U' R U' R' U2 R U' R r'",
    'Oll 13': "F U R U' R2 F' R U R U' R'",
    'Oll 14': "R' F R U R' F' R F U' F'",
    'Oll 15': "l' U' l L' U' L U l' U l",
    'Oll 16': "r U r' R U R' U' r U' r'",
    'Oll 17': "F R' F' R2 r' U R U' R' U' M'",
    'Oll 18': "r U R' U R U2 r2 U' R U' R' U2 r",
    'Oll 19': "r' R U R U R' U' M' R' F R F'",
    'Oll 20': "r U R' U' M2 U R U' R' U' M'",
    'Oll 21': "R U2 R' U' R U R' U' R U' R'",
    'Oll 22': "R U2 R2 U' R2 U' R2 U2 R",
    'Oll 23': "R2 D' R U2 R' D R U2 R",
    'Oll 24': "r U R' U' r' F R F'",
    'Oll 25': "F' r U R' U' r' F R",
    'Oll 26': "R U2 R' U' R U' R'",
    'Oll 27': "R U R' U R U2 R'",
    'Oll 28': "r U R' U' r' R U R U' R'",
    'Oll 29': "R U R' U' R U' R' F' U' F R U R'",
    'Oll 30': "F R' F R2 U' R' U' R U R' F2",
    'Oll 31': "R' U' F U R U' R' F' R",
    'Oll 32': "L U F' U' L' U L F L'",
    'Oll 33': "R U R' U' R' F R F'",
    'Oll 34': "R U R2 U' R' F R U R U' F'",
    'Oll 35': "R U2 R2 F R F' R U2 R'",
    'Oll 36': "L' U' L U' L' U L U L F' L' F",
    'Oll 37': "F R' F' R U R U' R'",
    'Oll 38': "R U R' U R U' R' U' R' F R F'",
    'Oll 39': "L F' L' U' L U F U' L'",
    'Oll 40': "R' F R U R' U' F' U R",
    'Oll 41': "R U R' U R U2 R' F R U R' U' F'",
    'Oll 42': "R' U' R U' R' U2 R F R U R' U' F'",
    'Oll 43': "F' U' L' U L F",
    'Oll 44': "F U R U' R' F'",
    'Oll 45': "F R U R' U' F'",
    'Oll 46': "R' U' R' F R F' U R",
    'Oll 47': "R' U' R' F R F' R' F R F' U R",
    'Oll 48': "F R U R' U' R U R' U' F'",
    'Oll 49': "r U' r2 U r2 U r2 U' r",
    'Oll 50': "r' U r2 U' r2 U' r2 U r'",
    'Oll 51': "F U R U' R' U R U' R' F'",
    'Oll 52': "R U R' U R U' B U' B' R'",
    'Oll 53': "l' U2 L U L' U' L U L' U l",
    'Oll 54': "r U2 R' U' R U R' U' R U' r'",
    'Oll 55': "R' F R U R U' R2 F' R2 U' R' U R U R'",
    'Oll 56': "r' U' r U' R' U R U' R' U R r' U r",
    'Oll 57': "R U R' U' M' U R U' r'",
}


def slugify(alg):
    return alg.replace(' ', '-')


def run():
    for alg in pll:
        Algorithm.objects.get_or_create(
            classification='PLL',
            alg_name=alg,
            slug=slugify(alg),
            moves=pll[alg]
        )

    for alg in oll:
        Algorithm.objects.get_or_create(
            classification='OLL',
            alg_name=alg,
            slug=slugify(alg),
            moves=oll[alg]
        )
