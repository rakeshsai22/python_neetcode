def reverse_str(word):
    if(word==""):
        return word

    else:
        subWord = word[1:]
        # print(f"subWord:{subWord}")
        subrevWord = reverse_str(subWord)
        solution = subrevWord + word[0]
        return solution

word='Hello' +' '+ 'world'
reverse_str(word)
# print(word[1:])
