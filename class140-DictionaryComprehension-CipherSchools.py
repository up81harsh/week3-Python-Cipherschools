#dictionary comprehension 
# square = {1:1 , 2:4 , 3:9}

square = {num:num*2 for num in range(1,11)}
print(square)

# 1:1
# 2:4
# square of 1:1 
square2= {f"squareof{num} is":num**2 for num in range (1,11)}
for k ,v in square2.items():
    print(f"{k}:{v}")
