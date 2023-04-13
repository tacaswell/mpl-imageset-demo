import string
import time
import random
import subprocess


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


def load_blame(*, target_file="image_list.txt"):
    blame_result = subprocess.run(
        ["git", "blame", "-l", "--line-porcelain", "image_list.txt"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    ret = {}

    cur_line = {}

    for ln in blame_result.stdout.decode().split("\n"):
        if not ln:
            continue
        print(ln)

        if ln[0] != "\t":
            if len(cur_line) == 0:
                sha, *_ = ln.split(" ")
                cur_line["sha"] = sha
            else:
                key, _, val = ln.partition(" ")
                cur_line[key] = val
        else:
            fname, rev, ts = ln[1:].strip().split(":")
            cur_line["rev"] = int(rev)
            cur_line["ts"] = float(ts)
            ret[fname] = cur_line
            cur_line = {}
    return ret


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
