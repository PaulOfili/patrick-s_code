arr = [3,2,1]


def minSwaps(arr):
    n = len(arr)

    # Create two arrays and use
    # as pairs where first array
    # is element and second array
    # is position of first element
    arrpos = [*enumerate(arr)]

    # Sort the array by array element
    # values to get right position of
    # every element as the elements
    # of second array.
    arrpos.sort(key=lambda it: it[1])

    # To keep track of visited elements.
    # Initialize all elements as not
    # visited or false.
    vis = {k: False for k in range(n)}

    # Initialize result
    ans = 0
    for i in range(n):

        # alreadt swapped or
        # alreadt present at
        # correct position
        if vis[i] or arrpos[i][0] == i:
            continue

        # find number of nodes
        # in this cycle and
        # add it to ans
        cycle_size = 0
        j = i
        while not vis[j]:
            # mark node as visited
            vis[j] = True

            # move to next node
            j = arrpos[j][0]
            cycle_size += 1

        # update answer by adding
        # current cycle
        if cycle_size > 0:
            ans += (cycle_size - 1)
            # return answer
    return ans


# C++ WAY SHA

# intt n, arr[maxx], brr[maxx];
# intt pos[maxx], used[maxx];
# intt cycle = 0;
#
# void dfs (intt v) {
#     used[v] = 1;
#     if (used[pos[arr[v]]]) cycle ++;
#     else dfs (pos[arr[v]]);
# }
#
# int main() {
#     cin >> n;
#     for (intt i = 1; i <= n; i++)
#         cin >> arr[i];
#     for (intt i = 1; i <= n; i++)
#         cin >> brr[i], pos[brr[i]] = i;
#     for (intt i = 1; i <= n; i++)
#         if (!used[i])
#             dfs (i);
#     cout << n - cycle << endl;
#     return 0;
# }