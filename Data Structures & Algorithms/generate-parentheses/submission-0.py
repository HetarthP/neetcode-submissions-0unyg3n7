class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stk = [("", 0, 0)]  #(string, open_count, closed_count)
        res = []

        while stk:
            s, open_count, closed_count = stk.pop()

            if len(s) == 2 * n:
                res.append(s)
                continue

            if open_count < n:
                stk.append((s + "(", open_count + 1, closed_count))

            if open_count > closed_count:
                stk.append((s + ")", open_count, closed_count + 1))

        return res
