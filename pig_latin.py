vowels = ['a', 'e', 'i', 'o', 'u']

text = input("Kérem írjon be egy tetszőleges mondatot: ")
output = []

def format_to_pig_latin(text):
    punctuation = ""
    
    if text[-1].isalpha() == False:
        punctuation = text[-1]
        text = text.replace(text[-1], "")

    if text[0] in vowels:
        if punctuation == "":
            return text + "yay"
        else:
            return text + "yay" + punctuation
    else:
        group = ""
        for i in text:
            if i not in vowels:
                group += i
            else:
                break
        result = text[len(group):len(text)]
        if punctuation == "":
            result = result + group + "ay"
        else:
            result = result + group + "ay" + punctuation
        return result

for word in text.split():
    output.append(format_to_pig_latin(word))

output = " ".join(output)

print(output)