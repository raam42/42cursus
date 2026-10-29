def cryptic_sorter(strings: list[str]) -> list[str]:
    def compare(str1, str2):
        if len(str1) != len(str2):
            return len(str1) - len(str2)
        
        lower1 = str1.lower()
        lower2 = str2.lower()
        if lower1 != lower2:
            if lower1 < lower2:
                return -1
            return 1
        
        vowels = "aeiouAEIOU"
        vowels1 = sum(1 for char in str1 if char in vowels)
        vowels2 = sum(1 for char in str2 if char in vowels)
        if vowels1 != vowels2:
            return vowels1 - vowels2
        return 0

        result = strings[:]
        for i in range(1, len(result)):
            current = result[i]
            j = i - 1
            while j >= 0 and compare(result[j], current) > 0:
                result[j + 1] = result[j]
                j -= 1
            result[j + 1] = current
        return result