#Exceptions
if True:
    posts = [{'Likes':21, 'Comments':2}, {'Likes':321, 'Comments':100, 'Shares':10}, {'Likes':3, 'Comments':4, 'Shares':2}, {'Likes':2, 'Comments':5}, {'Comments':15} ]

    total_likes = 0

    for post in posts:
        try:
            total_likes += post["Likes"]
        except KeyError:
            pass

    print(f"Total Likes: {total_likes}")