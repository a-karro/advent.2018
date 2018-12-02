def diff_by_one(string1, string2):
    if len(string1) != len(string2):
        return False
    cnt = 0
    for idx in range(len(string1)):
        cnt += 1 if string1[idx] != string2[idx] else 0
        if cnt > 1:
            return False
    return cnt == 1


with open('data/day2_1.txt', 'r') as f:
    box_codes = [box_code.strip() for box_code in f.readlines()]

for idx1 in range(len(box_codes) - 1):
    for idx2 in range(idx1 + 1, len(box_codes)):
        if diff_by_one(box_codes[idx1], box_codes[idx2]):
            print ''.join([i for i, j in zip(box_codes[idx1], box_codes[idx2]) if i == j])
