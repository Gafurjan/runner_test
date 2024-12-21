import unittest
from unittest import TestCase

from runner import Runner

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        runner_1 = Runner("Gafurjan")
        for i in range(10):
            runner_1.walk()
        self.assertEqual(runner_1.distance, 50)

    def test_run(self):
        runner_1 = Runner("Gafurjan")
        for i in range(10):
            runner_1.run()
        self.assertEqual(runner_1.distance, 100)

    def test_challenge(self):
        run1 = Runner("Halilla")
        run2 = Runner("Habibulla")
        for i in range(10):
            run1.walk()
            run1.run()
            run2.walk()
            run2.run()

        self.assertNotEqual(run1.distance, run1.walk)




