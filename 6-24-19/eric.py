# Create a set. Adding to a set is O(1). Checking if i in set s is O(1).
# Given k is a sum of a pair (i, j), add j to the set and check if i is in the set.
# Best case scenario is i and j are next to each other. Worst case scenario is i and j are on opposite ends of the array O(n)
def solution(in_list: list, k: int) -> bool:
    s = set()
    for i in in_list:
      s.add(k-i)
      if i in s:
        return True
    return False
