name = 'Caio'
age = '23'
alive = True
writeFile = open('./output.txt', 'w')

prints = (name, age, alive)
lazy = False

print('{} tem {} e está bem q só'.format(name, age), file=writeFile)
writeFile.close()
