cities = {'laayoune': {'population': 300_000, 'country': 'Morocco', 'fact': 'Laayoune means \'water sources\' in Arabic'},
          'agadir': {'population': 1_000_000, 'country': 'Morocco', 'fact': 'Agadir was the premier sardine port in the world in the 1980s'},
          'marrakech': {'population': 1_200_000, 'country': 'Morocco', 'fact': 'Marrakech has another name which is the Red City'}
          }
for key, value in cities.items():
    print(f"\n{key.title()}:")
    for key_1, value_1 in value.items():
        print(f"\t{key_1.title()}: {value_1}")