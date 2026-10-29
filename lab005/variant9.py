
text = input("Введите строку: ")


words = text.split()

matching_words = []

for word in words:
    cleaned_word = word.strip(".,!?;:").lower()
    
    if not cleaned_word:
        continue
        
    if 'а' not in cleaned_word:
        matching_words.append(cleaned_word)

if matching_words:
    for word in matching_words:
        print(word)
    print(f"Количество: {len(matching_words)}")
else:
    print("Нет совпадений")
    print("Количество: 0")
