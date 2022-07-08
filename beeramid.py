def beeramid(bonus, price):
    prev_beer_cnt = 0
    if bonus < price: return 0
    lvl = 0
    while (lvl + lvl + 1 + prev_beer_cnt)*price <= bonus :
        lvl += 1
        prev_beer_cnt = lvl + lvl-1 + prev_beer_cnt
        bonus -= prev_beer_cnt*price

    return lvl

def test_beeramid():
    assert beeramid(9, 2) == 1
    assert beeramid(21, 1.5) == 3
    assert beeramid(-1, 4) == 0