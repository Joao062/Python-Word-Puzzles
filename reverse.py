word = "python"

def reverse(word):
    reverseWord = ""

    for i in word:
        reverseWord = i + reverseWord

    return reverseWord

print(reverse("python"))
