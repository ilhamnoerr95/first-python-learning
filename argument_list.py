# argument list, * this mark reprsent of argument list
# argument list contain data as the parameter input
# argument list only once in function


def total(*list_angka):
    total = 0
    for angka in list_angka:
        total = total + angka
    print(f"total {list_angka} = {total}")



total(10,10,10)