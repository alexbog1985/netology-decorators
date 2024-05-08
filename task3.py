import datetime


def logger(old_function):
    ...

    def new_function(*args, **kwargs):
        result = old_function(*args, **kwargs)
        with open('task3.log', 'a') as f:
            f.write(f'{datetime.datetime.now()} {old_function.__name__} {args} {kwargs} {result} \n')
        return result
    return new_function


class FlatIterator:

    @logger
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.list_index = 0
        self.item_index = 0

    @logger
    def __iter__(self):
        return self

    @logger
    def __next__(self):
        item = []
        if self.list_index < len(self.list_of_list):
            list_ = self.list_of_list[self.list_index]
            if self.item_index < len(list_):
                item = list_[self.item_index]
                self.item_index += 1
                return item
            else:
                self.item_index = 0
                self.list_index += 1
                return self.__next__()
        else:
            raise StopIteration


@logger
def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()