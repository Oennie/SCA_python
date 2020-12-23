# To join the uncommon characters in 2 strings
# Convert string into set
# Put together common characters
# sepearte uncommon characters
# join uncommn characters into a string

def solve(str_a, str_b):
    set_a = set(str_a)
    set_b = set(str_b)
    common_character = list(set_a & set_b)
    result = [ch for ch in str_a if ch not in common_character] + [ch for ch in str_b if ch not in common_character]
    print( ''.join(result) )

solve("adbc", "dfga")
