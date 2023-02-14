img = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1, 0, 0, 1, 1, 0],
        [0, 1, 1, 1, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 1, 0, 0, 0, 0, 1, 1, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

def erosion(img, n):
    result = []
    coordine_a_enlever_x = []
    coordine_a_enlever_y = []

    for number_of_tries in range(n):
        for line in range(len(img[0])):
            img[0][line] = 0
            img[-1][line] = 0
        for coordone_x in range(len(img)):
            for coordone_y in range(len(img[0])):
                if coordone_y + 1 < len(img[0])  and coordone_x + 1 < len(img) and coordone_x > 0 and coordone_y > 0:

                    if img[coordone_x][coordone_y - 1] == 0 or img[coordone_x-1][coordone_y] == 0 or img[coordone_x + 1][coordone_y] == 0 or img[coordone_x][coordone_y + 1] == 0:
                        coordine_a_enlever_x.append(coordone_x)
                        coordine_a_enlever_y.append(coordone_y)
                    else: 
                        img[coordone_x][coordone_y] = 1
                else:
                    img[coordone_x][coordone_y] = 0
        for number in range(len(coordine_a_enlever_x)):
            img[coordine_a_enlever_x[number]][coordine_a_enlever_y[number]] = 0

    for row in img:  
        result.append(''.join(['#' if color_value == 1 else '.' for color_value in row]))
    return '\n'.join(result) 
              
    

print(erosion(img,1))