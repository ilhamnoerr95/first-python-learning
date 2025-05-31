# method return value

def result(*list_angka):
    total = 0
    for angka in list_angka:
        total = total + angka

    # ini sudah menyimpan data total
    return total

# dijadikan sebuah variable
biji = result(10,10,10)

#print hasil dari return dr function result
print(biji)

print("=================")
def result2(*list_angka):
    totals = 0
    for angka in list_angka:
        totals = totals + angka
    # menggunakan tupple untuk mereturn data agar data bisa di object structuring seperti js
    return (list_angka, totals)

# seperti object struturing
list_angka , totals = result2(5,5,5)

print(f"{list_angka} = {totals}")


