from cf import uni2zg, zg2uni, uni2win, win2uni

def convert(input_value, output_value, input=''):
    result = ''
    if input_value == output_value:
        return input
    if input_value == 'Unicode':
        if output_value == 'Zawgyi':
            result = uni2zg.convert(input)
        elif output_value == 'Win_Myanmar':
            result = uni2win.convert(input)

    elif input_value == 'Zawgyi':
        if output_value == 'Unicode':
            result = zg2uni.convert(input)
        elif output_value == 'Win_Myanmar':
            result = uni2win.convert(zg2uni.convert(input))

    elif input_value == 'Win_Myanmar':
        if output_value == 'Zawgyi':
            result = uni2zg.convert(win2uni.convert(input))
        elif output_value == 'Unicode':
            result = win2uni.convert(input)

    return result

