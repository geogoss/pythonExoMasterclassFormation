# Liste chainée (linked list)
#
# Node (Noeud)
#  Data (données)
#  Next (élément suivant)
#

class LinkedList:
    def __init__(self, node):
        self.head = node

    def get_nb_nodes(self):
        c = 1
        n = self.head
        while n.next:
            c += 1
            n = n.next
        return c

    def get_all_data_as_list(self):
        l = []
        n = self.head
        while n.next:
            l.append(n.data)
            n = n.next

        l.append(n.data)
        return l

    def delete_node_from_data(self, data):
        n = self.head
        if n.data == data:
            self.head = n.next
            return
        prev = None
        while n.next:
            # n = n.next
            if n.next.data == data:
                n.next = n.next.next
                return
            prev = n
            n = n.next
                # A -> B -> C
                # A ------> C
        if n.data == data:
            # supprimer le tail
            prev.next = None

    # def_delete_node_at_index

    def insert_node_at_index(self, node, index):
        # 0 : head
        # fin : tail
        # index invalide : -1, trop grand => rien
        # insérer entre 2 nodes
        n = self.head
        i = 0

        if index == 0:
            node.next = n
            self.head = node
            return

        while n.next:
            if i+1 == index:
                node.next = n.next
                n.next = node
                return
            i = i+1
            n = n.next

        if i+1 == index:
            n.next = node
            node.next = None


class Node:
    def __init__(self, d):
        self.data = d
        self.next = None

    def set_next(self, node):
        self.next = node


node1 = Node("Bonjour") # head
node2 = Node("je")
node3 = Node("suis")
# <----- "la mère de"
node4 = Node("Toto") # tail

node1.set_next(node2)
node2.set_next(node3)
node3.set_next(node4)

linked_list = LinkedList(node1)
# linked_list.append_and_create_node("Bonjour")

#linked_list.delete_node_from_data("je")
node_insert = Node("la mère de")
linked_list.insert_node_at_index(node_insert, 3)

print("Nombre de noeuds:", linked_list.get_nb_nodes())
print("Toutes les data:", linked_list.get_all_data_as_list())

# ["Bonjour", "je", "suis", "Toto"]

