def returnBar(
    value: int = 0,
    max: int = 100,
    lbound: str = "[",
    rbound: str = "]",
    track: str = ".",
    bar: str = "█",
    width: int = 20,
    perc: bool = False,
):
    value += 1
    val = ((value / max) * width) + 1
    _perc = round((value/max)*100,2)
    construct = lbound
    for x in range(width):
        if x > int(val):
            construct += track
        else:
            construct += bar
    construct += rbound
    if perc:
        construct += f" {_perc}%"
    return construct