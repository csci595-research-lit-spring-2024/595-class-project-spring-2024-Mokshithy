front_matter = {
    "qid": 1584,
    "title": "Min Cost to Connect All Points",
    "titleSlug": "min-cost-to-connect-all-points",
    "difficulty": "Medium",
    "tags": ["Array", "Union Find", "Graph", "Minimum Spanning Tree"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """You are given an array `points` representing integer coordinates of some points on a 2D-plane, where `points[i] = [xi, yi]`.

    The cost of connecting two points `[xi, yi]` and `[xj, yj]` is the **manhattan distance** between them: `|xi - xj| + |yi - yj|`, where `|val|` denotes the absolute value of `val`.

    Return *the minimum cost to make all points connected.* All points are connected if there is **exactly one** simple path between any two points.



    **Example 1:**

    ![](https://assets.leetcode.com/uploads/2020/08/26/d.png)
    ```
    Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    Output: 20
    Explanation:
    ![](https://assets.leetcode.com/uploads/2020/08/26/c.png)
    We can connect the points as shown above to get the minimum cost of 20.
    Notice that there is a unique path between every pair of points.
    ```
    **Example 2:**

    ```
    Input: points = [[3,12],[-2,5],[-4,1]]
    Output: 18
    ```


    **Constraints:**

    * `1 <= points.length <= 1000`
    * `-10^{6} <= xi, yi <= 10^{6}`
    * All pairs `(xi, yi)` are distinct.
    """

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
