def get_word_count(string):
    return len(string.split())

def get_char_count(text: str) -> set[tuple[str, int]]:
    text = text.lower()
    zaehler = {}
    
    for buchstabe in text:
        if buchstabe.isalpha():  # Nur Buchstaben zählen
            zaehler[buchstabe] = zaehler.get(buchstabe, 0) + 1
            
    return zaehler