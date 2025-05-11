# your code goes here!
class Anagram:
    pass

    def __init__(self,word):
        self.word = word

    def match(self,word_list):
        matches = []
        sorted_given_word = sorted(self.word)

        for candidate in word_list:
            normalized_candidate = candidate.lower()
            if normalized_candidate == sorted_given_word:
                continue
            if sorted(normalized_candidate) == sorted_given_word:
                matches.append(candidate)

        return matches
