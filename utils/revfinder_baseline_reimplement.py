#########################################################################
# File: stringCompare.py
# Descriptions: String comparison techniques for file path similarity
# Input: The arguments f1, f2 are strings of file path
# Output: Number of common file path components in f1 and f2
# Written By: Patanamon Thongtanunam (patanamon-t@is.naist.jp)
#########################################################################
import json


def path2List(fileString):
    return fileString.split("/")


def LCP(f1, f2):
    f1 = path2List(f1)
    f2 = path2List(f2)
    common_path = 0
    min_length = min(len(f1), len(f2))
    for i in range(min_length):
        if f1[i] == f2[i]:
            common_path += 1
        else:
            break
    return common_path


def LCSuff(f1, f2):
    f1 = path2List(f1)
    f2 = path2List(f2)
    common_path = 0
    r = list(range(min(len(f1), len(f2))))
    r.reverse()
    for i in r:
        if f1[i] == f2[i]:
            common_path += 1
        else:
            break
    return common_path


def LCSubstr(f1, f2):
    f1 = path2List(f1)
    f2 = path2List(f2)
    common_path = 0
    if len(set(f1) & set(f2)) > 0:
        mat = [[0 for x in range(len(f2) + 1)] for x in range(len(f1) + 1)]
        for i in range(len(f1) + 1):
            for j in range(len(f2) + 1):
                if i == 0 or j == 0:
                    mat[i][j] = 0
                elif f1[i - 1] == f2[j - 1]:
                    mat[i][j] = mat[i - 1][j - 1] + 1
                    common_path = max(common_path, mat[i][j])
                else:
                    mat[i][j] = 0
    return common_path


def LCSubseq(f1, f2):
    f1 = path2List(f1)
    f2 = path2List(f2)
    if len(set(f1) & set(f2)) > 0:
        L = [[0 for x in range(len(f2) + 1)] for x in range(len(f1) + 1)]
        for i in range(len(f1) + 1):
            for j in range(len(f2) + 1):
                if i == 0 or j == 0:
                    L[i][j] = 0
                elif f1[i - 1] == f2[j - 1]:
                    L[i][j] = L[i - 1][j - 1] + 1
                else:
                    L[i][j] = max(L[i - 1][j], L[i][j - 1])
        common_path = L[len(f1)][len(f2)]
    else:
        common_path = 0
    return common_path


def evaulte():
    userIds = []
    filepaths = []
    with open('dataset/android.json') as fr:
        lines = fr.readlines()
        for line in lines:
            data = json.loads(line)
            # print(data)
            # _userid = data['userId']
            # if _userid not in userIds:
            #     userIds.append(_userid)

            files = data['files']
            for file in files:
                filepaths.append(file)

    with open('result/revfinder_baseline.txt','a') as fw:
        for f1 in filepaths:
            for f2 in filepaths:
                common_lcp = LCP(f1,f2)
                common_LCSsuff = LCSuff(f1,f2)
                common_LCSubstr = LCSubstr(f1,f2)
                common_LCSubseq = LCSubseq(f1,f2)
                print(f'LCP: {f1}---{f2}---{common_lcp}')
                print(f'LCSsuff: {f1}---{f2}--{common_LCSsuff}')
                print(f'LCSubstr: {f1}---{f2}---{common_LCSubstr}')
                print(f'LCSubseq: {f1}---{f2}---{common_LCSubseq}')
                fw.write(f'LCP: {f1}---{f2}---{common_lcp} \n')
                fw.write(f'LCSsuff: {f1}---{f2}--{common_LCSsuff} \n')
                fw.write(f'LCSubstr: {f1}---{f2}---{common_LCSubstr} \n')
                fw.write(f'LCSubseq: {f1}---{f2}---{common_LCSubseq} \n')



if __name__ == '__main__':
    evaulte()
