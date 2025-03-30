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
    

    