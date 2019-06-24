
test1 = [10, 15, 3, 7]
goal_sum = 17

def sum_in_list(in_list: list, goal_sum: int) -> bool:
	for i in in_list:
		for j in in_list:
			if i + j == goal_sum:
				return True
	return False
