from my_advanced_lib.core.decorators import timer

def test_timer():
    @timer
    def sample():
        return True
    assert sample() == True
