import unittest
from optional.optional import Optional


class TestOptional(unittest.TestCase):
    def test_get(self):
        opt = Optional.of('hello')
        assert opt.get() == 'hello'

    def test_get_empty(self):
        opt = Optional.empty()
        with self.assertRaises(Exception):
            opt.get()

    def test_of_noneable(self):
        opt = Optional.of_noneable(None)
        assert opt == Optional.empty()

    def test_of_noneable_2(self):
        opt = Optional.of_noneable('foo')
        assert opt == Optional.of('foo')

    def test_of_noneable_3(self):
        opt = Optional.of_noneable(666)
        assert opt == Optional.of(666)

    def test_if_present(self):
        pass


if __name__ == '__main__':
    unittest.main()
