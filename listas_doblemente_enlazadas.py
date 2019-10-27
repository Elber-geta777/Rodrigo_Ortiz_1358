class NodoDoble:
    def __init__(self, value, siguiente, previo):
        self.data = value
        self.next = siguiente
        self.prev = previo

"""
ADT Lista Doblemente Ligada

ListaDoblementeEnlazada()
get_size() -> Regresa el número de elementos que haya en la cola
insert(value) -> Inserta un dato al final
find_from_head(value) -> Entra a la cabeza y busca hacia la derecha
find_from_tail(value) -> Entra a la cola y busca hacia la izquierda
remove_from_head(value) -> Entra a la cabeza y borra el primer elemento que encuentre hacia la derecha
remove_from_tail(value) -> Entra a la cola y borra el primer elemento que encuentre hacia la izquierda
insert_between(value,predecesor,sucesor) -> Inserta un dato entre dos nodos
transversal() -> Imprime los nodos de head a tail
reverse_transversal() -> Imprime los nodos de tail a head
"""
class DoubleLinkedList:
    def __init__(self):
        self.__head = NodoDoble(None, None, None)
        self.__tail = NodoDoble(None, None, None)
        self.__head.next = self.__tail
        self.__tail.prev = self.__head
        self.__size = 0

    def get_size(self):
        return self.__size

    def insert(self, value):
        """ Inserta al Final """
        if self.__size == 0:
            nuevo = NodoDoble(value, self.__tail, self.__head)
            self.__head.next = nuevo
            self.__tail.prev = nuevo
        else:
            nuevo = NodoDoble(value, self.__tail, self.__tail.prev)
            self.__tail.prev.next = nuevo
            self.__tail.prev = nuevo
        self.__size +=1

    def transversal(self):
        curr_Node = self.__head
        while curr_Node.next != None:
            print(curr_Node.data, "->", end="")
            curr_Node = curr_Node.next
        print("")

    def reverse_transversal(self):
        curr_Node = self.__tail
        while curr_Node.prev != None:
            print(curr_Node.data, "->", end="")
            curr_Node = curr_Node.prev
        print("")

    def find_from_head(self, value):
        curr_Node = self.__head
        encontrado = None
        while curr_Node.data is not value:
            curr_Node = curr_Node.next
        if curr_Node.data == value:
            encontrado = curr_Node
        return encontrado

    def find_from_tail(self, value):
        encontrado = None
        curr_Node = self.__tail
        while curr_Node.data is not value:
            curr_Node = curr_Node.prev
        if curr_Node.data == value:
            encontrado = curr_Node
        return encontrado

    def remove_from_head(self, value):
        encontrado = self.find_from_head(value)
        encontrado.next.prev = encontrado.prev
        encontrado.prev.next = encontrado.next
        self.__size -= 1

    def remove_from_tail(self, value):
        encontrado = self.find_from_tail(value)
        encontrado.prev.next = encontrado.next
        encontrado.next.prev = encontrado.prev
        self.__size -= 1

    def insert_between(self, value, predecesor, sucesor):
        head = self.find_from_head(predecesor)
        tail = self.find_from_tail(sucesor)
        nuevo = NodoDoble(value, tail, head)
        head.next = nuevo
        tail.prev = nuevo
        self.__size += 1

def main():
    dll = DoubleLinkedList()
    dll.insert(10)
    dll.insert(20)
    dll.insert(30)
    dll.transversal()
    dll.insert_between(15, 10, 20)
    dll.transversal()
    print(f"Get size: {dll.get_size()}")
    dll.reverse_transversal()
    print(f"Find from head: {dll.find_from_head(10)}")
    print(f"Find from tail: {dll.find_from_tail(20)}")
    dll.remove_from_head(10)
    dll.remove_from_tail(30)
    dll.transversal()
    print(f"Get size: {dll.get_size()}")

main()














