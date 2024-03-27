#Flipping An Image
#https://leetcode.com/problems/flipping-an-image/description/

caseImage_1 = [[1,1,0],[1,0,1],[0,0,0]]
caseImage_2 = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]

if False:
    def flipAndInvertImage(image):
        left, right = 0, len(image[0]) -1 

        for row in image:
            left_t = left
            right_t = right
            while left_t < right_t:
                row[left_t], row[right_t] = row[right_t], row[left_t]
                left_t+=1
                right_t-=1

        for row in image:
            for i in range(len(row)):
                row[i] = 1 if row[i] == 0 else 0

        return image        

if True:
    def flipAndInvertImage(image):
        for row in image:
            #Slice assignment is needed as otherwise row would refer to 
            #a new list object and not modify the row inside image
            row[:] = row[::-1]
        
        f= lambda n: 1 if n == 0 else 0
        for row in image:
            row[:] = map(f, row)

        return image

print(f"{flipAndInvertImage(caseImage_1)}")
print(f"{flipAndInvertImage(caseImage_2)}")