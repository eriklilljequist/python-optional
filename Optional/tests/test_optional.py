import unittest
from src.optional import optional


class TestOptional(unittest.TestCase):
    def test_get(self):
        opt = optional.Optional.of('hello')
        assert opt.get() == 'hello'


if __name__ == '__main__':
    unittest.main()
