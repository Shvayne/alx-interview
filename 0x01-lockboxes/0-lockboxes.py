#!/usr/bin/python3
"""this script contains a canUnlockAll function"""

def canUnlockAll(boxes):
    """Determines if all boxes can be opened"""
    n = len(boxes)
    unlocked = set([0])
    keys = set(boxes[0])

    while keys:
      new_key = keys.pop()
      if new_key < n and new_key not in unlocked:
        unlocked.add(new_key)
        keys.update(boxes[new_key])

    return len(unlocked) == n
