import unittest


def triple_step_helper(n, memo):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if not memo.get(n):
        memo[n] = triple_step_helper(n - 1, memo) + triple_step_helper(n - 2, memo) + triple_step_helper(n - 3, memo)
    return memo[n]


def triple_step(n):
    # Create a dict for memoization
    memo = {}
    import time
    start = time.time()
    result = triple_step_helper(n, memo)
    elapsed = time.time() - start
    print(f'Took: {round(elapsed,5)}, Result: {result}')
    return result


class TestTripleStep(unittest.TestCase):

    def test_triple_step(self):
        self.assertEqual(triple_step(100), 44)
