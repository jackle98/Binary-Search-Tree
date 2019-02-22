class Binary_Search_Tree:
  # TODO.I have provided the public method skeletons. You will need
  # to add private methods to support the recursive algorithms
  # discussed in class

  class __BST_Node:
    # TODO The Node class is private. You may add any attributes and
    # methods you need. Recall that attributes in an inner class
    # must be public to be reachable from the the methods.

    def __init__(self, value):
      self.value = value
      self.height = 0
      self.right_child = None
      self.left_child = None

  def __init__(self):
    self.__root = None
    self.string = "[" + " "
    self.max = None
    self.end = None
    self.list = []
    # TODO complete initialization

  def insert_element(self, value):
      if self.__root == None:
          self.__root = self.__BST_Node(value)
          self.__root.height = 1
      else:
          self.__root = self.__recursive_insert(value, self.__root)
    # Insert the value specified into the tree at the correct
    # location based on "less is left; greater is right" binary
    # search tree ordering. If the value is already contained in
    # the tree, raise a ValueError. Your solution must be recursive.
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
    # TODO replace pass with your implementation

  def __recursive_insert(self, value, current_node):
      if current_node == None:
          current_node = self.__BST_Node(value)
          current_node.height = 1
          return current_node
      if value < current_node.value:
          current_node.left_child = self.__recursive_insert(value, current_node.left_child)
          self.__update_height(current_node)
      elif value > current_node.value:
          current_node.right_child = self.__recursive_insert(value, current_node.right_child)
          self.__update_height(current_node)
      elif value == current_node.value:
          raise ValueError
      return self.__balance(current_node)

  def remove_element(self, value):
      if self.__root == None:
          raise ValueError
      self.__root = self.__recursive_remove(value, self.__root)
    # Remove the value specified from the tree, raising a ValueError
    # if the value isn't found. When a replacement value is necessary,
    # select the minimum value to the from the right as this element's
    # replacement. Take note of when to move a node reference and when
    # to replace the value in a node instead. It is not necessary to
    # return the value (though it would reasonable to do so in some
    # implementations). Your solution must be recursive.
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
    # TODO replace pass with your implementation

  def __recursive_remove(self, value, current_node):
      if current_node == None:
          raise ValueError
      if value < current_node.value:
          current_node.left_child = self.__recursive_remove(value, current_node.left_child)
          self.__update_height(current_node)
      elif value > current_node.value:
          current_node.right_child = self.__recursive_remove(value, current_node.right_child)
          self.__update_height(current_node)
      elif value == current_node.value:
          if current_node.left_child == None:
              holder = current_node.right_child
              current_node = None
              return holder
          elif current_node.right_child == None:
              holder = current_node.left_child
              current_node = None
              return holder
          else:
              holder = self.__find_min(current_node.right_child)
              current_node.value = holder.value
              current_node.right_child = self.__recursive_remove(holder.value, current_node.right_child)
      return self.__balance(current_node)

  def __balance(self, current_node):
      if self.__balance_calc(current_node) == -2:
          if self.__balance_calc(current_node.left_child) == -1 or self.__balance_calc(current_node.left_child) == 0:
              old_root = current_node
              floater = current_node.left_child.right_child
              current_node = current_node.left_child
              current_node.right_child = old_root
              current_node.right_child.left_child = floater
              self.__update_height(current_node.right_child)
              self.__update_height(current_node)
          elif self.__balance_calc(current_node.left_child) == 1:
              #first rotation
              first_root = current_node.left_child
              floater = first_root.right_child.left_child
              current_node.left_child = current_node.left_child.right_child
              current_node.left_child.left_child = first_root
              current_node.left_child.left_child.right_child = floater
              self.__update_height(current_node.left_child.left_child)
              self.__update_height(current_node.left_child)
              #second rotation
              second_root = current_node
              floater2 = current_node.left_child.right_child
              current_node = current_node.left_child
              current_node.right_child = second_root
              current_node.right_child.left_child = floater2
              self.__update_height(current_node.right_child)
      elif self.__balance_calc(current_node) == 2:
          if self.__balance_calc(current_node.right_child) == 1 or self.__balance_calc(current_node.right_child) == 0:
              old_root = current_node
              floater = current_node.right_child.left_child
              current_node = current_node.right_child
              current_node.left_child = old_root
              current_node.left_child.right_child = floater
              self.__update_height(current_node.left_child)
          elif self.__balance_calc(current_node.right_child) == -1:
              #first rotation
              first_root = current_node.right_child
              floater = first_root.left_child.right_child
              current_node.right_child = current_node.right_child.left_child
              current_node.right_child.right_child = first_root
              current_node.right_child.right_child.left_child = floater
              self.__update_height(current_node.right_child.right_child)
              self.__update_height(current_node.right_child)
              #second rotation
              second_root = current_node
              floater2 = current_node.right_child.left_child
              current_node = current_node.right_child
              current_node.left_child = second_root
              current_node.left_child.right_child = floater2
              self.__update_height(current_node.left_child)
      return current_node



  def __balance_calc(self, current_node):
      if current_node.left_child == None:
          left_height = 0
      elif current_node.left_child != None:
          left_height = current_node.left_child.height
      if current_node.right_child == None:
          right_height = 0
      elif current_node.right_child != None:
          right_height = current_node.right_child.height
      balance = right_height - left_height
      return balance

  def __update_height(self, current_node):
      if current_node != None:
          if current_node.left_child == None and current_node.right_child == None:
              current_node.height = 1
          if current_node.left_child == None and current_node.right_child != None:
              current_node.height = current_node.right_child.height + 1
          if current_node.right_child == None and current_node.left_child != None:
              current_node.height = current_node.left_child.height + 1
          if current_node.right_child != None and current_node.left_child != None:
              if current_node.right_child.height > current_node.left_child.height:
                  current_node.height = current_node.right_child.height + 1
              if current_node.left_child.height > current_node.right_child.height:
                  current_node.height = current_node.left_child.height + 1
              if current_node.left_child.height == current_node.right_child.height:
                  current_node.height = current_node.left_child.height + 1





  def __find_max(self, root):
      if root.right_child != None:
          self.__find_max(root.right_child)
      else:
          self.max = root.value
          return self.max

  def __find_end(self, root):
      if root.right_child != None:
          self.__find_end(root.right_child)
      elif root.right_child == None and root.left_child != None:
          self.__find_end(root.left_child)
      else:
          self.end = root.value
          return self.end

  def __find_min(self, current_node):
      while current_node.left_child != None:
          current_node = current_node.left_child
      return current_node

  def in_order(self):
      if self.__root == None:
          in_order = "[" + " " + "]"
      else:
          self.__find_max(self.__root)
          in_order = self.__recursive_in_order(self.__root) + "]"
      self.string = "[" + " "
      self.max = None
      return in_order
    # Construct and return a string representing the in-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed as [ 4 ]. Trees with more
    # than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control
    # variable.
    # TODO replace pass with your implementation

  def __recursive_in_order(self, current_node):
      if current_node != None:
          self.__recursive_in_order(current_node.left_child)
          if current_node.value == self.max:
              self.string += str(current_node.value) + " "
          else:
              self.string += str(current_node.value) + "," + " "
          self.__recursive_in_order(current_node.right_child)
      return self.string

  def to_list(self):
      if self.__root == None:
          in_order_list = []
      else:
          in_order_list = self.__recursive_to_list(self.__root)
      self.list = []
      return in_order_list

  def __recursive_to_list(self, current_node):
      if current_node != None:
          self.__recursive_to_list(current_node.left_child)
          self.list.append(current_node.value)
          self.__recursive_to_list(current_node.right_child)
      return self.list




  def pre_order(self):
      if self.__root == None:
          pre_order = "[" + " " + "]"
      else:
          pre_order = self.__recursive_pre_order(self.__root)
          pre_order += "]"
      self.string = "[" + " "
      self.end = None
      return pre_order

    # Construct and return a string representing the pre-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control
    # variable.
    # TODO replace pass with your implementation

  def __recursive_pre_order(self, current_node):
      self.__find_end(self.__root)
      if current_node != None:
          if current_node.value == self.end:
              self.string += str(current_node.value) + " "
          else:
              self.string += str(current_node.value) + "," + " "
          if current_node.left_child != None:
              self.__recursive_pre_order(current_node.left_child)
          if current_node.right_child != None:
              self.__recursive_pre_order(current_node.right_child)
      return self.string

  def post_order(self):
      if self.__root == None:
          post_order = "[" + " " + "]"
      else:
          post_order = self.__recursive_post_order(self.__root)
          post_order += "]"
      self.string = "[" + " "
      return post_order
    # Construct an return a string representing the post-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control
    # variable.
    # TODO replace pass with your implementation

  def __recursive_post_order(self, current_node):
      if current_node != None:
          if current_node.left_child != None:
              self.__recursive_post_order(current_node.left_child)
          if current_node.right_child != None:
              self.__recursive_post_order(current_node.right_child)
          if current_node == self.__root:
              self.string += str(current_node.value) + " "
          else:
              self.string += str(current_node.value) + "," + " "
      return self.string

  def get_height(self):
      if self.__root == None:
          return 0
      elif self.__root.left_child == None and self.__root.right_child == None:
          return self.__root.height
      return self.__root.height
    # return an integer that represents the height of the tree.
    # assume that an empty tree has height 0 and a tree with one
    # node has height 1. This method must operate in constant time.
    # TODO replace pass with your implementation

  def __str__(self):
    return self.in_order()

if __name__ == '__main__':
    BST = Binary_Search_Tree()
    BST.insert_element(44)
    BST.insert_element(20)
    BST.insert_element(50)
    BST.insert_element(60)
    BST.insert_element(48)
    print(BST.get_height())
    print(BST.pre_order())
    BST.insert_element(46)
    print(BST.get_height())
    print(BST.pre_order())
  #unit tests make the main section unnecessary.
