def word_count(s):
    # Your code here
    # Python3 code to demonstrate
    # to count words in string
    # using split()

    # initializing string
    test_string = "Hello, my cat. And my cat doesn't say 'hello' back."
    count = 0
    # using split()
    # to count words in string
    res = len(test_string.split())
    for i in range(res):
    

    # printing result
    print("The number of words in string are : " + str(res))


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))