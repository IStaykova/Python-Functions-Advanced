def fill_the_box(height, length, width, *args):
    box_volumes = width * length * height
    boxes = 0

    for item in args:
        if item == "Finish":
            break
        boxes += item

    if box_volumes > boxes:
        return f"There is free space in the box. You could put {box_volumes - boxes} more cubes."
    else:
        return f"No more free space! You have {boxes - box_volumes} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))