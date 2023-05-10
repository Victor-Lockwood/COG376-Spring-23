import re
import random

# 1: Prompt with random message if there isn't a match
# 2: Have patterns that match on keywords, no capturing
# 3: Have pattern that captures some information
# 4: Have pattern that uses two pieces of captured info

model = {
    r"\bhello\b|\bhi\b|\bwhassup\b|\bhowdy\b|\bhiya\b|\byo\b": [
        "Hi.  I'm a fish.  Glub glub.",
        "Yo.  I'm a fish.  Glub blub."
    ],
    r"\bshark\b|\bsharks\b": [
        "Sharks are cool.  I pay them off with Shark Bucks so they leave me alone.  Blub glub."
    ],
    r"\bmy name is\b": [
        "Cool name.  I won't remember that.  I have the memory of a goldfish.  Blub blub."
    ],
    r"\bi ate some (.*)": [
        "I hope {first} doesn't have fish in it.\nJust kidding - I don't care.  You do you.  Blub glub.  What else do you eat?  Glub blub.",
        "Those {first} sound tasty.  I usually just eat rocks.  What else can you tell me? You are soooooo interesting.  Blub blub.",
        "Wow, that's suuuuuuch a cool food.  Tell me more. Glub glub."
    ],
    r"\bi like to (.*) because i am (.*)": [
        "Being able to {first} seems sooooo cool.  I'm a fish so I can't do that.  I don't know what it's like to be {second} either, on account of being a fish.  "
        "\nYou should soooo tell me more.  Glub glub."
    ],
    r"\bi like to (.*) because i (.*)": [
        "Wow, it sounds sooo fun to {first}.  I don't get to do that because I'm a fish.  I don't know what it's like to {second} either.  "
        "\nYou should toooootally tell me more.  Glub blub."
    ],
    r"\bmy (dad|brother|dog|cat|mom|sister|sibling)\b": [
        "I don't have a {first} on account of being a fish.  Having a {first} must be soooooo cool.  Tell me more.  Blub blub.",
        "That's sooooo cool.  My family got eaten by orcas.  Tell me more about yours, though.  Blub blub."
    ],
    r"\bmy fish\b|\bpet fish\b": [
        "Woah woah woah.  Eating a fish?  Whatever.  Owning a fish?  Too far.  Blub blub."
    ],
    r"\bsorry\b": [
        "Lol I'm a fish I don't actually care.  Blub blub."
    ],
    r"\byour name\b": [
        "My name is Glub.  Blub blub."
    ]
}

default_model = [
    "Neat.  I didn't understand a word of that, but I'm a fish so it's ok.  Glub blub.",
    "That's cool.  Fun fact: I was not involved in the creation of the Warren Report, on account of me being a fish.\n"
    "Blub glub.  Forget I said that, though.  I'll probably forget I said that and say it again.  Tell me more about you.  Blub blub. ",
    "Wow, that's so cool.  Blub blub.  Humans are soooo neat.  Tell me more.  Glub glub.",
    "Your experiences on land are so different from mine.  I loooove hearing about them.  Blub blub."
]


def discuss(u_input):
    response = None
    match = None
    strip_group = ":?.!,;"

    # Keys are regex patterns
    for key in model.keys():
        if re.search(key, u_input.lower()):
            match = re.search(key, u_input.lower())
            response = random.choice(model[key])
            break

    if match:
        if match.groups():
            if len(match.groups()) == 1:
                response = response.format(first=match.group(1).strip(strip_group))
            else:
                response = response.format(first=match.group(1).strip(strip_group), second=match.group(2).strip(strip_group))

        print(response)
    else:
        print(random.choice(default_model))


# Main loop
done = False
print("Hi.  I'm a fish.")

while not done:
    user_input = input("> ")
    if user_input.lower() == "exit":
        print("Blub blub.  Bye.")
        done = True
    else:
        discuss(user_input)
