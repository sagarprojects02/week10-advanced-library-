from my_advanced_lib.core.generators import fibonacci

def test_fibonacci():
    result = list(fibonacci(5))
    assert result == [0, 1, 1, 2, 3]
