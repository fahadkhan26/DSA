def fruitsinbasket(fruits):
    l = 0
    maxlen = 0
    basket = {}

    for r in range(len(fruits)):
        if fruits[r] not in basket:
            basket[fruits[r]] = 1
        else:
            basket[fruits[r]] += 1

        while len(basket) > 2:
            basket[fruits[l]] -= 1
            if basket[fruits[l]] == 0:
                del basket[fruits[l]]
            l += 1
        maxlen = max(maxlen, r - l + 1)

    return basket, maxlen