from amwds import example


def func(x):
    return x + 2


def test_answer():
    assert func(3) == 5


def test_print_cwd():
    try:
        example.print_cwd()
    except Exception as e:
        raise e
