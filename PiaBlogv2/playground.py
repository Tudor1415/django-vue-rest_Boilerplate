def showPosts(posts):
    objects = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    count = 0
    dimensions =[]

    for i in range(0, posts):
        if i % 8 == 0:
            dimensions.append(count)
            count += 1

    if not dimensions:
        dimensions.append(0)

    return dimensions

# showPosts(5)

print(showPosts(10))