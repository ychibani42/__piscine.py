import unittest

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

#   Modify a list like an array in C

ft_list[1] = "World"

#   A tuple is an immutable type,
#   i.e. you can't modify an element of the object,
#   so you pass it through a temporary list which
#   you will then define as a tuple

tupleTemp = list(ft_tuple)
tupleTemp[1] = "France"
#   print(type(tuple_temp))
ft_tuple = tuple(tupleTemp)
#   print(type(ft_tuple))

#   Set items are unordered,
#   unchangeable, and do not allow duplicate values.
#   ex : (1 and True are the same)
#   set_test = {"1", 1, True}
#   there is no "max element in the set" since
#   print(set_test)


ft_set.discard("tutu!")
ft_set = ft_set | {"Paris"}


#   Dict data set is ordered,
#   Mutable and works as key:value pair
#   it allows duplicate too
#   from Python version 3.7, dictionaries are ordered.
#   In Python 3.6 and earlier, dictionaries are unordered.

ft_dict["Hello"] = "42"

#   convention : test_<testing name>


class TestTypeMethods(unittest.TestCase):

    def test_list(self):
        var = ft_list
        self.assertIsInstance(var, list)
        self.assertEqual(var, ['Hello', 'World'])

    def test_tuple(self):
        var = ft_tuple
        self.assertIsInstance(var, tuple)
        self.assertEqual(var, ('Hello', 'France'))

    def test_set(self):
        var = ft_set
        self.assertIsInstance(var, set)
        self.assertEqual(var, {'Hello', 'Paris'})
        self.assertEqual(var, {'Paris', 'Hello'})

    def test_dict(self):
        var = ft_dict
        self.assertIsInstance(var, dict)
        self.assertEqual(var, {'Hello': '42'})

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
