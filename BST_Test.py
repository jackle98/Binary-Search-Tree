import unittest
from Binary_Search_Tree import Binary_Search_Tree

class AVL_Tree_Tester(unittest.TestCase):

    def setUp(self):
      self.__BST = Binary_Search_Tree()

    def test_left_left_imbalance_at_root_insertion_in_order(self):
        self.__BST.insert_element(10)
        self.__BST.insert_element(15)
        self.__BST.insert_element(5)
        self.__BST.insert_element(7)
        self.__BST.insert_element(0)
        self.__BST.insert_element(-5)
        self.assertEqual("[ -5, 0, 5, 7, 10, 15 ]", self.__BST.in_order())

    def test_left_left_imbalance_at_root_insertion_post_order(self):
        self.__BST.insert_element(10)
        self.__BST.insert_element(15)
        self.__BST.insert_element(5)
        self.__BST.insert_element(7)
        self.__BST.insert_element(0)
        self.__BST.insert_element(-5)
        self.assertEqual("[ -5, 0, 7, 15, 10, 5 ]", self.__BST.post_order())

    def test_left_left_imbalance_at_root_insertion_pre_order(self):
        self.__BST.insert_element(10)
        self.__BST.insert_element(15)
        self.__BST.insert_element(5)
        self.__BST.insert_element(7)
        self.__BST.insert_element(0)
        self.__BST.insert_element(-5)
        self.assertEqual("[ 5, 0, -5, 10, 7, 15 ]", self.__BST.pre_order())

    def test_right_right_imbalance_at_root_insertion_in_order(self):
        self.__BST.insert_element(10)
        self.__BST.insert_element(15)
        self.__BST.insert_element(5)
        self.__BST.insert_element(13)
        self.__BST.insert_element(20)
        self.__BST.insert_element(17)
        self.assertEqual("[ 5, 10, 13, 15, 17, 20 ]", self.__BST.in_order())

    def test_right_right_imbalance_at_root_insertion_post_order(self):
        self.__BST.insert_element(10)
        self.__BST.insert_element(15)
        self.__BST.insert_element(5)
        self.__BST.insert_element(13)
        self.__BST.insert_element(20)
        self.__BST.insert_element(17)
        self.assertEqual("[ 5, 13, 10, 17, 20, 15 ]", self.__BST.post_order())

    def test_right_right_imbalance_at_root_insertion_pre_order(self):
        self.__BST.insert_element(10)
        self.__BST.insert_element(15)
        self.__BST.insert_element(5)
        self.__BST.insert_element(13)
        self.__BST.insert_element(20)
        self.__BST.insert_element(17)
        self.assertEqual("[ 15, 10, 5, 13, 20, 17 ]", self.__BST.pre_order())

    def test_left_right_imbalance_at_root_insertion_in_order(self):
        self.__BST.insert_element(20)
        self.__BST.insert_element(0)
        self.__BST.insert_element(50)
        self.__BST.insert_element(-5)
        self.__BST.insert_element(5)
        self.__BST.insert_element(3)
        self.assertEqual("[ -5, 0, 3, 5, 20, 50 ]", self.__BST.in_order())

    def test_left_right_imbalance_at_root_insertion_post_order(self):
        self.__BST.insert_element(20)
        self.__BST.insert_element(0)
        self.__BST.insert_element(50)
        self.__BST.insert_element(-5)
        self.__BST.insert_element(5)
        self.__BST.insert_element(3)
        self.assertEqual("[ -5, 3, 0, 50, 20, 5 ]", self.__BST.post_order())

    def test_left_right_imbalance_at_root_insertion_pre_order(self):
        self.__BST.insert_element(20)
        self.__BST.insert_element(0)
        self.__BST.insert_element(50)
        self.__BST.insert_element(-5)
        self.__BST.insert_element(5)
        self.__BST.insert_element(3)
        self.assertEqual("[ 5, 0, -5, 3, 20, 50 ]", self.__BST.pre_order())

    def test_right_left_imbalance_at_root_insertion_in_order(self):
        self.__BST.insert_element(30)
        self.__BST.insert_element(5)
        self.__BST.insert_element(50)
        self.__BST.insert_element(40)
        self.__BST.insert_element(70)
        self.__BST.insert_element(35)
        self.assertEqual("[ 5, 30, 35, 40, 50, 70 ]", self.__BST.in_order())

    def test_right_left_imbalance_at_root_insertion_post_order(self):
        self.__BST.insert_element(30)
        self.__BST.insert_element(5)
        self.__BST.insert_element(50)
        self.__BST.insert_element(40)
        self.__BST.insert_element(70)
        self.__BST.insert_element(35)
        self.assertEqual("[ 5, 35, 30, 70, 50, 40 ]", self.__BST.post_order())

    def test_right_left_imbalance_at_root_insertion_pre_order(self):
        self.__BST.insert_element(30)
        self.__BST.insert_element(5)
        self.__BST.insert_element(50)
        self.__BST.insert_element(40)
        self.__BST.insert_element(70)
        self.__BST.insert_element(35)
        self.assertEqual("[ 40, 30, 5, 35, 50, 70 ]", self.__BST.pre_order())

    def test_left_left_imbalance_at_root_removal_in_order(self):
        self.__BST.insert_element(20)
        self.__BST.insert_element(5)
        self.__BST.insert_element(50)
        self.__BST.insert_element(0)
        self.__BST.insert_element(10)
        self.__BST.insert_element(70)
        self.__BST.insert_element(-5)
        self.__BST.remove_element(70)
        self.assertEqual("[ -5, 0, 5, 10, 20, 50 ]", self.__BST.in_order())

    def test_left_left_imbalance_at_root_removal_post_order(self):
        self.__BST.insert_element(20)
        self.__BST.insert_element(5)
        self.__BST.insert_element(50)
        self.__BST.insert_element(0)
        self.__BST.insert_element(10)
        self.__BST.insert_element(70)
        self.__BST.insert_element(-5)
        self.__BST.remove_element(70)
        self.assertEqual("[ -5, 0, 10, 50, 20, 5 ]", self.__BST.post_order())

    def test_left_left_imbalance_at_root_removal_pre_order(self):
        self.__BST.insert_element(20)
        self.__BST.insert_element(5)
        self.__BST.insert_element(50)
        self.__BST.insert_element(0)
        self.__BST.insert_element(10)
        self.__BST.insert_element(70)
        self.__BST.insert_element(-5)
        self.__BST.remove_element(70)
        self.assertEqual("[ 5, 0, -5, 20, 10, 50 ]", self.__BST.pre_order())

    def test_right_right_imbalance_at_root_removal_in_order(self):
        self.__BST.insert_element(20)
        self.__BST.insert_element(5)
        self.__BST.insert_element(50)
        self.__BST.insert_element(0)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(80)
        self.__BST.remove_element(0)
        self.assertEqual("[ 5, 20, 30, 50, 70, 80 ]", self.__BST.in_order())

    def test_right_right_imbalance_at_root_removal_post_order(self):
        self.__BST.insert_element(20)
        self.__BST.insert_element(5)
        self.__BST.insert_element(50)
        self.__BST.insert_element(0)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(80)
        self.__BST.remove_element(0)
        self.assertEqual("[ 5, 30, 20, 80, 70, 50 ]", self.__BST.post_order())

    def test_right_right_imbalance_at_root_removal_pre_order(self):
        self.__BST.insert_element(20)
        self.__BST.insert_element(5)
        self.__BST.insert_element(50)
        self.__BST.insert_element(0)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(80)
        self.__BST.remove_element(0)
        self.assertEqual("[ 50, 20, 5, 30, 70, 80 ]", self.__BST.pre_order())

    def test_left_right_imbalance_at_root_removal_in_order(self):
        self.__BST.insert_element(20)
        self.__BST.insert_element(5)
        self.__BST.insert_element(50)
        self.__BST.insert_element(0)
        self.__BST.insert_element(10)
        self.__BST.insert_element(70)
        self.__BST.insert_element(7)
        self.__BST.remove_element(70)
        self.assertEqual("[ 0, 5, 7, 10, 20, 50 ]", self.__BST.in_order())

    def test_left_right_imbalance_at_root_removal_post_order(self):
        self.__BST.insert_element(20)
        self.__BST.insert_element(5)
        self.__BST.insert_element(50)
        self.__BST.insert_element(0)
        self.__BST.insert_element(10)
        self.__BST.insert_element(70)
        self.__BST.insert_element(7)
        self.__BST.remove_element(70)
        self.assertEqual("[ 0, 7, 5, 50, 20, 10 ]", self.__BST.post_order())

    def test_left_right_imbalance_at_root_removal_pre_order(self):
        self.__BST.insert_element(20)
        self.__BST.insert_element(5)
        self.__BST.insert_element(50)
        self.__BST.insert_element(0)
        self.__BST.insert_element(10)
        self.__BST.insert_element(70)
        self.__BST.insert_element(7)
        self.__BST.remove_element(70)
        self.assertEqual("[ 10, 5, 0, 7, 20, 50 ]", self.__BST.pre_order())

    def test_right_left_imbalance_at_root_removal_in_order(self):
        self.__BST.insert_element(20)
        self.__BST.insert_element(5)
        self.__BST.insert_element(50)
        self.__BST.insert_element(0)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(25)
        self.__BST.remove_element(0)
        self.assertEqual("[ 5, 20, 25, 30, 50, 70 ]", self.__BST.in_order())

    def test_right_left_imbalance_at_root_removal_post_order(self):
        self.__BST.insert_element(20)
        self.__BST.insert_element(5)
        self.__BST.insert_element(50)
        self.__BST.insert_element(0)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(25)
        self.__BST.remove_element(0)
        self.assertEqual("[ 5, 25, 20, 70, 50, 30 ]", self.__BST.post_order())

    def test_right_left_imbalance_at_root_removal_pre_order(self):
        self.__BST.insert_element(20)
        self.__BST.insert_element(5)
        self.__BST.insert_element(50)
        self.__BST.insert_element(0)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(25)
        self.__BST.remove_element(0)
        self.assertEqual("[ 30, 20, 5, 25, 50, 70 ]", self.__BST.pre_order())

    def test_height_after_left_left_imbalance_insertion(self):
        self.__BST.insert_element(10)
        self.__BST.insert_element(15)
        self.__BST.insert_element(5)
        self.__BST.insert_element(7)
        self.__BST.insert_element(0)
        self.__BST.insert_element(-5)
        self.assertEqual(3, self.__BST.get_height())

    def test_height_after_right_right_imbalance_insertion(self):
        self.__BST.insert_element(10)
        self.__BST.insert_element(15)
        self.__BST.insert_element(5)
        self.__BST.insert_element(13)
        self.__BST.insert_element(20)
        self.__BST.insert_element(17)
        self.assertEqual(3, self.__BST.get_height())

    def test_height_after_left_right_imbalance_insertion(self):
        self.__BST.insert_element(20)
        self.__BST.insert_element(0)
        self.__BST.insert_element(50)
        self.__BST.insert_element(-5)
        self.__BST.insert_element(5)
        self.__BST.insert_element(3)
        self.assertEqual(3, self.__BST.get_height())

    def test_height_after_right_left_imbalance_insertion(self):
        self.__BST.insert_element(30)
        self.__BST.insert_element(5)
        self.__BST.insert_element(50)
        self.__BST.insert_element(40)
        self.__BST.insert_element(70)
        self.__BST.insert_element(35)
        self.assertEqual(3, self.__BST.get_height())

    def test_height_after_left_left_imbalance_removal(self):
        self.__BST.insert_element(20)
        self.__BST.insert_element(5)
        self.__BST.insert_element(50)
        self.__BST.insert_element(0)
        self.__BST.insert_element(10)
        self.__BST.insert_element(70)
        self.__BST.insert_element(-5)
        self.__BST.remove_element(70)
        self.assertEqual(3, self.__BST.get_height())

    def test_height_after_right_right_imbalance_removal(self):
        self.__BST.insert_element(20)
        self.__BST.insert_element(5)
        self.__BST.insert_element(50)
        self.__BST.insert_element(0)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(80)
        self.__BST.remove_element(0)
        self.assertEqual(3, self.__BST.get_height())

    def test_height_after_left_right_imbalance_removal(self):
        self.__BST.insert_element(20)
        self.__BST.insert_element(5)
        self.__BST.insert_element(50)
        self.__BST.insert_element(0)
        self.__BST.insert_element(10)
        self.__BST.insert_element(70)
        self.__BST.insert_element(7)
        self.__BST.remove_element(70)
        self.assertEqual(3, self.__BST.get_height())

    def test_height_after_right_left_imbalance_removal(self):
        self.__BST.insert_element(20)
        self.__BST.insert_element(5)
        self.__BST.insert_element(50)
        self.__BST.insert_element(0)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(25)
        self.__BST.remove_element(0)
        self.assertEqual(3, self.__BST.get_height())

    def test_left_left_imbalance_at_root_insertion_to_list(self):
        self.__BST.insert_element(10)
        self.__BST.insert_element(15)
        self.__BST.insert_element(5)
        self.__BST.insert_element(7)
        self.__BST.insert_element(0)
        self.__BST.insert_element(-5)
        self.assertEqual([-5, 0, 5, 7, 10, 15 ], self.__BST.to_list())

    def test_right_right_imbalance_at_root_insertion_to_list(self):
        self.__BST.insert_element(10)
        self.__BST.insert_element(15)
        self.__BST.insert_element(5)
        self.__BST.insert_element(13)
        self.__BST.insert_element(20)
        self.__BST.insert_element(17)
        self.assertEqual([ 5, 10, 13, 15, 17, 20 ], self.__BST.to_list())

    def test_left_right_imbalance_at_root_insertion_to_list(self):
        self.__BST.insert_element(20)
        self.__BST.insert_element(0)
        self.__BST.insert_element(50)
        self.__BST.insert_element(-5)
        self.__BST.insert_element(5)
        self.__BST.insert_element(3)
        self.assertEqual([ -5, 0, 3, 5, 20, 50 ], self.__BST.to_list())

    def test_right_left_imbalance_at_root_insertion_to_list(self):
        self.__BST.insert_element(30)
        self.__BST.insert_element(5)
        self.__BST.insert_element(50)
        self.__BST.insert_element(40)
        self.__BST.insert_element(70)
        self.__BST.insert_element(35)
        self.assertEqual([ 5, 30, 35, 40, 50, 70 ], self.__BST.to_list())

    def test_to_list_for_empty_tree(self):
        self.assertEqual([], self.__BST.to_list())

    def test_to_list_for_one_node_tree(self):
        self.__BST.insert_element(20)
        self.assertEqual([20], self.__BST.to_list())

if __name__ == '__main__':
  unittest.main()
