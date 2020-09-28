count = 0
for log in logs:
    if log == '../':
        if count > 0:
            count -= 1
        else:
            pass
    elif log == './':
        pass
    else:
        count += 1
return count
