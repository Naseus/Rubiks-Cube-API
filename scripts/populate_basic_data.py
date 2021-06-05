from api_cube.models import Algorithm

pll = {
    'JaPerm': '',
}

oll = {
    'Sune': '',
}


def run():
    for alg in pll:
        Algorithm.objects.get_or_create(
            classification='PLL',
            alg_name=alg,
            slug=alg,
            moves=pll[alg]
        )

    for alg in oll:
        Algorithm.objects.get_or_create(
            classification='OLL',
            alg_name=alg,
            slug=alg,
            moves=pll[alg]
        )
