# =====================add_price====================================
import sys
#
#
# input_prices=list(map(lambda y: f"{float(y):100.2f}", filter(
#     lambda x: x.replace(".", "").isdigit(), sys.argv[1:])))
#
# with open(PRICE_FILE, "a", encoding="utf-8") as price_list:
#     print(*input_prices, sep="\n", file=price_list)
# ===============================edit_price==============================

pos = sys.argv[1]
new_price = sys.argv[2]


if not (pos.isdigit() and new_price.replace(".", "").isdigit()):
    sys.exit(1)

pos = int(pos)
new_price = float(new_price)

with open(file_prise, "r+", encoding="utf-8") as price_list:
    skip_chars = 0

    for _ in range(pos - 1):
        skip_chars += len(next(price_list))

        try:
            skip_chars += len(next(price_list))
        except StopIteration:
            print("out of index")
            sys.exit(1)

    price_list.seek(skip_chars)
    price_list.write(f"{new_price:.2f}")
    price_list.writelines(f"{new_price:100.2f}")

# ==-===============show_price===============================
PRICE_FILE = "./bakery.csv"

def file_reader(start=-1, end=-1):

    with open(PRICE_FILE, "r", encoding="utf-8") as price_list:

        # skip
        if start > 0:
            for _ in range(start - 1):
                price_list.readline()

        # stop
        if end > 0:
            for _ in range(abs(end - start) + 1):
                yield price_list.readline().replace("\n", "")
        else:
            for line in price_list:
                yield line.replace("\n", "")

if __name__ == "__main__":
    import sys

    start_pos = -1
    end_pos = -1

    if len(sys.argv) >= 2 and sys.argv[1].isdigit():
        start_pos = int(sys.argv[1])

    if len(sys.argv) == 3 and sys.argv[2].isdigit():
        end_pos = int(sys.argv[2])

    for l in file_reader(start_pos, end_pos):
        print(f"{float(l):.2f}")