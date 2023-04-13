import string
import time
import random


def generate_initial():
    write_data(
        {
            f: {"rev": 0, "ts": time.time()}
            for let in string.ascii_letters
            for f in [f"{let}.{ext}" for ext in ["svg", "png", "pdf"]]
        }
    )


def load_data(*, target_file="image_list.txt"):
    ret = []
    with open(target_file) as fin:
        for ln in fin:
            fname, rev, ts = ln.strip().split(":")
            ret.append([fname, int(rev), float(ts)])

    return {fname: {"rev": rev, "ts": ts} for fname, rev, ts in ret}


def write_data(data, *, target_file="image_list.txt"):
    with open(target_file, "w") as fout:
        for fname, v in sorted(data.items()):
            fout.write(f"{fname}:{v['rev']}:{v['ts']}\n")


def rev_fname(fname, *, target_file="image_list.txt"):
    data = load_data()
    old_rev = data[fname]["rev"]
    data[fname] = {"rev": old_rev + 1, "ts": time.time()}
    write_data(data)


for k in random.choices(string.ascii_letters, k=5):
    ext = random.choice(["svg", "png", "pdf"])
    rev_fname(f"{k}.{ext}")
