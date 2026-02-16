# 🔐 rusty_skillz - CTF Challenge

## Challenge Details

| Attribute | Value |
|-----------|-------|
| **Source** | nullxbytes |
| **Difficulty** | Easy |
| **Language** | Rust / Python |
| **Category** | Cryptography - PRNG |

## Description

This is an easy cryptography CTF challenge that involves reversing a (PRNG) implementation. The challenge demonstrates how weak or predictable PRNGs can be exploited in cryptographic contexts.

## Challenge Objective

Decrypt the flag using the provided encrypted data and understanding the PRNG seed mechanism.

## Key Concepts

- **PRNG Seed Reversal**: The main vulnerability lies in the predictability of the PRNG seed
- **XOR Encryption**: Data is encrypted using XOR operation with PRNG-generated key bytes
- **State Recovery**: Following the code logic allows for seed recovery and decryption

## Files

- `rusty_skillz.py` - Solution script demonstrating the decryption algorithm
- `dusty` - Original challenge binary

## Solution Approach

The decryption process involves:
1. Initialize the PRNG state from a known seed
2. Generate pseudo-random key bytes using the PRNG algorithm
3. XOR each encrypted byte with the corresponding key byte
4. Recover the plaintext flag

### Algorithm Breakdown
