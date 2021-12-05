#2d shapes calculator
v = input (' 1.circle\n 2.triangle\n 3.rectangle\n\n ')

if v == '1' :
#calculate circle
    v1 = input ('\n 1.circumference\n 2.area\n\n ')

    if v1 == '1' :
         rd = input('radius: ')
         cc = 2 * 3.1415926536 * int(rd)
         print (cc)
    elif v1 == '2' :
         dr = input ('radius: ')
         ca = 3.1415926536 * int(dr) * int(dr)
         print (ca)
if v == '2' :
#calculate triangle
    v2 = input ('\n 1.perimeter\n 2.area\n\n ')

    if v2 == '2' :
        bse = input ('base: ')
        hght = input ('height: ')
        trgle = int (bse) * int (hght) / 2
        print (trgle)
    elif v2 == '1' :
        bse = input ('base: ')
        hght = input ('height: ')
        sde =input ('side: ')
        p = int(bse) + int (hght) + int (sde)
        print (p)
#calculate rectangle        
#in developing...