def spin_words(sentence):
    palabras = sentence.split()
    palabra_al_reves = []
    
    for p in palabras:
        if len(p) >= 5:
            palabra_al_reves.append(p[::-1]) 
        else:
            palabra_al_reves.append(p)

    frase_final_con_comillas = ""
    for i in range(len(palabra_al_reves)):
        frase_final_con_comillas += palabra_al_reves[i]
        if i < len(palabra_al_reves) - 1:
            frase_final_con_comillas += " "

    return frase_final_con_comillas

if __name__ == '__main__':

    assert spin_words("Welcome") == "emocleW"
    assert spin_words("to") == "to"
    assert spin_words("CodeWars") == "sraWedoC"
    assert spin_words("Hey fellow warriors") == "Hey wollef sroirraw"
    assert spin_words("This sentence is a sentence") == "This ecnetnes is a ecnetnes"