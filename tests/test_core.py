import unittest

import core


class TestCore(unittest.TestCase):
    def test_00(self):
        state = core.new_game()
        state["next_id"] = 7
        self.assertEqual(core.bug_9(state), 7)

    def test_01(self):
        state = core.new_game()
        rows = core.bug_16(state)
        self.assertTrue(all(row[0] == "a" for row in rows))

    def test_02(self):
        state = core.new_game()
        self.assertEqual(core.bug_23(state), 1)

    def test_03(self):
        state = core.new_game()
        self.assertTrue(core.bug_0(state))
        self.assertFalse(core.bug_0(state))

    def test_04(self):
        state = core.new_game()
        self.assertEqual(core.bug_7(state), 1)

    def test_05(self):
        state = core.new_game()
        self.assertEqual(core.bug_14(state), 0)

    def test_06(self):
        state = core.new_game()
        self.assertFalse(core.bug_21(state))

    def test_07(self):
        state = core.new_game()
        self.assertFalse(core.bug_28(state))

    def test_08(self):
        state = core.new_game()
        state["queue"] = [1]
        self.assertEqual(core.bug_5(state), 1)
        self.assertEqual(len(state["queue"]), 1)

    def test_09(self):
        state = core.new_game()
        core.bug_12(state)
        self.assertEqual(state["src"], 5)


if __name__ == "__main__":
    unittest.main()
