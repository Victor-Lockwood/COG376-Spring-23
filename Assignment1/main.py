# Assignment 1 for COG376, Spring 23
# Much code was used from Professor Lindstedt's walkthrough
# vlock     -   April 6, 2023   - Created

def analyze_text(input_string):
    success = True

    words = input_string.split()

    print("--Stats--")
    print("\tChar count:\t", len(input_string))
    print("\tWord count:\t", len(words))
    print("\tWord len (avg):\t", (len(input_string) / len(words)))

    print("--Transformations--")
    print("\tLower case:\t", input_string.lower())
    print("\tUpper case:\t", input_string.upper())
    print("\tTitle case:\t", input_string.title())
    print("\tReversed:\t", reverse(input_string))
    print("\tWord rev:\t", reverse(words, " "))
    print("\tMock case:\t", mock_case(input_string))

    return success


# Reverses a given input string
def reverse(input_string, separator=""):
    reversed_string = ""

    for i in range(1, len(input_string) + 1):
        reversed_string += input_string[-i] + separator

    return reversed_string


# Alternates the case for a given input string
def mock_case(input_string):
    mocked_string = ""

    for i in range(0, len(input_string)):
        if i % 2 == 0:
            mocked_string += input_string[i].lower()
        else:
            mocked_string += input_string[i].upper()

    return mocked_string


continue_loop = True

# Main loop of the script - to exit just don't type anything and hit enter
while continue_loop:
    user_input = input("Enter a sentence:\n> ")

    if user_input:
        analyze_text(user_input)
    else:
        continue_loop = False
        print("Ending session...")
