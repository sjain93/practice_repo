def foo(list):
    output = []
    for index, value in enumerate(list):
        if index%2==0:
            insert = value + 1
            output.append(insert)
        else:
            insert = value - 1
            output.append(insert)
    return output

