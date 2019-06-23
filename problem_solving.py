# There are N problems numbered 1..N which you need to complete. You've arranged the problems in increasing difficulty
# order, and the ith problem has estimated difficulty level i. You have also assigned a rating vi to each problem.
# Problems with similar vi values are similar in nature. On each day, you will choose a subset of the problems and solve them.
# You've decided that each subsequent problem solved on the day should be tougher than the previous problem you solved
# on that day. Also, to make it less boring, consecutive problems you solve should differ in their vi rating by at
# least K. What is the least number of days in which you can solve all problems?
#
# Input Format
#
# The first line contains the number of test cases T. T test cases follow. Each case contains an integer N and K on the
#  first line, followed by integers v1,...,vn on the second line.
#
# Constraints
#
# 1 <= T <= 100
# 1 <= N <= 300
# 1 <= vi <= 1000
# 1 <= K <= 1000
#
# Output Format
#
# Output T lines, one for each test case, containing the minimum number of days in which all problems can be solved.
#
# Sample Input
#
# 2
# 3 2
# 5 4 7
# 5 1
# 5 3 4 5 6
# Sample Output
#
# 2
# 1
# Explanation
#
# For the first example, you can solve the problems with rating 5 and 7 on the first day and the problem with rating 4
# on the next day. Note that the problems with rating 5 and 4 cannot be completed consecutively because the ratings
# should differ by at least K (which is 2). Also, the problems cannot be completed in order 5,7,4 in one day because
# the problems solved on a day should be in increasing difficulty level.
#
# For the second example, all problems can be solved on the same day.


count = 0


def problem_solving(remaining_tasks, count, k):
    print(remaining_tasks)
    if len(remaining_tasks) == 0:
        return count
    elif len(remaining_tasks) == 1:
        count += 1
        return count
    else:
        prev = remaining_tasks[0]
        remaining_tasks[0] = None

        for index, task in enumerate(remaining_tasks[1:]):
            if abs(task - prev) >= k:
                prev = task
                remaining_tasks[index+1] = None

        count += 1
        new_array = list(filter(lambda curr: curr is not None, remaining_tasks))
        return problem_solving(new_array, count, k)


stringg = "47 387 431 691 217 983 847 186 493 215 852 815 953 341 242 931 754 865 191 255 631 187 673 763 288 73 698 " \
          "326 222 390 661 621 777 443 311 993 425 510 530 270 76"
string_arr = stringg.split(' ')


print(problem_solving(list(map(int, string_arr)), count, 335))
