from utils import coord2merc, merc2coord

if __name__ == '__main__':

    a = coord2merc(37, 5)
    b= merc2coord(a)
    print(str(a))
    print(str(b))