import winsound
import time

UKR_TO_MORSE = {
    'а': '.-', 'б': '-...', 'в': '.--', 'г': '--.', 'ґ': '--.', 'д': '-..', 'е': '.', 'є': '..-..',
    'ж': '...-', 'з': '--..', 'и': '..', 'і': '..', 'ї': '..--', 'й': '.---', 'к': '-.-', 'л': '.-..',
    'м': '--', 'н': '-.', 'о': '---', 'п': '.--.', 'р': '.-.', 'с': '...', 'т': '-', 'у': '..-',
    'ф': '..-.', 'х': '....', 'ц': '-.-.', 'ч': '---.', 'ш': '----', 'щ': '--.-', 'ь': '-..-', 'ю': '..--',
    'я': '.-.-', ' ': '/'
}

def translate_to_morse(text):
    morse_code = ' '.join(UKR_TO_MORSE.get(char.lower(), '') for char in text)
    for symbol in morse_code:
        if symbol == '.':
            winsound.Beep(1000, 200)
        elif symbol == '-':
            winsound.Beep(1000, 600)
        elif symbol == ' ':
            time.sleep(0.2)  
        time.sleep(0.2)
    return morse_code

user_input = input("Введіть текст для перекладу: ")
print(translate_to_morse(user_input))
