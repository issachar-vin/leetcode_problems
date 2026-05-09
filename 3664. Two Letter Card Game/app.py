class Card:
    value: str
    wildcard: bool

    def __init__(self, value, wildcard):
        self.value = value
        self.wildcard = wildcard
        
    @classmethod
    def from_string(cls, value: str, letter: str):
        is_wildcard = (
            value[0] == letter
            and value[1] == letter
        )
        return cls(
            value=value,
            wildcard=is_wildcard
        )

class Solution:
    def check_if_all_the_same(self, cards, letter):
        cards = [card for card in cards if letter in card]
        if cards:
            base = cards[0]
            for card in cards:
                if base != card:
                    return False
        return True

    def score(self, cards: List[str], x: str) -> int:
        if self.check_if_all_the_same(cards, x):
            return 0
        deck = [Card.from_string(card, x) for card in cards]

        wildcard_count = 0
        index_1_count = 0
        index_2_count = 0

        for card in deck:
            if card.wildcard:
                wildcard_count += 1
            else:
                if card.value[0] == x:
                    index_1_count += 1
                if card.value[1] == x:
                    index_2_count += 1

        result = 0

        if not wildcard_count:
            index_1_set = set([card.value for card in deck if card.value[0]==x])
            index_2_set = set([card.value for card in deck if card.value[1]==x])
            index_1_count = len(index_1_set)
            index_2_count = len(index_2_set)

        if index_1_count > index_2_count:
            if index_2_count < wildcard_count:
                result += index_2_count
                wildcard_count -= index_2_count
                if index_1_count < wildcard_count:
                    result += index_1_count
                else:
                    result += wildcard_count
                    result += int((index_1_count - wildcard_count) / 2)
            else:
                result += wildcard_count
                result += int((index_2_count - wildcard_count) / 2)
                result += int(index_1_count / 2)
        else:
            if index_1_count < wildcard_count:
                result += index_1_count
                wildcard_count -= index_1_count
                if index_2_count < wildcard_count:
                    result += index_2_count
                else:
                    result += wildcard_count
                    result += int((index_2_count - wildcard_count) / 2)
            else:
                result += wildcard_count
                result += int((index_1_count - wildcard_count) / 2)
                result += int(index_2_count / 2)

        return result
