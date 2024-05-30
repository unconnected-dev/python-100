#Furthest Point From Origin
#https://leetcode.com/problems/furthest-point-from-origin/description/

caseMoves_1 = "L_RL__R"
caseMoves_2 = "_R__LL_"
caseMoves_3 = "_______"

if True:
    def furthestDistanceFromOrigin(moves):
        lefts, rights, optional = 0, 0, 0

        for c in moves:
            
            if c == "L":
                lefts += 1
            elif c == "R":
                rights += 1
            elif c == "_":
                optional += 1
        
        return optional + (max(lefts, rights) - min(lefts, rights))

print(f"{furthestDistanceFromOrigin(caseMoves_1)}")
print(f"{furthestDistanceFromOrigin(caseMoves_2)}")
print(f"{furthestDistanceFromOrigin(caseMoves_3)}")