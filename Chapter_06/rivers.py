rivers = {'nile': 'egypt',
          'yangtze': 'china',
          'amazon': 'brazil',
          'volga': 'russia',
          'mississippi': 'united states of america'
          }
for keys, value in rivers.items():
    print(f"The {keys.title()} runs through {value.title()}.")