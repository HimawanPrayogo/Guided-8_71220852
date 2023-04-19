print("diamond.txt")


a=open("diamond.txt","w")

n=int(input("Masukkan angka:"))

diamond=""

for i in range(n):
    if i<=n/2:
        diamond+=" "*(n//2-i)+"*"*(2*i+1)+"\n"

    else:
        diamond+=" "*(i-n//2)+"*"*(2*(n-i)-1)+"\n"

a.write(diamond)
a.close()
