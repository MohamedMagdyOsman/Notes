#! /bin/python3
import requests
import argparse
import re
from concurrent.futures import ThreadPoolExecutor, as_completed


def get_args():
    parser = argparse.ArgumentParser(description="HTTP Brute Force Tool Made With Python3.")
    parser.add_argument('target', help="The website you want to work on.")
    parser.add_argument('-v', '--verbose', action='store_true', help='Show what\'s running right now.')
    parser.add_argument('--threads', type=int, default=10, help="Number of concurrent requests.")
    return parser.parse_args()


def contains_http(text):
    return bool(re.search(r"https?://", text))


def dir_brute_force(word, target, verbose):
    STATUS_CODES = [200, 301, 302, 401, 403]
    url = f"{target}/{word}"

    try:
        r = requests.get(url, timeout=3)
        if verbose:
            print(f"> Now, brute forcing /{word} on {target}")
        if r.status_code in STATUS_CODES:
            preview = r.text[:200].strip()
            return [f'/{word}', r.status_code, r.headers.get('Content-Length'), preview]
    except requests.exceptions.RequestException:
        pass

    return None


def main(args):
    TARGET = args.target if contains_http(args.target) else f"https://{args.target}"
    WORDLIST = ['admin', 'login', 'test', 'backup']
    results = {
        "paths": [],
        "codes": [],
        "c_len": [],
        "preview": []
    }

    print(f"[*] Starting brute force on {TARGET}\r\n")

    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        futures = []

        for word in WORDLIST:
            futures.append(
                executor.submit(
                    dir_brute_force,
                    word,
                    TARGET,
                    args.verbose
                )
            )

        for future in as_completed(futures):
            output = future.result()

            if output:
                results['paths'].append(output[0])
                results['codes'].append(output[1])
                results['c_len'].append(output[2])
                results['preview'].append(output[3])

    
    print("\r\n--- RESULTS ---\r\n")
    for i in range(len(results['paths'])):
        print(f"[+] {results['codes'][i]} | {results['paths'][i]} | {results['c_len'][i]} bytes")
        print(f"    ↳ Preview: {results['preview'][i]}\r\n")


if __name__ == '__main__':
    args = get_args()
    main(args)