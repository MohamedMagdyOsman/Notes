# 🔐 Cryptography

## 📌 What is Cryptology?

**Cryptology** = The science of secret communication

It has 2 parts:

1. 🔒 **Cryptography** → Making secrets
2. 🔎 **Cryptanalysis** → Breaking secrets

---

# 🔒 Cryptography

## 🧠 What Does It Do?

It protects data by changing it into unreadable form.

### ✉️ Encryption

```
Clear Text + Key → Ciphertext
```

### 🔓 Decryption

```
Ciphertext + Key → Clear Text
```

---

# 🔑 Types of Ciphers

## 1️⃣ Symmetric Encryption

👉 Uses **ONE shared key**

Both sides use the **same key** to encrypt and decrypt.

### ✅ Features:

* Fast ⚡
* Low CPU usage
* Used to encrypt actual data

### 🧩 Examples:

* DES
* 3DES
* AES (128 / 192 / 256 bit)

### 📌 Important:

The key is called a **Pre-Shared Key (PSK)**.

---

## 2️⃣ Asymmetric Encryption

👉 Uses **TWO keys**

* 🔓 Public Key (shared with everyone)
* 🔐 Private Key (kept secret)

### ✅ Features:

* Slower 🐢
* High CPU usage
* Used mainly for **key exchange**

### 🧩 Examples:

* RSA
* Diffie-Hellman (DH)

---

# 🔄 How They Work Together

💡 In real life, both types are used together.

### Step 1:

Asymmetric encryption securely exchanges a key.

### Step 2:

Symmetric encryption uses that shared key to encrypt the real data.

👉 Because symmetric is faster.

---

# 🏢 PKI (Public Key Infrastructure)

PKI manages digital certificates.

## 🧩 Main Components:

### 1️⃣ CA (Certificate Authority)

Trusted organization that signs certificates.

Examples:

* Google (GTS)
* GoDaddy
* Microsoft

### 2️⃣ Identity Certificate

Digital file that proves identity.

### 3️⃣ Revocation Check

Checks if certificate is still valid.

### 4️⃣ Enrollment

Process of requesting and receiving a certificate.

---

# 🌍 HTTPS Connection (Step-by-Step)

When you visit a secure website:

### 1️⃣ Client ➜ Server

Sends connection request.

### 2️⃣ Server ➜ Client

Sends its **digital certificate (contains public key)**.

### 3️⃣ Browser checks:

* Is certificate signed by trusted CA?
* Is it valid?
* Is it expired?

### 4️⃣ Client creates:

A random **session key** 🔑

### 5️⃣ Client encrypts session key

Using server’s **public key**

### 6️⃣ Server decrypts session key

Using its **private key**

### 7️⃣ Secure communication starts 🔐

Both now use the **same symmetric session key**.
