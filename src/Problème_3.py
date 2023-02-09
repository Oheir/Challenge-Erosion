img = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
]

def erosion(img, n):
    position_to_know = [(-1,0),(1,0),(0,-1),(0,1)]
    for i in range(n):
        positive_value = []
        result = []
        y = 0
        for x in img:
            print(img[y-1])
            print(len(img))
            print(y)
            for i in range(len(x)):
                if x[i] == 1:
                    
                    if y + 1 > len(x):
                        x[i] = 0
                    if img[y-1][i] or img[y+1][i] == 0:
                        x[i] = 0
            for i in range(len(x)):
                if x[i] == 1:
                    if x[i-1] or x[i+1] == 0:
                        x[i] = 0 
            if y +1  != len(img) :
                y += 1
            else: 
                for i in range(len(x)):
                    x[i] = 0
    result = []
    for row in img:  
        result.append(''.join(['#' if color_value == 1 else '.' for color_value in row]))
    return '\n'.join(result) 
              
    

print(erosion(img,1))