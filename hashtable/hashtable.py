# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
# ​
#     def __repr__(self):
#         return f'Node({repr(self.value)})'
# ​
# class LinkedList:
#     def __init__(self):
#         self.head = None
# ​
#     def __str__(self):
#         """Print entire linked list."""
# ​
#         if self.head is None:
#             return "[Empty List]"
# ​
#         cur = self.head
#         s = ""
# ​
#         while cur != None:
#             s += f'({cur.value})'
# ​
#             if cur.next is not None:
#                 s += '-->'
# ​
#             cur = cur.next
# ​
#         return s
# ​
#     def find(self, value):
#         cur = self.head
# ​
#         while cur is not None:
#             if cur.value == value:
#                 return cur
# ​
#             cur = cur.next
# ​
#         return None
# ​
#     def delete(self, value):
#         cur = self.head
# ​
#         # Special case of deleting head
# ​
#         if cur.value == value:
#             self.head = cur.next
#             return cur
# ​
#         # General case of deleting internal node
# ​
#         prev = cur
#         cur = cur.next
# ​
#         while cur is not None:
#             if cur.value == value:  # Found it!
#                 prev.next = cur.next   # Cut it out
#                 return cur  # Return deleted node
#             else:
#                 prev = cur
#                 cur = cur.next
# ​
#         return None  # If we got here, nothing found
# ​
#     def insert_at_head(self, node):
#         node.next = self.head
#         self.head = node
# ​
#     def insert_or_overwrite_value(self, value):
#         node = self.find(value)
# ​
#         if node is None:
#             # Make a new node
#             self.insert_at_head(Node(value))
# ​
#         else:
#             # Overwrite old value
#             node.value = value

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
        self.capacity = [None] * capacity
        self.count = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.capacity)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        load_factor = self.count / self.get_num_slots()
        return load_factor


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """ 
        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash_var = 5381
        byte_array = key.encode()

        for byte in byte_array:
            # the modulus keeps it 32-bit, python ints don't overflow
            # hash_var = (hash_var * 33) + ord(byte)
            # hash_var = ((hash_var * 33) ^ byte) % 0x100000000
            hash_var = ((hash_var << 5) + hash_var ) + byte


        return hash_var


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.get_num_slots()

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        self.count += 1 # update the count because we are inserting a key
        hashed_value = self.hash_index(key) # hash the key being passed in
        new_entry = HashTableEntry(key, value) # new entry being passed in

        # if the hash table is empty
        if self.capacity[hashed_value] is None:
            self.capacity[hashed_value] = new_entry
        # if the hash table is not empty
        else:
            if self.get_load_factor() > 0.7:
                self.resize(len(self.capacity) * 2)
            else:
                cur = self.capacity[hashed_value]
                # check for duplicate at head
                if cur.key == key:
                    self.capacity[hashed_value] = new_entry
                else:
                    # if no duplicate at head, while loop to traverse the hash table
                    while cur is not None:
                        if cur.key == key:
                            self.capacity[hashed_value] = new_entry
                    cur = cur.next
                return None


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        hashed_value = self.hash_index(key)
        cur = self.capacity[hashed_value]
        if cur.key == key:
            hashed_value = cur.next
            self.count -= 1
            return cur
        else:
            prev = cur
            cur = cur.next

            while cur is not None:
                if cur.key == key:
                    prev.next = cur.next
                    self.count -= 1
                    return cur
                else:
                    prev = cur
                    cur = cur.next
            return None

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        hashed_value = self.hash_index(key)
        cur = self.capacity[hashed_value]
        if cur.key == key:
            return cur.value
        else:
            while cur is not None:
                if cur.value == key.value:
                    return cur.value

                cur = cur.next
        return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        old_capacity = self.capacity
        new_capacity = [None] * new_capacity

        for i in old_capacity:
            cur = i
            print(old_capacity)
            while old_capacity is not None:
                self.put(cur.key, cur.value)
                cur = cur.next


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
