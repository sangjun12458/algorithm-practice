# 7662. 이중 우선순위 큐
import sys
input = sys.stdin.readline

class DPQ:
    l = []
    end = -1
    
    def insert(self, value):
        self.end += 1
        if self.end >= len(self.l):
            self.l.append(value)
        else:
            self.l[self.end] = value

        child = self.end
        parent = (child - 1) // 2
        while parent >= 0:
            if self.l[child] < self.l[parent]:
                self.l[child], self.l[parent] = self.l[parent], self.l[child]
            child = parent
            parent = (child - 1) // 2

    def delete_min(self):
        if self.end < 0:
            return False, 0
        
        min_value = self.l[0]

        self.l[0] = self.l[self.end]
        self.end -= 1

        parent = 0
        left = parent * 2 + 1
        right = parent * 2 + 2

        while left <= self.end:
            if right <= self.end and self.l[right] <= self.l[left]:
                self.l[left], self.l[right] = self.l[right], self.l[left]
            if self.l[left] < self.l[parent]:
                self.l[parent], self.l[left] = self.l[left], self.l[parent]
            parent = left
            left = parent * 2 + 1
            right = parent * 2 + 2
    
        return True, min_value

    def delete_max(self):
        if self.end < 0:
            return False, 0
        
        max_idx = self.end
        max_value = self.l[self.end]

        for i in range(self.end // 2, self.end):
            if max_value < self.l[i]:
                max_idx = i
                max_value = self.l[i]

        self.l[max_idx] = self.l[self.end]
        self.end -= 1

        child = max_idx
        parent = (child - 1) // 2
        while parent >= 0:
            if self.l[child] < self.l[parent]:
                self.l[child], self.l[parent] = self.l[parent], self.l[child]
            child = parent
            parent = (child - 1) // 2

        return True, max_value

t = int(input())
for _ in range(t):

    dpq = DPQ()

    k = int(input())
    for _ in range(k):
        c, n = input().split()
        n = int(n)

        if c == 'I':
            dpq.insert(n)

        elif c == 'D':
            if n == -1:
                _, _ = dpq.delete_min()
            elif n == 1:
                _, _ = dpq.delete_max()

    is_max, max_v = dpq.delete_max()
    is_min, min_v = dpq.delete_min()

    if is_max:
        if is_min:
            print(max_v, min_v)
        else:
            print(max_v, max_v)
    else:
        print('EMPTY')