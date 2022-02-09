import doctest

import mapinfow_prj.parser as parser


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocFileSuite("reference.txt"))
    tests.addTests(doctest.DocFileSuite("parser.txt"))
    tests.addTests(doctest.DocTestSuite(parser))
    return tests
