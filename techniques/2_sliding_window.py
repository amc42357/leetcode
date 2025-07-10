def sliding_window(s):
    left = 0
    char_count = {}
    max_length = 0
    
    for right in range(len(s)):
        # Expandir ventana
        char = s[right]
        char_count[char] = char_count.get(char, 0) + 1
        
        # Contraer ventana hasta que sea válida
        while not condition_valid(char_count):
            left_char = s[left]
            char_count[left_char] -= 1
            if char_count[left_char] == 0:
                del char_count[left_char]
            left += 1
        
        # Actualizar resultado
        max_length = max(max_length, right - left + 1)
    
    return max_length

# Ejemplo: Longest Substring Without Repeating Characters (LeetCode 3)
# Input: "abcabcbb" → Output: 3 (abc)