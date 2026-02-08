import argparse
import urllib3
from urllib3 import util
import json
import math
import time  # Ajout du module time
from tqdm import tqdm  # Importation de tqdm pour la barre de progression

LIMIT = 200  # Modifier la limite à 405 adresses
SATOSHI = 1e+8

def check_balance(fi, fo):
    print('loading addresses...')
    f1 = open(fi)
    f2 = open(fo, 'w')
    addresses = []
    for l in f1:
        addresses.append(l.strip())
    print('addresses loaded:', len(addresses))
    print('getting balances info...')
    f1.close()
    http = urllib3.PoolManager(timeout=util.Timeout(10))
    total = len(addresses)
    steps = math.ceil(total / LIMIT)  # Utilisation de math.ceil pour arrondir à l'entier supérieur
    remind = total % LIMIT

    # Création de la barre de progression fixe
    with tqdm(total=total, position=0, leave=True, bar_format='{desc}: {percentage:3.0f}%|{bar}| {n_fmt}/{total_fmt}') as pbar:
        for step in range(steps):
            url = 'https://blockchain.info/balance?active='
            start = step * LIMIT
            end = min((step + 1) * LIMIT, total)  # Limiter la boucle pour éviter un dépassement d'index
            for a in range(start, end):
                url += addresses[a] + '|'
            url = url[:-1]
            res = http.request('GET', url, timeout=util.Timeout(10), retries=util.Retry(10))
            data = json.loads(res.data.decode('utf-8'))
            for address in data:
                balance = data[address]['final_balance'] / SATOSHI
                n_tx = data[address]['n_tx']
                b = '{0:.8f} '.format(balance)
                f2.write(address + '\t\t\t' + b + '\t\t\t' + str(n_tx) + '\n')
            pbar.update(end - start)  # Mise à jour de la barre de progression avec le nombre d'adresses traitées

            print("%.2f" % ((step / (steps if steps > 0 else 1)) * 100), '%')

            # Ajout du délai de 25 ms
            time.sleep(0.25)

    f2.close()
    print('complete')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("fi", help="text file containing one address per line")
    parser.add_argument("fo", help="text file to save addresses with balance details")
    args = parser.parse_args()
    fi = args.fi
    fo = args.fo
    check_balance(fi, fo)
