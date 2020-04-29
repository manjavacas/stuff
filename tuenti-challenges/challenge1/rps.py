with open('submitInput.txt', 'r') as file_in, open('submitOutput.txt', 'w') as file_out:
    next(file_in)
    i = 1
    for line in file_in:
        if 'R' in line and 'S' in line:
            file_out.write('Case #' + str(i) + ': R\n')
        elif 'P' in line and 'R' in line:
            file_out.write('Case #' + str(i) + ': P\n')
        elif 'S' in line and 'P' in line:
            file_out.write('Case #' + str(i) + ': S\n')
        else:
            file_out.write('Case #' + str(i) + ': -\n')
        i += 1