liist = [1,3,4,6,2,8,5,1,6,5,3,2,4,6,8,9,0]

no_dups = list(set(liist))

print(no_dups)

no_dups.sort()

print(f"Second largest : {no_dups[-2]}")
