vowels = ['a', 'e', 'i', 'o', 'u']

text = input("Kérem írjon be egy tetszőleges mondatot: ")
output = []

def format_to_pig_latin(text):
    if text[0] in vowels:
        return text + "yay"
    else:
        group = ""
        for i in text:
            if i not in vowels:
                group += i
            else:
                break
        result = text[len(group):len(text)]
        result = result + group + "ay"
        return result

for word in text.split():
    output.append(format_to_pig_latin(word))

output = " ".join(output)

print(output)