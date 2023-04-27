def canUnlockAll(boxes):
    # set to keep track of keys we have
    keys = set([0])
    # list of boxes that we can open
    boxes_to_open = [0]

    # loop through the boxes that we can open
    while boxes_to_open:
        box = boxes_to_open.pop()
        # loop through the keys in the current box
        for key in boxes[box]:
            # if we have not seen this key before, add it to our set of keys
            if key not in keys:
                keys.add(key)
                # add the box that can be opened with this key to our list of boxes to open
                boxes_to_open.append(key)

    # check if we have opened all the boxes
    return len(keys) == len(boxes)

