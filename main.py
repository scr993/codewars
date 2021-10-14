def unique_in_order(iterable):
    d = []
    a = 0
    for i in iterable:
        if i != a:
            d.append(i)
            a = i
    print(d)

test.assert_equals(unique_in_order('AAAABBBCCDAABBB'), ['A','B','C','D','A','B'])