string = "Programozás"
example_list = ["P", "y", "t", "h", "o", "n"]

print(string[:])                   # teljes másolat
print(string[:2])                  # elejétől 2-ig (0–1 index)
print(string[2:])                  # 2-es indextől a végéig
print(string[1:4])                 # 1–4 index között (1,2,3)
print(string[::2])                 # minden 2. karakter
print(string[::-1])                # string megfordítva
print(string[5:1:-1])              # rész visszafelé (5→2 index)
print(string[-3:])                 # utolsó 3 karakter
print(string[:-2])                 # string utolsó 2 karakter nélkül
print(string[-4:-1])               # negatív indexekkel 4-től 1-ig
print(string[::3])                 # minden 3. karakter
print(string[::-2])                # visszafelé minden 2. karakter

print(string.lower())              # minden karakter kisbetűs
print(string.upper())              # minden karakter nagybetűs
print(string.capitalize())         # első betű nagy, többi kicsi
print(string.title())              # minden szó első betűje nagy
print(string.swapcase())           # kis->nagy, nagy->kis

print(string.find("a"))            # megkeresi "a" első előfordulását (vagy -1)
print(string.rfind("o"))           # utolsó előfordulás (itt 'o'-t nézünk)
print(string.index("o"))           # mint find, de hiba, ha nem találja
print(string.startswith("H"))      # igaz, ha ezzel kezdődik
print(string.endswith("x"))        # igaz, ha ezzel végződik

print(string.strip())              # levágja a szóközöket
print(string.lstrip())             # bal oldalról vág
print(string.rstrip())             # jobb oldalról vág

print(string.replace("o", "0"))    # karakterek cseréje
print(string.split(","))           # string → lista szeparátor alapján
print(",".join(example_list))      # lista → string
print(string.partition(","))       # 3 rész: előtte, ',', utána
print(string.center(30))           # középre igazítja
print(string.ljust(30))            # balra igazítja
print(string.rjust(30))            # jobbra igazítja

print(string.isalpha())            # csak betűk?
print(string.isdigit())            # csak számok?
print(string.isalnum())            # betű vagy szám?
print(string.isspace())            # csak whitespace?
print(string.islower())            # minden karakter kisbetűs?
print(string.isupper())            # minden karakter nagybetűs?
print(string.istitle())            # minden szó első betűje nagy?

print("Hello {}!".format("World")) # régebbi .format használat
print(f"{string}")                 # modern f-string

print("42".zfill(5))               # 0-kal feltölt 5 karakter hosszúságig
