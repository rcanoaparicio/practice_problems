"""
    Implement an autocomplete system. That is, given a query string s and a set of all possible query strings,
    return all strings in the set that have s as a prefix.

    For example, given the query string "de" and the set of strings [dog, deer, deal], return [deer, deal].

    Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
"""
import string
import time

class Node:
    def __init__(self, value, left=None, right=None, next=None):
        self.value = value
        self.left = left
        self.right = right
        self.next = next

def add_word(root, word):
    if len(word) == 0:
        if root == None:
            root = Node(".")
        else:
            root.left = add_word(root.left, word)
    elif root == None:
        root = Node(word[0])
        root.next = add_word(root.next, word[1:])
    elif root.value != "." and word[0] < root.value:
        root.left = add_word(root.left, word)
    elif root.value != "." and word[0] > root.value:
        root.right = add_word(root.right, word)
    elif root.value == ".":
        root.next = add_word(root.next, word)
    else:
        root.next = add_word(root.next, word[1:])
    return root

def build_tree_from_list(list):
    root = Node(list[0][0])
    for e in list:
        root = add_word(root, e)
    return root

def find_words(word, root, arr, s):
    if root:
        if len(word) == 0:  # All words above are valid
            if root.value == ".":
                arr.append(s)
                find_words(word, root.next, arr, s)
            else:
                find_words(word, root.next, arr, s+root.value)
            find_words(word, root.left, arr, s)
            find_words(word, root.right, arr, s)
        else:
            if root.value == ".":
                find_words(word, root.next, arr, s)
            elif root.value == word[0]:
                s += root.value
                find_words(word[1:], root.next, arr, s)
            elif word[0] < root.value:
                find_words(word, root.left, arr, s)
            else:
                find_words(word, root.right, arr, s)

def autocomplete_v1(s, queries):
    res = []
    start = time.time()
    root = build_tree_from_list(queries)
    print("BUILD", time.time()-start)
    start = time.time()
    find_words(s, root, res, "")
    print("FIND", time.time()-start)
    return res

def autocomplete_v0(s, queries):
    res = []
    for query in queries:
        if len(query) >= len(s):
            diff = False
            i = 0
            while not diff and i < len(s):
                if s[i] != query[i]:
                    diff = True
                i += 1
            if not diff:
                res.append(query)
    return res

asc = string.ascii_lowercase
combs = [val1+val2+val3+val4 for val1 in asc for val2 in asc for val3 in asc for val4 in asc]
#combs = [val1+val2+val3 for val1 in asc for val2 in asc for val3 in asc]
print(len(combs))
print(autocomplete_v0("de", ["dog", "deer", "deal"]))
print(autocomplete_v1("dogs", ["dog", "deer", "deal", "dogs", "dee"]))
start = time.time()
autocomplete_v0("do", combs)
print("V0",time.time()-start)

autocomplete_v1("do", combs)
