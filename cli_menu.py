menu_items = {
    1 : "Első menüpont",
    2 : "Második menüpont",
    3 : "Harmadik menüpont",
    4 : "Negyedik menüpont",
    5 : "Kilépés"
}

while True:
    for k, v in menu_items.items():
        print(f"{k}. {v}")
    key = input("Kérem válasszon egy menüpontot: ")
    if key.isdigit():
        key = int(key)
        if key in menu_items:
            print(f"Az ön válassztása a {menu_items[key]}")
            if key == 5:
                print("Kilépett a menüből!")
                break
        else:
            print("Nincs ilyen menüpont! Kérem válasszon újra!")
    else:
        print("Kérem válasszon egy menüpontot! Csak számot adhat meg!")