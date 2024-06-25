vals = [12, 9, 4, 21, 11]
vals_sum = 0

for val in vals:
    vals_sum = vals_sum+val
vals_mean = vals_sum/len(vals)

shopping_list = ["Riso", "latte", "pane", "vino", "yourt", "birra"]

print("la mia lista della spesa")

for item in shopping_list:
    print("-" + item)
    
list(enumerate(shopping_list))
    
    
list(range(1,10))

n = int(input("fino a che numero vuoi stampare? "))

for i in range(n):
    print("%d è %s" % (i, "dispari" if i%2 else "pari"))