# Question 1:
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        current = self.root
        for ch in word:
            if ch not in current.children.keys():
                
                current.children[ch] = TrieNode()

            current = current.children[ch]
        current.end = True
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        current = self.root
        for ch in word:
            if ch not in current.children.keys():
                return False
            current = current.children[ch]
        
        if current.end == True:
            return True
        else: False
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        current = self.root
        for ch in prefix:
            if ch not in current.children.keys():
                return False
            current = current.children[ch]
        return True
            