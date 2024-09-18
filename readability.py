from cs50 import get_string


def main():
    text = get_string("Text: ")
    # words starts at 1 because last word wont be counted otherwise
    letters = 0
    words = 1
    sentences = 0

    for i in range(len(text)):
        if text[i].isalpha():
            letters += 1
        elif text[i].isspace():
            words += 1
        elif text[i] in [".", "?", "!"]:
            sentences += 1

    l = (letters / words) * 100
    s = (sentences / words) * 100
    # Coleman-Liau index
    index = 0.0588 * l - 0.296 * s - 15.8
    index = round(index)

    if index > 16:
        print("Grade 16+")
    elif index < 1:
        print("Before Grade 1")
    else:
        print(f"Grade {index}")


main()
