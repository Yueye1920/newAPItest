


def test_sum(setup_data):
    print(setup_data)
    assert sum(setup_data) ==15

def test_traversal(setup_data):
    print(setup_data)
    for i in setup_data:
        assert i in setup_data