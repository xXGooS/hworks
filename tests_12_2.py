from runner_and_tournament import Runner, Tournament
import unittest

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner("Усэйн", 10)
        self.runner2 = Runner("Андрей", 9)
        self.runner3 = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for key, result in cls.all_results.items():
            print({place: runner.name for place, runner in result.items()})

    def test_1(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        TournamentTest.all_results["Усейн и Ник"] = results
        self.assertTrue(results[max(results.keys())] == "Ник")

    def test_2(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        TournamentTest.all_results["Андрей и Ник"] = results
        self.assertTrue(results[max(results.keys())] == "Ник")

    def test_3(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        TournamentTest.all_results["Усейн, Андрей и Ник"] = results
        self.assertTrue(results[max(results.keys())] == "Ник")

if __name__ == '__main__':
    unittest.main()


