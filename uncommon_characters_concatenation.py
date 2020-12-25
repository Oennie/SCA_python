# To join the uncommon characters in 2 strings
# Convert string into set
# Put together common characters
# sepearte uncommon characters
# join uncommn characters into a string

def solve(str_a, str_b):
    set_a = set(str_a)
    set_b = set(str_b)
    common_character = list(set_a & set_b)
    un_chr1 = []
    un_chr2 = []
    for chr_ in str_a:
        if chr_ not in common_character:
            un_chr1.append(chr_)
    for chr_ in str_b:
        if chr_ not in common_character:     
            un_chr2.append(chr_)
    result = (un_chr1 + un_chr2)
    
            
# result = [ch for ch in str_a if ch not in common_character] + [ch for ch in str_b if ch not in common_character]
    print( ''.join(result) )

solve("adbc", "dfga")
