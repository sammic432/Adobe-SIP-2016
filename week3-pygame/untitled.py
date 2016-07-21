def triangle (side_length, fill_color):
    fillcolor(fill_color)
    pendown()
    for i in range (3):
        forward (side_length)
        right (60)
        print ("I just turned right!")

triangle (50, purple)
