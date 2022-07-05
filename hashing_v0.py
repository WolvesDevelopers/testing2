import hashlib

def hashinitation(word):
    h = hashlib.new('MD5') #implementation of the algorithm.
    h.update(word.encode()) #It gives us the encoded string, and returns the hashed strings.
    return (h.hexdigest())


def run():
    print("===========string-to-hash converter V.1.0.0==============")
    access = True
    prompt = 'Enter a word to convert.'
    prompt += 'Or type "exit" to close the app. : '
    while access:
        word = input(prompt)
        if word == "exit":
            print("closing program.")
            access = False
        else:
            print(f"Your word hashed is : {hashinitation(word)}")



    
if __name__ == '__main__':
    run()