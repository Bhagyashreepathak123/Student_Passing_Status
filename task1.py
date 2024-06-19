def reverse_string(a):
    words = a.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

input_string = "how are you"
reversed_string = reverse_string(input_string)
print("Input String : ", input_string)
print("Reversed String :" ,reversed_string)
