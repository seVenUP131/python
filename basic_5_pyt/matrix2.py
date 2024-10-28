rows = 3
cols = 3


start_value = 100


for i in range(rows):
    for j in range(cols):
        
        value = start_value + (i * cols + j) * 2
        
        print(f"{value:3}", end=' ')
    print()  