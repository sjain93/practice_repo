def maskify(cc):
    coerced_input = str(cc)
    final = []
    for index, charac in enumerate(coerced_input):
        if index == len(coerced_input)-4 :
            final.append(charac)
        elif index == len(coerced_input)-3 :
            final.append(charac)
        elif index == len(coerced_input)-2 :
            final.append(charac)
        elif index == len(coerced_input)-1:
            final.append(charac)
        else:
            final.append("#")
    output = ''.join(final)
    print(output)

maskify(5148935246)
