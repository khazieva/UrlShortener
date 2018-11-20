import os
from termcolor import colored
import storage


FAILED = colored('failed', 'red')
PASSED = colored('passed', 'green')


def test_init_and_remove(name, base_path):
    storage.init_db(base_path)
    if os.path.exists(base_path):
        result_one = PASSED
    else:
        result_one = FAILED
    storage.remove_db(base_path)
    if os.path.exists(base_path):
        result_two = FAILED
    else:
        result_two = PASSED
    print("Test {}: init {}; remove {}.".format(name, result_one, result_two))


def run_tests_init_and_remove():
    test_init_and_remove("1", './test_db.sqlite')


def run_tests():
    run_tests_init_and_remove()


if __name__ == "__main__":
    run_tests()
