

### Basic commands & Host discovery

```bash
# read from a file
nmap -iL targets.txt

# List the IPs that will be scanned
nmap -sL 10.0.0.0/30

# No port scanning + no reverse DNS lookup
nmap -sn -n 10.0.0.0/24

# ARP scan in LANs
nmap -sn -PR 192.168.1.0/24

# assume host is up
nmap -Pn 10.10.11.45
```

### Port scanning

```bash
nmap -sS 10.10.11.45
nmap -sT 10.10.11.45
nmap -sU 10.10.11.45
```

### Enumeration (getting info/versions of scanning open ports)

**nmap scanning mindet/steps**
1. Find open ports
2. Enumerate services
3. Go deeper per service using `nmap NSE`

**Real-life usage** 

```bash
# The most common real command
nmap -sC -sV 10.10.11.45

# After a full port scan (most realistic flow)
nmap -sC -sV -O -p 22,80,443 10.10.11.45

# Bug bounty / labs / CTFs
nmap -sC -sV -T4 -p 80,443 10.10.11.45

# Agressive
nmap -A -p 22,80,443 10.10.11.45
```

### Timing

#### Most common choices
-T3  → default, safe
-T4  → fast and practical (most used)

#### Rare but intentional
-T2  → old / sensitive systems

#### Almost never
-T0, -T1, -T5

#### Real-life examples
```bash
#Full port scan, realistic speed
nmap -p- -T4 10.10.11.45

# Bug bounty / lab
nmap -sC -sV -T4 -p 80,443 10.10.11.45
```

### Save the scan in a file

| Option | File     | Used by    | Reality     |
| ------ | -------- | ---------- | ----------- |
| `-oN`  | `.nmap`  | Humans     |
| `-oG`  | `.gnmap` | CLI tools  |
| `-oX`  | `.xml`   | Frameworks |
| `-oA`  | `All the 3 files`   | All formats |


#### examples

```bash
# command
nmap Target_IP -oA initial_scan
# file(s)
initial_scan.nmap   → human-readable (notes / report)
initial_scan.gnmap  → greppable (quick parsing)
initial_scan.xml    → tools (Metasploit, Dradis, Faraday)


# command
nmap Target_IP -oG initial_scan.gnmap
# file(s)
initial_scan.gnmap  → greppable (quick parsing)


# command
nmap Target_IP -oN initial_scan.nmap
# file(s)
initial_scan.nmap   → human-readable (notes / report)


# command
nmap Target_IP -oX initial_scan.nmap
# file(s)
initial_scan.xml    → tools (Metasploit, Dradis, Faraday)
```

### Summarize

1. First, we check which devices are up using e.x: `nmap -sn -n 192.168.1.0/24`, or use e.x:`nmap -sn -PR 192.168.1.0/24` for an ARP scan on local networks (LANs).

2. Second, we perform port scanning on the target IP with e.x:`nmap -sS -sU -p- -T4 192.168.1.10`.

3. Next, we enumerate services with e.x:`nmap -sV -O -sC -p T:80,445,U:53,161 192.168.1.10`.

4. Finally, we go deeper with Nmap’s NSE. We can use `-oA, -oG, -oN, or -oX` to save the scan output.