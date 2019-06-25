def solution(in_list: list, k: int) -> bool:
    s = set.()
    for i in in_list:
      s.add(k-i)
      if i in s:
        return True
    return False
