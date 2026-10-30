class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        res = []
        digit_letters = {"2": {"a","b","c"}, "3":{"d", "e", "f"}, "4":{"g", "h", "i"}, "5":{"j", "k", "l"}, "6":{"m", "n", "o"}, "7":{"p", "q", "r", "s"}, "8":{"t", "u", "v"}, "9":{"w", "x", "y", "z"}}
        def dfs(i, curr):
            if i >= len(digits):
                res.append("".join(curr))
                return
            for letter in digit_letters[digits[i]]:
                curr.append(letter)
                dfs(i+1, curr)
                curr.pop()
        dfs(0,[])
        return res
        