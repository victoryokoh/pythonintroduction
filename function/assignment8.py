# group9.py
def inheritance_distribution():
    total_assets = 108000 - 10000
    ratio = [1, 3, 4]
    total_ratio = sum(ratio)
    shares = [(total_assets * r) / total_ratio for r in ratio]
    highest_share = max(shares)
    child_index = shares.index(highest_share) + 1
    print(f"Child {child_index} got the highest share: ${highest_share}")

inheritance_distribution()