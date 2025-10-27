def build_letter_finde(str1, str2):
    freq1 = {}
    freq2 = {}
    
    for char in str1:
        freq1[char] = freq1.get(char, 0) + 1
    
    for char in str2:
        freq2[char] = freq2.get(char, 0) + 1

    freq_to_chars1 = {}
    for char, count in freq1.items():
        if count not in freq_to_chars1:
            freq_to_chars1[count] = []
        freq_to_chars1[count].append(char)
    
    freq_to_chars2 = {}
    for char, count in freq2.items():
        if count not in freq_to_chars2:
            freq_to_chars2[count] = []
        freq_to_chars2[count].append(char)

    for freq in freq_to_chars1:
        if freq not in freq_to_chars2:
            print("Невозможно построить соответствие: разная частота символов")
            return
        
        if len(freq_to_chars1[freq]) != len( freq_to_chars2[freq]):
            print("Невозможно построить соответствие: разное количество символов с одинаковой частотой")
            return

    finde = []

    for freq in sorted(freq_to_chars1.keys()):
        chars1 = sorted(freq_to_chars1[freq])  
        chars2 = sorted(freq_to_chars2[freq])  

        for char1, char2 in zip(chars1, chars2):
            finde.append(f"{char1}={char2}")

    print(" ".join(finde))

str1 = "abcbaa"
str2 = "jkekjj"
build_letter_finde(str1, str2)
