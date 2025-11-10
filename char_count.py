# Írjon függvényt, amely egy paraméterként megkapott tetszőleges sztringben megszámolja a karakterek gyakoriságát!

def char_count(text):
    char_dict = {}
    for i in text.upper(): # Nagybetűssé alakítás, hogy ne tegyen külömbséget a kis és nagybetűk között
        if i.isalpha(): # Csak a betűk számítanak más karakterek nem
            if i in char_dict:
                char_dict[i] += 1
            else:
                char_dict[i] = 1
    return char_dict

text = "Hello, world!"

for k, v in char_count(text).items():
    print(f"{k} betűből {v} darab")