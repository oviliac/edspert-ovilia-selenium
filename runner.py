import unittest
from unittest.suite import TestSuite
import navbar, hero_banner, section_1, section_2

if __name__ == "__main__":
    # create test suite from classes
    suite = TestSuite()
    # panggil test
    tests = unittest.TestLoader()
    # menambahkan ke test suite
    suite.addTest(tests.loadTestsFromModule(navbar))
    suite.addTest(tests.loadTestsFromModule(hero_banner))
    suite.addTest(tests.loadTestsFromModule(section_1))
    suite.addTest(tests.loadTestsFromModule(section_2))

    # run test suite
    runner = unittest.TextTestRunner(verbosity=3)
    runner.run(suite)

