#shape calculator
#only works on pyhton 3.10.2 and up!
while True:
    v = input (' 1.circle\n a1.sphere\n 2.triangle\n b1.pyramid vol\n b2.cone vol\n 3.rectangle\n 4.square\n\n"press 0 to exit"\n select: ')
    if v == '0':
        break
    match v:
        case '1': #circle
            v1 = input ('\n 1.circumference\n 2.area\n\n select: ')
            match v1:
                case '1':
                    rd = input('radius: ')
                    print (2 * 3.1415926536 * int(rd)) #circle circum
                case '2':
                    dr = input ('radius: ')
                    print(3.1415926536 * int(dr) * int(dr)) #circle area

        case 'a1': #sphere
            vsphere = input('\n 1.volume\n 2.surface area\n\n select: ')
            match vsphere:
                case '1':
                    volsphere = input('radius: ')
                    print(4/3 * 3.1415926536 * int(volsphere)**3) #sphere vol
                case '2':
                    srf = input('radius: ')
                    print(4 * 3.1415926536 * int(srf)**2) #sphere area

        case '2': #triangle
            v2 = input ('\n 1.perimeter\n 2.area\n\n select: ')
            match v2:
                case '1':
                    bse, hght, sde = input ('side A, side B, side C: ').split()
                    print (int(bse) + int (hght) + int (sde)) #triangle peri
                case '2':
                    bse, hght = input ('base, height: ').split()
                    print (int (bse) * int (hght) / 2) #triangle area

        case 'b1': #pyramid
            w, l, h = input('base width, base lenght, height: ').split()
            print(int(l) * int(w) *int(h) / 3) #pyramid

        case 'b2': #cone
            r, h = input('radius, height: ').split()
            print(3.1415926536 * int(r)**2 * int(h)/3) #cone vol

        case '3': #rectangle
            v3 = input('\n 1.perimeter\n 2.area\n\n select: ')
            match v3:
                case '1':
                    a, b, = input('width, height: ').split()
                    print(2 * (int(a) + int(b))) #recta peri
                case '2':
                    a, b = input('width, height: ').split()
                    print(int(a) * int(b)) #recta area

        case '4': #square
            vsq = input('\n 1.perimeter\n 2.area\n\n select: ')
            match vsq:
                case '1':
                    vlsqr = input('side: ')
                    print(int(vlsqr)*2) #square peri
                case '2':
                    vlsqr2 = input('side: ')
                    print(int(vlsqr2)**2) #square area