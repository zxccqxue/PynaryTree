from PynaryTree import *



class TestInsert():
    
    def setUp(self):
        self.root = TreeNode(5)

    def test_one_insert(self):
        self.root.insert(8)
        #self.assertEqual(str(self.root), '58')

    def test_weird_insert(self):
        self.root.insert(TreeNode(3))
        #self.assertEqual(str(self.root), '35')

    def test_mult_insert(self):
        self.root.insert('acg')
        self.root.insert('b')
        self.root.insert(1)
        self.root.insert(4)
        self.root.insert('adf')
        self.root.insert(6)
        #self.assertEqual(str(self.root), '1345689')

    #def test_insert_return(self):
        #self.assertEqual(True, self.root.insert(3))
        #self.assertEqual(False, self.root.insert(3))
        #self.assertEqual(False, self.root.insert(5))

def print_tree(tr):
        if tr.left != None:
                print_tree(tr.left)

        print tr.data

        if tr.right != None:
                print_tree(tr.right)
        



if __name__ == '__main__':
    tree = TestInsert()
    tree.setUp()
    tree.test_mult_insert()

    print_tree(tree.root)



