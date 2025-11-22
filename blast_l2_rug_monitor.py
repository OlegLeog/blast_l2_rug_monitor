import requests, time

def blast_rug_watcher():
    print("Blast L2 instant rug / honeypot detector")
    seen = set()
    while True:
        r = requests.get("https://api.blastscan.io/api?module=stats&action=tokens&sort=desc")
        for token in r.json().get("result", [])[:30]:
            addr = token["contractAddress"]
            if addr in seen: continue
            seen.add(addr)
            if int(token["totalSupply"]) < 1_000_000_000_000 and token["holderCount"] < 50:
                print(f"POSSIBLE RUG / HONEYPOT DETECTED!\n"
                      f"Token: {token['name']} ({token['symbol']})\n"
                      f"Supply: {int(token['totalSupply']):,}\n"
                      f"Holders: {token['holderCount']}\n"
                      f"Contract: {addr}\n"
                      f"https://blastscan.io/token/{addr}\n"
                      f"→ Very low holders + tiny supply = classic scam setup\n"
                      f"{'☠️'*25}")
        time.sleep(9)

if __name__ == "__main__":
    blast_rug_watcher()
