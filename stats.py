def sort_on(dict):
    return dict["num"]

def get_word_count(string):
    return len(string.split())

def get_char_count(text: str) -> set[tuple[str, int]]:
    text = text.lower()
    zaehler = {}
    
    for buchstabe in text:
        if buchstabe.isalpha():  # Nur Buchstaben zählen
            zaehler[buchstabe] = zaehler.get(buchstabe, 0) + 1
            
    return zaehler

def get_sorted_char_list(zaehler)->list[tuple[str, str],tuple[str,int]]:  
    sorted=[]  
    for char in zaehler:
        #char_tupel= ("char",char)
        #char_count= ("num",zaehler[char])
        #instert={char_tupel,char_count}
        instert={"char":char,"num":zaehler[char]}
        sorted.append(instert)
    sorted.sort(reverse=True, key=sort_on)
    return sorted