import random
#This program generates simple English sentences
def get_determiner(quantity):
    '''
    Return a randomly chosen determiner.
    '''
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]
    return random.choice(words)

def get_noun(quantity):
    '''
    Return a randomly chosen noun.
    '''
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

    return random.choice(words)

def get_verb(quantity, tense):
    '''
    Return a randomly chosen verb.
    '''
    if tense == "past":
        words = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present":
        if quantity == 1:
            words = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
        else:
            words = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    else:
        words = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    return random.choice(words)

def get_preposition():
    '''
    Return a randomly chosen preposition.
    '''
    words = ["about", "above", "across", "after", "along",
      "around", "at", "before", "behind", "below",
      "beyond", "by", "despite", "except", "for",
      "from", "in", "into", "near", "of",
      "off", "on", "onto", "out", "over",
      "past", "to", "under", "with", "without"]
    return random.choice(words)

def get_adjective():
    '''
    Return a randomly chosen adjective.
    '''
    words = ["happy", "sad", "bright", "dark", "quick", "slow", "strong", "weak", "soft", "hard", "warm", "cold", "sharp", "dull", "loud", "quiet", "brave", "shy", "friendly", "mean", "gentle", "rough", "smooth", "bumpy", "deep", "shallow", "tall", "short", "heavy", "light"]
    return random.choice(words)

def get_prepositional_phrase(quantity):
    '''
    Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.
    '''
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    prepositional_phrase = f"{preposition} {determiner} {noun}"
    return prepositional_phrase

def make_sentence(quantity, tense):
    '''
    Build and return a sentence with a determiner, noun, verb, prepositional phrase, and adjective.
    '''
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    preposition = get_prepositional_phrase(quantity)
    adjective = get_adjective()
    sentence = f"{determiner} {noun} {verb} {preposition} {adjective}.".capitalize()

    return sentence

def main():
    #Generate and prints six sentences with different characteristics
    print(make_sentence(1, "past"))
    print(make_sentence(1, "present"))
    print(make_sentence(1, "future"))
    print(make_sentence(2, "past"))
    print(make_sentence(2, "present"))
    print(make_sentence(2, "future"))
if __name__ == "__main__":
    main()