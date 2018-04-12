def ord(t):
    def temps(i):
        return t[i]

    clients = range(len(t))

    return sorted(clients, key=temps)
