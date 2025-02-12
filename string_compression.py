'''7. String Compression
Problem: Given a string s, compress it by replacing consecutive characters with their count.

Code:'''
def compress_string(s: str) -> str:
    if not s:
        return ""
    
    compressed = ""
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed += s[i - 1] + (str(count) if count > 1 else "")
            count = 1
    
    compressed += s[-1] + (str(count) if count > 1 else "")
    return compressed

# Example
print(compress_string("aabcccccaaa"))  # Output: "a2bc5a3"
print(compress_string("abc"))  # Output: "abc"