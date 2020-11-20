# from itertools import permutations
#
#
# def possible_permutations(lst):
#     for permutation in permutations(lst):
#         yield list(permutation)
#
#
# [print(n) for n in possible_permutations([1, 2, 3])]


perm = [0, 0, 0]
used = 3 * [False]


def pos_perm(seq, idx = 0):
    if idx == len(seq):
        print(perm)
        return

    for i, x in enumerate(seq):
        if not used[i]:
            perm[idx] = x
            used[i] = True
            pos_perm(seq, idx + 1)
            used[i] = False

print(pos_perm([1, 2, 3]))