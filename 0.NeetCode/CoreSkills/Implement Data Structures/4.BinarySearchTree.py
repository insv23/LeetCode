'''
设计一个二叉搜索树（Binary Search Tree，简称BST）涉及到创建一个树结构，这个树结构中的每个节点都遵循二叉搜索树的性质：节点的左子树只包含小于当前节点的数，节点的右子树只包含大于当前节点的数，每个子树也都是一个二叉搜索树。
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, val: int) -> None:
        if not self.root:
            self.root = TreeNode(val)
        else:
            self._insert_recursive(self.root, val)
    
    def _insert_recursive(self, node, val):
        if not node:
            return TreeNode(val)
        if val < node.val:
            node.left = self._insert_recursive(node.left, val)
        elif val > node.val:
            node.right = self._insert_recursive(node.right, val)
        return node
    
    def search(self, val: int) -> bool:
        return self._search_recursive(self.root, val)
    
    def _search_recursive(self, node, val):
        if not node:
            return False
        if val == node.val:
            return True
        elif val < node.val:
            return self._search_recursive(node.left, val)
        else:
            return self._search_recursive(node.right, val)
    
    def delete(self, val: int) -> None:
        self.root = self._delete_recursive(self.root, val)
    
    def _delete_recursive(self, node, val):
        if not node:
            return None
        if val < node.val:
            return self._delete_recursive(node.left, val)
        elif val > node.val:
            return self._delete_recursive(node.right, val)
        else:
            if not node.left:
                # 被删除节点的左子树为空, 直接把其右子树补上
                return node.right
            elif not node.right:
                return node.left
            # 只需找出被删除节点的右子树的最小节点补上就行(或左子树最大节点)
            tmp_val = self._find_min(node.right)
            node.val = tmp_val
            # 需要把补充到当前节点的"右子树最小节点"删除
            node.right = self._delete_recursive(node.right, tmp_val)
            return node
 
    def _find_min(self, node):
        while node.left:
            node = node.left
        return node.val