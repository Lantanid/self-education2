brra = set(['kitay', 'rushka', 'india'])
a = 'india' in brra
print(a)
a = 'falos' in brra
print(a)
bric = brra.copy()
print(bric)
bric.add('Falos')
print(bric)
a = bric.issuperset(brra)
print(a)
brra.remove('rushka')
print(bric)
a = brra.intersection(bric) #Or brra & bric
print(brra)
print(bric)
print(a)
