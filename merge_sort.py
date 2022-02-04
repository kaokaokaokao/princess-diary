arr = [3,7,2,9,8,6,1]

def merge_sort(left,right):
  result = []
  i,j = 0,0
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1
  result += left[i:]
  result += right[j:]
  return result

def split(oreo):
  if len(oreo) <= 1:
    return oreo
  m = len(oreo)//2
  left = split(oreo[:m])
  right = split(oreo[m:])
  return merge_sort(left,right)

print(split(arr))