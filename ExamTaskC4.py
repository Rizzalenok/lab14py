class FitnessClients:
    def __init__(self, month, year, client_code, hours):
        self.month = month
        self.year = year
        self.client_code = client_code
        self.hours = hours

    def is_later(self, other):
        if self.year > other.year:
            return True
        if self.year == other.year and self.month > other.month:
            return True
        return False

N = int(input())
clients = []
for i in range(N):
    line = input().split()
    clients.append(FitnessClients(int(line[0]), int(line[1]), int(line[2]), int(line[3])))

best = clients[0]
for client in clients[1:]:
    if client.hours > best.hours:
        best = client
    elif client.hours == best.hours:
        if client.is_later(best):
            best = client

print(best.hours, best.year, best.month)

# пример входных данных:
# 4
# 5 2005 15 10
# 3 2006 22 15
# 8 2006 18 15
# 12 2007 30 12