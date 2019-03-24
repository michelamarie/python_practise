def add_vectors(v1, v2):
    assert len(v1) == len(v2), "Add vectors: vector mismatch"

    for i in range(len(v1)):
        sum = v1[i] + v2[i]
        v3.append(sum)

    return
############################
v1 = [1,2,3,4]
v2 = [10,100,12,13]
v3 = []



print("1, summed vectors: ", v3)
print("2, summed vectors: ", v3)