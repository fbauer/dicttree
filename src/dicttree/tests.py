import unittest
import doctest
from pprint import pprint
from interlude import interact

optionflags = doctest.NORMALIZE_WHITESPACE | \
              doctest.ELLIPSIS | \
              doctest.REPORT_ONLY_FIRST_FAILURE

TESTFILES = [
    'test.rst',
    'test_utils.rst',
    'test_view.rst',
]

TESTMODULES = [
    'dicttree.aspects',
    'dicttree.interfaces',
    'dicttree._node',
    'dicttree.utils',
    'dicttree._view',
]

def test_suite():
    return unittest.TestSuite([
        doctest.DocTestSuite(
            module,
            optionflags=optionflags,
            ) for module in TESTMODULES
        ]+[
        doctest.DocFileSuite(
            file,
            optionflags=optionflags,
            globs={'interact': interact,
                   'pprint': pprint},
            ) for file in TESTFILES
        ])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')  #pragma NO COVERAGE
