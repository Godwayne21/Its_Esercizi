def letter_count(text: str) -> dict[str,int]:
    count = 0
    lower_text=text.lower()
    diz = {}
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in lower_text:
        if i in alphabet:
            count += 1

    diz[text] = [count]

    return diz

letter_count ("defsr-S")