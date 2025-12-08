import time

def genTime(func):
    def Time():
        start = time.time()
        res = func()
        end = time.time()

        print(f"time -> {end - start:.4f}")
        return res
    return Time

@genTime
def getNumbers():
    return [i for i in range(1, 100001) if i % 2 == 0]

nums = getNumbers()
# print(nums)

