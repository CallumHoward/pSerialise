"""
You can auto-discover and run all tests with this command:

    py.test

Documentation: https://docs.pytest.org/en/latest/
"""

#TODO add tests for serialiser classes


def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 4
