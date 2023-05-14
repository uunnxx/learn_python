import timeit


# print(sum([i * i for i in range(1_000_000)]))
# # print(sum(i * i for i in range(1_000_000)))
# print(sum((i * i for i in range(1_000_000))))
# print(sum(map(lambda i: i * i, range(1_000_000))))


def sum_gen_list():
    return sum([i * i for i in range(1_000_000)])


def sum_gen_gen():
    # print(sum(i * i for i in range(1_000_000)))
    return sum((i * i for i in range(1_000_000)))


def sum_gen_map():
    return sum(map(lambda i: i * i, range(1_000_000)))


print(timeit.timeit(sum_gen_list, number=100))
print(timeit.timeit(sum_gen_gen, number=100))
print(timeit.timeit(sum_gen_map, number=100))
