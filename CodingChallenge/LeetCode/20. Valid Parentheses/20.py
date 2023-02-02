class Solution:
    def isValid(self, s: str) -> bool:
        bracket = {')': '(', '}': '{', ']': '['}

        stack = []
        for word in list(s):
            if bracket.get(word) is None:
                stack.append(word)
            else:
                if not stack or stack.pop() != bracket.get(word):  # 스택 최상단에 문자와 현재 괄호가 쌍을 이루는지 확인
                    return False

        if not stack:  # 모든 괄호가 서로 매칭된 경우에만 True 반환
            return True
        return False
