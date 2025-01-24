def test_any():
    lists = [True, False, True]

    assert any(lists) == True

def test_any2():
    lists = [False, False, False]

    assert any(lists) == False

def test_all():
    lists = [True, True, False]

    assert all(lists) == False