# Lab 10: Hash Table with Chaining

## 1. Introduction

A hash table is a data structure that stores key-value pairs. It uses
a hash function to map keys to indices in an array. A collision occurs
when two different keys map to the same index.

This laboratory demonstrates collision resolution using chaining,
where each bucket contains a linked list of entries.

## 2. Objectives

1. Implement a custom hash function.
2. Resolve collisions using linked-list buckets.
3. Observe the relationship between load factor and search efficiency.
4. Compare chaining with linear probing.

## 3. Methodology

The program uses two classes:

- `HashNode`: Stores a key, value, and pointer to the next node.
- `HashTable`: Manages the buckets and implements hashing, insertion,
  searching, and displaying entries.

The hash function calculates the sum of the ASCII values of the
characters in a key and applies modulo table capacity.

    hash(key) = sum(ord(char) for char in key) % capacity

When a collision occurs, the new entry is added to the linked list
in the corresponding bucket. If the key already exists, its value
is updated instead of creating a duplicate entry.

## 4. How to Run

Requirements:
- Python 3
- A terminal or command prompt

Instructions:

1. Download or clone this repository.
2. Open a terminal in the project directory.
3. Execute the following command:

       python lab10_hash_table.py

   Alternatively, use:

       python3 lab10_hash_table.py

4. Observe the displayed buckets and search results.

## 5. Sample Execution and Output

Expected output:

    Initial hash table:
    Bucket 0: [Bob: 30]
    Bucket 1: [Charlie: 35]
    Bucket 2:
    Bucket 3: [Alice: 25]
    Bucket 4:

    Search result for Alice: 25
    Updated value for Alice: 26

    Hash table after inserting Eve and Vee:
    Bucket 0: [Bob: 30]
    Bucket 1: [Charlie: 35]
    Bucket 2:
    Bucket 3: [Alice: 26] -> [Eve: 22] -> [Vee: 28]
    Bucket 4:

The output demonstrates insertion, searching, updating an existing
key, and collision resolution through chaining.

## 6. Report Analysis

### Question 1: Record hash table entries demonstrating a collision event.

The hash table has a capacity of five. The ASCII values of the
characters in both "Eve" and "Vee" add up to 288.

    hash("Eve") = 288 % 5 = 3
    hash("Vee") = 288 % 5 = 3

Both keys map to Bucket 3. Since Alice is also stored in that bucket,
the resulting chain is:

    [Alice: 26] -> [Eve: 22] -> [Vee: 28]

This demonstrates collision resolution using chaining. Each key
retains its own value, and updating Alice does not affect Eve or Vee.

### Question 2: Compare the search efficiency of chaining versus linear probing.

Chaining stores colliding entries in a linked list associated with
each bucket. Linear probing stores entries directly in the array
and checks subsequent positions when a collision occurs.

| Feature | Chaining | Linear Probing |
|---|---|---|
| Collision handling | Linked lists | Next available array position |
| Average search | O(1) under suitable assumptions | O(1) at low load factors |
| Worst-case search | O(n) | O(n) |
| Load factor | Can exceed 1 | Must not exceed 1 |
| Main disadvantage | Long linked lists | Clustering |
| Memory usage | Additional pointers | No linked-list pointers |

Here, n represents the number of stored entries.

Chaining performs well when keys are distributed uniformly and
linked lists remain short. Linear probing can use memory efficiently,
but clusters of occupied positions can increase search time.

The load factor of a hash table is calculated as:

    Load factor = Number of entries / Table capacity

For example, a table containing seven entries with a capacity of
ten has a load factor of 0.7.

A lower load factor generally helps maintain efficient searches.
However, actual performance also depends on the hash function and
the distribution of keys.

Both methods have O(n) worst-case search complexity.

## 7. Conclusion

This laboratory demonstrates how a hash table maps keys to array
indices and handles collisions through linked lists. The experiment
shows that different keys can share a bucket without losing their
individual values.

It also illustrates the importance of load factor in maintaining
search efficiency. Chaining allows multiple entries in one bucket,
while linear probing stores entries directly in the array but may
suffer from clustering.

## 8. Repository Structure

    lab10-hash-table/
    ├── lab10_hash_table.py
    └── README.md