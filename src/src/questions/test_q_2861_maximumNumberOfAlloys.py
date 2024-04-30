import pytest
from q_2861_maximumNumberOfAlloys import Solution


@pytest.mark.parametrize(
    "n, k, budget, composition, stock, cost, output",
    [
        (3, 2, 15, [[1, 1, 1], [1, 1, 10]], [0, 0, 0], [1, 2, 3], 2),
        (3, 2, 15, [[1, 1, 1], [1, 1, 10]], [0, 0, 100], [1, 2, 3], 5),
        (2, 3, 10, [[2, 1], [1, 2], [1, 1]], [1, 1], [5, 5], 2),
    ],
)
class TestSolution:
    def test_maxNumberOfAlloys(
        self,
        n: int,
        k: int,
        budget: int,
        composition: List[List[int]],
        stock: List[int],
        cost: List[int],
        output: int,
    ):
        sc = Solution()
        assert (
            sc.maxNumberOfAlloys(
                n,
                k,
                budget,
                composition,
                stock,
                cost,
            )
            == output
        )
