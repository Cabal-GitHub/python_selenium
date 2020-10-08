from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from assertions import Assertionstest
from search_test import SearchTest

assertions_test = TestLoader().loadTestsFromTestCase(Assertionstest)
search_test = TestLoader().loadTestsFromTestCase(SearchTest)

smoke_test = TestSuite([assertions_test, search_test])

kwarg = {
    "output":'smoke-report'
}

runner = HTMLTestRunner(**kwarg)
runner.run(smoke_test)