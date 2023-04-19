a=open("daftarbuku.txt")
nama=input("Nama buku:").lower()

l=0

for i in a:
    d=i.split(",")
    buku=d[0].lower()
    l+=1

    if nama==buku:
        print("buku ditemukan")
        print("Nama:",d[0])
        print("Kode:",d[1])
        print("Tahun rilis:",d[2])
        print("Deskripsi:",d[3])
        break

    elif nama!=buku:
        l<=1

    else:
        print("buku tidak ditemukan")
        break
