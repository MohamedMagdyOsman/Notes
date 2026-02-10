#! /bin/python3
import socket
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed


# Read arguments after file name
def get_args():
    parser = argparse.ArgumentParser(description="A banner grabbing tool made with python3.")

    parser.add_argument('ip', help="The IP(s) to scan.")
    parser.add_argument('-p', '--ports', required=True, help="The port(s) to scan.")
    parser.add_argument('-t', '--threads', type=int, default=50, help="The number of threads.")
    parser.add_argument( "-T", "--timeout", type=float, default=1, help="Socket timeout in seconds")
    parser.add_argument('-v', '--verbose', action='store_true', help="Show info about what's happening right now.")

    args = parser.parse_args()
    return args


# Scan a port with TCP connection & banner grabbing (info about the service)
def scan_port(ip, port, verbose, timeout):
    # start TCP connection
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)

    # try..execpt | if the conect() function failed
    try:
        if verbose:
            print(f"> Scanning {ip}:{port}")

        s.connect((ip, int(port)))

        try:
            # HTTP  banner grabbing
            if int(port) in [80, 8080, 8000]:
                http_request = (
                    f"GET / HTTP/1.1\r\n"
                    f"Host: {ip}\r\n"
                    f"User-Agent: PentestScanner\r\n"
                    f"Connection: close\r\n\r\n"
                )
                s.sendall(http_request.encode())
                response = s.recv(1024).decode(errors="ignore")

                # Verbose...
                if verbose:
                    print(f"> Connected to {ip}:{port}, received banner (HTTP request sent)...")
                
                for line in response.split("\r\n"):
                    if line.lower().startswith("server:"):
                        print(f"[*] {ip}: port {port} is OPEN | {line}")
                        return

                print(f"[*] {ip}: port {port} is OPEN")
            #  normal services banner grabbing
            else:
                banner = s.recv(1024).decode(errors="ignore").strip()
                print(f"[*] {ip}: port {port} is OPEN | {banner}")
        except socket.timeout:
            print(f"[*] {ip}: port {port} is OPEN")
    except socket.error:
        pass
    finally:
        s.close()


# Thread pool
def create_thread(ip, ports, verbose, timeout):
    with ThreadPoolExecutor(max_workers=args.threads) as exucuter:
            futures = []
            
            for port in ports:
                futures.append(
                    exucuter.submit(scan_port, ip, port, verbose, timeout)
                )
            
            for _ in as_completed(futures):
                pass


# Main funtion checks for the IPs and runs the thread pool
def main(args):
    # specific IPs
    if  ',' in args.ports:
        ports = args.ports.split(',')
        create_thread(args.ip, ports, args.verbose, args.timeout)
    # range of IPs
    elif '-' in args.ports:
        all_ports = []
        ports = args.ports.split('-')

        for i in range(int(ports[0]), int(ports[1])+1):
            all_ports.append(i)

        create_thread(args.ip, all_ports, args.verbose, args.timeout)
    # one IP
    else:
        scan_port(args.ip, args.ports, args.verbose, args.timeout)


# Only run the code of this file if it's the main file or when it's called from another file
# Don't run the code immediately after import it in another file
if __name__ == '__main__':
    args = get_args()
    main(args)    