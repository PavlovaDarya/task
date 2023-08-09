def unique_in_order(iterable):
    if len(iterable) == 1:
        return [iterable[i] for i in range(len(iterable))]
    elif iterable.count(iterable[0]) == len(iterable):
        return iterable[0]
    else:
        iterable = [iterable[i] for i in range(len(iterable)) if iterable[i] != iterable[i - 1]]
    return iterable


print(unique_in_order('AAAAddbba'))