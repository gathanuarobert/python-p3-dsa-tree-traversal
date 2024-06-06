class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    pass
    def dfs(node):
      if node['id'] == id:
        return node
      for child in node['children']:
        result = dfs(child)
        if result:
          return result
      return None
    return dfs(self.root)    
  

  def breadth_first_traversal(node):
    result = []
    nodes_to_visit = [node]
    while len(nodes_to_visit) > 0:
      node = nodes_to_visit.pop(0)
      result.append(node['value'])
      nodes_to_visit = nodes_to_visit + node['children']

    return result

  def braedth_first_traversal(node):
    result = []
    nodes_to_visit = [node]
    while len (nodes_to_visit) > 0:
      nodde = nodes_to_visit.pop(0)
      result.append(node['value'])
      nodes_to_visit = node['children'] + nodes_to_visit

    return result

  def depth_first_traversal(node, result = []):
    result.append(node['value'])
    for child in node['children']:
      depth_first_traversal(child, result)

    return result  
