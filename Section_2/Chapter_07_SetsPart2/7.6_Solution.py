# Read input for the three matches
match1 = eval(input())
match2 = eval(input())
match3 = eval(input())

# 1. Find players who participated in all three matches
thee_matches = match1 & match2 & match3
# 2. Find players who participated in exactly two matches
two_matches = (
    ((match1 & match2) - match3) |
    ((match1 & match3) - match2) | 
    ((match2 & match3) - match1)
)
# 3. Find players who participated in only one match
one_match = (
    (match1 - match2 - match3) |
    (match2 - match1 - match3) |
    (match3 - match1 - match2)
)
# 4. Count total unique players
unique_playes = match1 | match2 | match3
# 5. Find players in Match 1 only
match_one_only = match1 - (match2 | match3)
# Print results in the specified format
print("Players in all matches:",sorted(list(thee_matches)))
print("Players in exactly two matches:",sorted(list(two_matches)))
print("Players in only one match:",sorted(list(one_match)))
print("Total unique players:",len(unique_playes))
print("Players in Match 1 only:",sorted(list(match_one_only)))
