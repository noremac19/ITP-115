


faces = ["heads","tails"]
def coin ():

def experiment():
    flips = 0
    heads = 0
    # loop until heads = 3
    while heads < 3:
        flip = coin()
        flips += 1
        if flip == "heads":
            heads += 1
        else:
            heads = 0

    return flips
def main():

main()
