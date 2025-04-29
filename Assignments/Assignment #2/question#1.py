def query(x: int) -> int:
    return -1 * (x - 7)**2 + 49

def find_peak(N: int) -> int:
    left = 0
    right = N
    
    while left < right:
        mid = (left + right) // 2
        if query(mid) < query(mid + 1):
            left = mid + 1
        else:
            right = mid
    
    return left

if __name__ == "__main__":
    N = 16  
    peak = find_peak(N)
    print(f"The peak is at index: {peak}")
    print(f"Elevation at peak: {query(peak)}")
