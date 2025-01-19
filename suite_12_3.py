import unittest
from tests_12_3 import RunnerTest, TournamentTest

TestsSuite = unittest.TestSuite()

TestsSuite.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
TestsSuite.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(TestsSuite)