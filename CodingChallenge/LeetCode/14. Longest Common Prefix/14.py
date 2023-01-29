class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        refer = list(strs[0])
        if (len(strs) == 1):
            return strs[0]

        result = ""
        stop_flag = False
        for string_index in range(0, len(refer)):
            for list_index in range(1, len(strs)):
                if len(strs[list_index]) <= string_index or strs[list_index][string_index] != refer[string_index]:
                    stop_flag = True
                    break
                # print(strs[list_index], string_index, strs[list_index][string_index])
            if stop_flag:
                break
            result += refer[string_index]

        return (result)
