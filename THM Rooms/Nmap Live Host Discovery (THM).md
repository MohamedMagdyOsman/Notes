# 🔍 Nmap – Host Discovery & Basics

## 🎯 Purpose of Nmap in Pentesting
During a **penetration test or network assessment**, our main objectives are:
1. Identify **which devices are alive**
2. Discover **open ports and running services** on those devices



## 🧭 Nmap Scan Phases
A complete Nmap scan can include the following phases:
1. Target specification
2. Host discovery
3. Port scanning
4. Service / version detection
5. OS detection
6. Script scanning 



## 🚀 Default Nmap Behavior

By default, Nmap performs:

* Host discovery (ping)
* Scans the **top 1000 TCP ports**
* DNS resolution (IP ↔ domain)

## 🎯 nmap basics

### Single Target

```bash
nmap machine_ip
nmap domain.com
```

### IP Range

```bash
nmap 10.11.12.15-20
```

### Scan Targets from File

```bash
nmap -iL list_of_hosts.txt

# Example file:
text
10.10.10.5
scanme.nmap.org
192.168.1.10
```


### List Scan (DNS Lookup Only)

```bash
nmap -sL 10.10.12.13/29
```

* Shows which IPs Nmap *would* scan
* No host discovery
* No port scanning



## 🔐 Privileges vs Scan Methods

| Scenario          | Method Used |
| -- | -- |
| Root + Local      | ARP         |
| Root + Remote     | ICMP + TCP  |
| Non-root + Remote | TCP SYN     |


## 🖥️ Host Discovery Methods

Nmap uses **three main techniques** to detect active hosts.



### 1️⃣ ARP Scan (LAN Only)

* Uses **ARP requests**
* Works only within the **local network**
* ARP is a broadcast message → routers do not forward it
* Most **accurate and fastest** method on LAN

```bash
nmap -sn 192.168.1.0/24
nmap -PR -sn TARGETS
```
> -sn → Host discovery only (no port scanning)

> -PR → Do ARP scan only


### 2️⃣ ICMP Scan

* Sends ICMP echo request (ping)

```bash
nmap -sn -PE TARGET
```

Other ICMP types:

* -PP → ICMP timestamp request
  *Useful when ICMP echo is blocked*
* -PM → ICMP address mask request
  *Practically useless*



### 3️⃣ TCP / UDP Ping Scan

Used when ICMP is blocked by firewalls.

#### 🔹 TCP SYN Ping

```bash
sudo nmap -PS -sn TARGET
sudo nmap -PS80,443 -sn TARGET
```

#### 🔹 TCP ACK Ping

```bash
sudo nmap -PA -sn TARGET
sudo nmap -PA80,443 -sn TARGET
```

#### 🔹 UDP Ping

```bash
nmap -PU -sn TARGET
```

If a closed UDP port replies with an ICMP error → host is **up**



## ⚠️ Important Nmap Options

* -sn → Host discovery only (no port scan)
* -Pn → Skip host discovery, assume host is up
  *(useful when ping is blocked)*
* -n → Disable DNS resolution (faster, stealthier)


## ✅ Summary

* ARP scan is **best for internal networks**
* ICMP is often **blocked**
* TCP/UDP pings help **bypass firewalls**
* -Pn is critical for **hardened environments**
* Disable DNS (-n) to reduce noise and speed scans

Nmap host discovery is flexible and powerful. Choosing the correct discovery method depends on:

* Network location (local vs remote)
* Firewall restrictions
* Privileges (root vs non-root)