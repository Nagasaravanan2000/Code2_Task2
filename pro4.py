lst =[]
n=int(input("Enter the number"))
for i in range(0,n):
  els=int(input())
  lst.append(els)
print("Positive number in the list are:")
for j in range(n):
    if lst[j]>=0:
        print(lst[j], end=' ')
    
