n = int(input("Tabuada: "))

y = int(input("Até que numero da tabuada você quer que vá ex: 4x\"100\": "))

for c in range(1,y + 1):

    print("{} x {} = {}".format(n, c, n*c))

