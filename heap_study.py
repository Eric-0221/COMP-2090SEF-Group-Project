class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2
    
    def left_child(self, i):
        return i * 2 + 1
    
    def right_child(self, i):
        return i * 2 + 2
    
    def insert(self, val):
        self.heap.append(val)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, i):
        while i > 0 and self.heap[i] < self.heap[self.parent(i)]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        min_val = self.heap[0]
        last = self.heap.pop()
        if len(self.heap) > 0:
            self.heap[0] = last
            self.heapify_down(0)
        return min_val
        
    def heapify_down(self, i):
        smallest = i
        left = self.left_child(i)
        right = self.right_child(i)
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify_down(smallest)

def heap_sort(arr):
    heap = MinHeap()
    for num in arr:
        heap.insert(num)
    sorted_arr = []
    while heap.heap:
        sorted_arr.append(heap.extract_min())
    return sorted_arr

if __name__ == "__main__":
    data = [8, 3, 5, 1, 10, 2]
    print("Orginal data: ", data)
    print("Heap sort result: ", heap_sort(data))