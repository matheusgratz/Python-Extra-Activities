def test_n_presence(list_of_numbers, n):

    for value in list_of_numbers:
        
        if n == value:
            return True
    
    return False
    


print(test_n_presence([1, 2, 3, 4, 5 , 6], 3))
print(test_n_presence([1, 2, 3, 4, 5], 0))