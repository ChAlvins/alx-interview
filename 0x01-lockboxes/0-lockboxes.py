#!/usr/bin/python3
"""
Defines a function that determines if a box containing keys
to unlock n number of boxes
"""


def canUnlockAll(boxes):
    """determines if all the boxes can be opened or not"""

    unlocked = [0]

    for box_id, box in enumerate(boxes):
        if not box:
            continue
        for key in box:
            if key < len(boxes) and key not in unlocked and key != box_id:
                unlocked.append(key)
    if len(unlocked) == len(boxes):
        return True
    return False
