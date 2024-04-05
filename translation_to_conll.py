from pathlib import Path


text = Path("to_be_translated.txt").read_text()

for line in text.splitlines():
    line = line.strip()
    if line.startswith("#"):
        print(line.replace("text", "text_zh"))
    else:
        print(f"# text = {line}")
        for i,syl in enumerate(line.split()):
            print("\t".join([str(i+1), syl, syl, "_","_", "_", "_","_", "_", "_"]),)
        print()

