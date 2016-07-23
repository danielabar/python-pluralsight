def modify(k):
    k.append(39) # side effect, modifies the input
    print("k =", k)

def main(list):
    modify(list)

if __name__ == "__main__":
    main(sys.argv[1])
