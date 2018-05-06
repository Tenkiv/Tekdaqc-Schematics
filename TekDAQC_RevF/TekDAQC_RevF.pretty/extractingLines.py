debug = 0

text = open('TENKIV_INFO_BLOCK.kicad_mod', 'r')
newText = open('zz.txt', 'w')

for line in text:
    state = 0
    xy = 0
    coordinate = ''
    for char in line:
        '''print(char, end='')'''
        if char == 'x':
            state = 1
        elif state == 1 and char == 'y':
            state = 2
            xy = xy+1
            if (debug):
                print('found xy')
            continue
        elif state < 2:
            state = 0

        if state == 2: #x
            if char != '.':
                coordinate = coordinate + char
            else:
                if (debug):
                    print('\tcoordinateX: ', coordinate)
                if float(coordinate) > 9.8 and float(coordinate) < 11.8:
                        coordinate = ''
                        state = 3
                else:
                    break
        elif state == 3:
            if char == ' ':
                state = 4
        elif state == 4: #y
            if char != '.':
                coordinate = coordinate + char
            else:
                if (debug):
                    print('\tcoordinateY: ', coordinate)
                if float(coordinate) < -4.9:
                    if (xy == 4):
                        print(line)
                        newText.write(line)
                        coordinate = ''
                        state = 0
                        break
                    else:
                        coordinate = ''
                        state = 0
                else:
                    break
            
            
