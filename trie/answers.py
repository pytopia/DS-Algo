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
            

# Question 2
class Trie(object):
    def __init__(self):
        
        self.children = {}
        self.end = False

class WordDictionary:
    def __init__(self):
        self.root = Trie()
    
    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        current = self.root
        for ch in word:
            if ch not in current.children.keys():
                current.children[ch] = Trie()
            current = current.children[ch]
        current.end = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def dfs(start_index, root):
            current = root
            for i in range(start_index, len(word)):
                ch = word[i]
                
                if ch == ".":
                    for child in current.children.values():
                        
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if ch not in current.children.keys():
                        return False
                    current = current.children[ch]
            return current.end
        return dfs(0,self.root) #BC we always start by the first letter and the root node
        
        