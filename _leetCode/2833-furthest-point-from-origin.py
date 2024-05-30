#Furthest Point From Origin
#https://leetcode.com/problems/furthest-point-from-origin/description/

caseMoves_1 = "L_RL__R"
caseMoves_2 = "_R__LL_"
caseMoves_3 = "_______"

if False:
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
    
if False:
    def furthestDistanceFromOrigin(moves):
        res, optional = 0, 0
        
        for c in moves:
            if c == "L":
                res += 1
            elif c == "R":
                res -= 1
            else:
                optional += 1

        return abs(res) + optional

if True:
    def furthestDistanceFromOrigin(moves):
        my_dict = {}
        for c in moves:
            my_dict[c] = my_dict.get(c, 0) + 1
        
        max_ = max(my_dict.get("L",0), my_dict.get("R",0))
        min_ = min(my_dict.get("L",0), my_dict.get("R",0))
        
        return my_dict.get("_", 0) + (max_ - min_)

print(f"{furthestDistanceFromOrigin(caseMoves_1)}")
print(f"{furthestDistanceFromOrigin(caseMoves_2)}")
print(f"{furthestDistanceFromOrigin(caseMoves_3)}")