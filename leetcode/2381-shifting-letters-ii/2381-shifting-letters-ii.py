class Solution:
    def shiftingLetters(self, s: str, shifts):
        n = len(s)
        diff = [0] * (n + 1)

        for start, end, direction in shifts:
            if direction == 1:
                val = 1
            else:
                val = -1

            diff[start] += val
            if end + 1 < n:
                diff[end + 1] -= val

        for i in range(1, n):
            diff[i] += diff[i - 1]

        result = []

        for i in range(n):
            shift = diff[i]
            new_char = (ord(s[i]) - ord('a') + shift) % 26
            result.append(chr(new_char + ord('a')))

        return "".join(result)