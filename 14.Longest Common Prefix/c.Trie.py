class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        trie = Trie()
        for s in strs:
          trie.insert(s)
        
        return trie.longestCommonPrefix()

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class Trie:
    def __init__(self):
      self.root = TrieNode()
  
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEndOfWord = True
    
    def longestCommonPrefix(self):
        prefix = ""
        node = self.root
        while node and not node.isEndOfWord and len(node.children) == 1:
            char, next_node = next(iter(node.children.items()))
            # node.children 是一个字典，其中键是字符，值是对应的 TrieNode 实例。
            # node.children.items() 返回一个字典项的视图，其中每个元素是一个键值对（即 (char, TrieNode)）。
            # iter(node.children.items()) 返回一个迭代器，该迭代器可以用来遍历所有的键值对。
            # next(iter(node.children.items())) 从迭代器中获取下一个元素，即第一个（在这种情况下也是唯一的）键值对。因为我们是在检查一个只有一个子节点的节点，所以可以安全地使用 next() 来获取该子节点。
            prefix += char
            node = next_node
        return prefix


if __name__ == "__main__":
    trimmed_str = input().strip()[1:-1]
    words_list = [word.strip('"') for word in trimmed_str.split(',')]
    
    so = Solution()
    res = so.longestCommonPrefix(words_list)

    print(res)