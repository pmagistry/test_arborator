import csv

def split_lomaji(lmj):
    #if lmj[-1] != ".":
    #    lmj += "."
    return lmj. \
            replace("-"," "). \
            replace(","," ,"). \
            replace(".", " ."). \
            replace("?"," ?"). \
            replace("!"," !"). \
            replace(";"," ;"). \
            split()
        

def align(hj, lmj):
    ji = list(hj)
    syl = split_lomaji(lmj)
    assert(len(ji) == len(syl))
    return list(zip(ji,syl))


with open("3-2.csv") as f:
    reader = csv.DictReader(f)
    for N, row in enumerate(reader):
        sentence = align(row['Hanji'], row['Lomaji'])
        print(f"""
# sent_id = {N}
# text = {row['Hanji']}
# translit = {row['Lomaji']}
# text_zh = {row['Huagi']}
""".strip())
        for i,(hj,lmj) in enumerate(sentence):
            print("\t".join([str(i+1), hj, hj, "_","_", "_", "_","_", "_", f"Translit={lmj}"]),)
        print()

