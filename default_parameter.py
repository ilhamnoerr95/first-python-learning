# default argument value, parameter in def or function is strict

def say_gelo(name="bambang", last_name=""): 
    print(f"Gelo lu {name} - {last_name}")

say_gelo("wajib isi")

# specific input param, not have to fill up first param
say_gelo(last_name="biji")
