from meupacote.new_random import n_random
def test_n_random():
    assert len(n_random(2)) == 2
    assert type(n_random(2)) == list
    assert type(n_random(2)[1])== int
