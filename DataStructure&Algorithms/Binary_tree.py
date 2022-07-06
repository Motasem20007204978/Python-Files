
class Node:
    def __init__(self, data):
        self.data = data
        self.left:'Node' = None
        self.right:'Node' = None
    

class BinaryTree:
    def __init__(self):
        self.__root:Node = None
        self.__size = 0


    def _selfRoot(self):
        return self.__root
    
    def _insert_node(self, data, root:Node):
        if root is None:
            root = Node(data)
            self.__size += 1

        elif data < self.__root.data:
            if root.left is None:
                root.left = Node(data)
                self.__size += 1
            else:
                self._insert_node(root=root.left, data=data)
        else:
            if root.right is None:
                root.right = Node(data)
                self.__size += 1
            else:
                self._insert_node(root=root.right, data=data)
        
        self.__root = root
    
    def _pre_order(self, root:Node):
        if root is None:
            return
        print(root.data, end=", ")
        self._pre_order(root.left)
        self._pre_order(root.right)
    
    def _in_order(self, root:Node):
        if root is None:
            return
        self._in_order(root.left)
        print(root.data, end=", ")
        self._in_order(root.right)
    
    def _post_order(self, root:Node):
        if root is None:
            return
        self._post_order(root.left)
        self._post_order(root.right)
        print(root.data, end=", ")
    
    def _level_order(self, root:Node):
        if root is None:
            return
        queue = [root]
        while queue:
            tree.root = queue.pop(0)
            if tree.root.left:
                queue.append(tree.root.left)
            if tree.root.right:
                queue.append(tree.root.right)
            print(tree.root.data, end=", ")
    
    def _search(self, root:Node, data):
        if root is None:
            return
        if data == root.data:
            return True
        if data < root.data:
            return self._search(root.left, data)
        else:
            return self._search(root.right, data)

if __name__ == '__main__':
    tree = BinaryTree()
    tree._insert_node(root=tree._selfRoot(), data=80)
    tree._insert_node(root=tree._selfRoot(), data=40)
    tree._insert_node(root=tree._selfRoot(), data=30)
    tree._insert_node(root=tree._selfRoot(), data=50)
    tree._insert_node(root=tree._selfRoot(), data=30)
    tree._insert_node(root=tree._selfRoot(), data=70)
    tree._insert_node(root=tree._selfRoot(), data=10)
    tree._insert_node(root=tree._selfRoot(), data=20)
    tree._insert_node(root=tree._selfRoot(), data=60)

    print('pre-order:')
    tree._pre_order(tree._selfRoot())
    print()
    print('in-order:')
    tree._in_order(tree._selfRoot())
    print()
    print('post-order:')
    tree._post_order(tree._selfRoot())
    print()
    print('level-order:')
    tree._level_order(tree._selfRoot())
    print()
    print('search:')
    print(tree._search(tree._selfRoot(), 10))

    