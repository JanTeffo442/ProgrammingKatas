def longest_str(str_list):
   
    word_length = []
    for n in str_list:
        word_length.append((len(n), n))
    
    word_length.sort()
    return word_length[-1][1]

print(longest_str(["the","quick","brown", "fox", "ate", "my", "chickens", "Madimetja"]))