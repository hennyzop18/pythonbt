def append_middle(s1,s2) :
    print("Original Strings are", s1, s2)
    # middle index number of  s1
    mi = int(len(s1)/2)
    
    # get character from 0 to the middle index number from s1
    x = s1[:mi:]
    # Concatenate s2 to it
    x += s2
    # Append remaining character from s1
    x += s1[mi:]
    print ("After appending new string in middle:",  x)
    
append_middle("abc", "ccc")
    
