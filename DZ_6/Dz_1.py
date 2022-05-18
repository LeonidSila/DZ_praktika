def parse_log(pth_file="./nginx_logs.txt"):
    if pth_file:
        with open(pth_file, "r", encoding="utf-8") as file:
            for line in file:
                for line in file:
                    ip = line.split(" - - ")[0]
                    rsp_and_pth = line.split('"')[0]
                    rsp = rsp_and_pth.split()[0]
                    pth = rsp_and_pth.split()[1]
                    yield (ip, rsp, pth)
def find_spamer(pth_file="./nginx_logs.txt"):
    if not pth_file:
        return None
    parsed = parse_log(pth_file)
    db = {}

    for log in parsed:

        db[log[0]] = db.get(log[0], 0) + 1
    return max(db.items(), key=lambda x: x[1])
if __name__ == "__main__":
    parsed = parse_log()
    print(type(parsed))
    for _ in range(5):
        print(next(parsed))
    spamer = find_spamer()
    if spamer:
        print(f"ip spamer: {spamer[0]}, count: {spamer[1]}")