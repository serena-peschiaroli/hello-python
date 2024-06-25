vals = [12, 9, 4, 21, 11]
vals_sum = 0

i=0

while i<len(vals):
    vals_sum = vals_sum+vals[i]
    i+=1
vals_mean = vals_sum/len(vals)



n = int(input("Fino a che numero vuoi contare? "))
i = 0
while i<=n:
    if i%2:
        print(f"{i}  dispari ")
    else:
        print(f"{i} è pari")
    i+=1
    
    
shopping_list = ["Riso", "latte", "pane", "vino", "yourt", "birra"]

i=0
print("la mia lista della spesa")
while i<len(shopping_list):
    print(f"{i +1}) {shopping_list[i]}")
    i+=1