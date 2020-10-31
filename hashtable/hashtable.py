class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = max(capacity, MIN_CAPACITY)
        self.buckets = [None] * self.capacity
        self.load = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        length = len(self.buckets)
        return length

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here

        size = 0
        # Count how many indexes in our array
        # that is populated with values.
        for item in self.buckets:
            if item is not None:
                size += 1
        # Return bool value based on if the
        # amount of populated items are more
        # than half the length of the list.
        return size / len(self.buckets)

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        # Your code here
        # Constants
        FNV_prime = 1099511628211
        offset_basis = 14695981039346656037

        # FNV-1 Hash Function
        hash = offset_basis + key
        for char in key:
            hash = hash * FNV_prime
            hash = hash ^ ord(char)
        return hash

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for x in key:
            hash = ((hash << 5) + hash) + ord(x)
        return hash & 0xFFFFFFFF

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        node = HashTableEntry(key, value)
        key = self.buckets[index]
        self.load += 1
        if key:
            self.buckets[index] = node
            self.buckets[index].next = key
        else:
            self.buckets[index] = node
        return self.buckets[index]

        # new_node = HashTableEntry(key, value)
        # idx = self.hash_index(key)
        #
        # if self.buckets[idx] is not None:
        #     self.buckets[idx] = new_node
        #     print('warning! collision!')
        # self.buckets[idx] = value
        # self.load += 1
        # return self.buckets[idx]

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here

        self.load -= 1
        self.put(key, None)
        # idx = self.hash_index(key)
        #
        # if self.buckets[idx] is None:
        #     print('Warning! no key!!')
        # else:
        #     self.buckets[idx] = None
        #     self.load -= 1

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here

        idx = self.hash_index(key)
        node = self.buckets[idx]
        while node:
            if node.key == key:
                return node.value
            node = node.next

        # idx = self.hash_index(key)
        # if self.buckets[idx] is None:
        #     raise KeyError()
        # else:
        #     # Loop through all key-value-pairs
        #     # and find if our key exist. If it does
        #     # then return its value.
        #     for kvp in self.buckets[idx]:
        #         if kvp[0] == key:
        #             return kvp[1]
        #
        #     # If no return was done during loop,
        #     # it means key didn't exist.
        #     raise KeyError()

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here

        new_size = 2 * self.capacity
        for i in range(self.capacity * 2):
            new_capacity.append(None)
        for i in range(self.capacity):
            if self.buckets[i] is not None:
                self.put(self.buckets[i][0], self.buckets[i][1], new_capacity, new_size, True)
        self.buckets = new_capacity
        self.capacity = new_size


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
