# You are given two sorted arrays that contain only integers. Your task is to find a way to merge them into a single one, sorted in ascending order. Complete the function mergeArrays(arr1, arr2), where arr1 and arr2 are the original sorted arrays.

# You don't need to worry about validation, since arr1 and arr2 must be arrays with 0 or more Integers. If both arr1 and arr2 are empty, then just return an empty array.



def merge_arrays(arr1, arr2):
    new_arr = sorted(arr1 + arr2)
    result = []
    for x in new_arr:
      if x not in result:
        result.append(x)
    return result



print(merge_arrays([1, 3, 5, 7, 9], [10, 8, 6, 4, 2])) #, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))