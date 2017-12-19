from collections import OrderedDict

rule_order = ['2', '3', '4', '5', '6', '7', '8', '9', 'A', 'K', 'Q', 'J', 'T']

fragment_1 = ['A', 'J', 'K']
fragment_2 = ['T', '8', '9', 'A']
fragment_3 = ['2', 'T', '4', '5', '6', '7', '8', '9', 'A', 'J', 'K', 'Q', '3']


def card_sorting(fragment_to_sort):
    indexed_fragment = {}
    for i in fragment_to_sort:
        indexed_fragment.update({rule_order.index(i): i})
    indexed_fragment = OrderedDict(sorted(indexed_fragment.items()))
    return list(indexed_fragment.values())


if __name__ == '__main__':
    assert card_sorting(fragment_1) == ['A', 'K', 'J']
    assert card_sorting(fragment_2) == ['8', '9', 'A', 'T']
    assert card_sorting(fragment_3) == ['2', '3', '4', '5', '6', '7', '8', '9', 'A', 'K', 'Q', 'J', 'T']
