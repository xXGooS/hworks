import logging
import unittest
from rt_with_exceptions import Runner


class RunnerTest(unittest.TestCase):
    logging.basicConfig(level=logging.INFO, filename='runner_tests.log', filemode='w', encoding='utf-8',
                        format="[%(asctime)s] [%(levelname)s]: %(message)s")
    is_frozen = False

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            runner = Runner("test", speed=-10)
            for i in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 100)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as err:
            logging.warning("Неверная скорость для Runner", exc_info=err)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')

    def test_run(self):
        try:
            runner = Runner(False, speed=10)
            for i in range(10):
                runner.run()
            self.assertEqual(runner.distance, 200)
            logging.info('"test_run" выполнен успешно')
        except TypeError as err:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=err)


    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner1 = Runner("test1", speed=10)
        runner2 = Runner("test2", speed=10)
        for i in range(10):
            runner1.walk()
            runner2.run()
        self.assertNotEqual(runner1.distance, runner2.distance)

if __name__ == '__main__':
    unittest.main()