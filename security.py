
import hashlib
import os

# Part 1: Basic Hash Function
#takes a key as input and returns a hash value between 0 and 9
def simple_hash(key):
    #convert key to a string
    key_str = str(key)
    #calculating the sum of ASCII values of each character
    ascii_sum = sum(ord(char) for char in key_str)
    #taking the modulo of the sum with 10 to get hash value
    return ascii_sum % 10

# Part 2: Hash a List of Keys
def hash_keys_and_observe(keys):
    print("Key-Hash Pairs:")
    for key in keys:
        #hashing each key using simple hash function
        hash_val = simple_hash(key)
        #printing key-hash pairs
        print(f"'{key}': {hash_val}")

# Main execution
if __name__ == "__main__": 
    print("PART 1")
    user_input = input("\nEnter a key to see their hash value: ").strip()
    hash_value = simple_hash(user_input)
    print(f"Hash value for '{user_input}': {hash_value}")

    print("\nPART 2")
    keys = ['apple', 'banana', 'orange', 'grape', 'kiwi', 'melon', 'pear', 'peach', 'mango', 'plum']
    hash_keys_and_observe(keys)
    

# Part 3: Hash Table Implementationimport hashlib

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * self.size
    
    def _hash(self, key):
        key_str = str(key)
        ascii_sum = sum(ord(char) for char in key_str)
        return ascii_sum % self.size
    
    def insert(self, key, value):
        index = self._hash(key)
        new_node = Node(key, value)
        
        if self.table[index] is None:
            self.table[index] = new_node
        else:
            current = self.table[index]
            while current.next:
                if current.key == key:  # Update existing key
                    current.value = value
                    return
                current = current.next
            if current.key == key:
                current.value = value
            else:
                current.next = new_node
    
    def search(self, key):
        index = self._hash(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None
    
    def display(self):
        for i, node in enumerate(self.table):
            print(f"Index {i}:", end=" ")
            current = node
            while current:
                print(f"({current.key}: {current.value}) ->", end=" ")
                current = current.next
            print("None")

    def generate_salt(self, length=16):
        return os.urandom(length).hex()
    
    def salted_hash(self, key, salt):
        hash_input = (str(key) + salt).encode('utf-8')
        hash_output = hashlib.sha256(hash_input).hexdigest()
        return hash_output[:8]  # Return the first 8 characters

# Testing the Hash Table
if __name__ == "__main__":
    hash_table = HashTable()
    keys = ['apple', 'banana', 'orange', 'grape', 'kiwi', 'melon', 'pear', 'peach', 'mango', 'plum']
    
    print("Inserting keys with their length as values:")
    for key in keys:
        hash_table.insert(key, len(key))
    
    hash_table.display()
    
    print("\nSearching for keys:")
    for key in keys:
        value = hash_table.search(key)
        print(f"'{key}': {value}")
    
    print("\nGenerating salted hashes:")
    for key in keys:
        salt = hash_table.generate_salt()
        hashed_value = hash_table.salted_hash(key, salt)
        print(f"'{key}' with salt '{salt}' -> {hashed_value}")
