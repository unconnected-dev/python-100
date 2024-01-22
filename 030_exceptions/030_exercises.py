#Exceptions
if False:
    posts = [{'Likes':21, 'Comments':2}, {'Likes':321, 'Comments':100, 'Shares':10}, {'Likes':3, 'Comments':4, 'Shares':2}, {'Likes':2, 'Comments':5}, {'Comments':15} ]

    total_likes = 0

    for post in posts:
        try:
            total_likes += post["Likes"]
        except KeyError:
            pass

    print(f"Total Likes: {total_likes}")


if True:
    fruit_list = ["apple", "berry"]

    def make_pie(index):
        try:
            fruit = fruit_list[index]
        except IndexError:
            print(f"No fruit in that index: {index}")
        else:
            print(fruit + " pie")


    make_pie(4)
        