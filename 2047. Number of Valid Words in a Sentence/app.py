class Solution:
    def countValidWords(self, sentence: str) -> int:
        words = 0
        for word in sentence.strip().split(" "):
            if not word:
                continue
            hyphen_count = 0
            is_word = True
            for i, letter in enumerate(word):
                if letter.isdigit():
                    is_word = False
                    break
                elif letter == "-":
                    hyphen_count += 1
                    if (
                        hyphen_count > 1
                        or i == 0
                        or i == len(word) - 1
                        or not (word[i-1].islower() and word[i+1].islower())
                    ):
                        is_word = False
                        break
                elif letter in ["!", ".", ","] and i != len(word) - 1:
                    is_word = False
                    break

            if is_word:
                words += 1

        return words