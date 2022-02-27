"""
请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
实现 LRUCache 类：
LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lru-cache
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class listNode(object):
    def __init__(self, key, value, prev=None, next=None):
        super(listNode, self).__init__()
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class linkedList(object):
    def __init__(self):
        super(linkedList, self).__init__()
        self.head = None
        self.tail = None

    def addNode(self, node: listNode) -> listNode:
        if not self.head:
            self.head = node
            self.tail = node
            return node
        self.tail.next = node
        node.prev = self.tail
        node.next = None
        self.tail = node
        return node

    def removeNode(self, node: listNode) -> listNode:
        if self.head == node:
            self.head = node.next
        if self.tail == node:
            self.tail = node.prev
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        return node

    def moveToTail(self, node: listNode) -> None:
        node = self.removeNode(node)
        self.addNode(node)

    def removeHead(self) -> listNode:
        return self.removeNode(self.head)


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.link_list = linkedList()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.link_list.moveToTail(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.link_list.moveToTail(node)
        else:
            if len(self.cache) < self.capacity:
                node = listNode(key, value)
                self.link_list.addNode(node)
            else:
                node = self.link_list.removeHead()
                del self.cache[node.key]
                node.key, node.value = key, value
                self.link_list.addNode(node)
            self.cache[key] = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

"""
["LRUCache","put","put","get","put","get","put","get","get","get"]
[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
输出：
[null,null,null,1,null,-1,null,1,-1,4]
预期结果：
[null,null,null,1,null,-1,null,-1,3,4]

["LRUCache","put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]
[[10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]

[null,null,null,null,null,null,-1,null,19,17,null,-1,null,null,null,-1,null,-1,5,-1,12,null,null,3,5,5,null,null,1,null,-1,null,30,5,30,null,null,null,-1,null,-1,24,null,null,18,null,null,null,null,-1,null,null,18,null,null,-1,null,null,null,null,null,-1,null,null,24,null,4,29,-1,null,12,-1,null,null,null,null,29,null,null,null,null,17,22,-1,null,null,null,24,null,null,null,20,null,null,null,29,-1,-1,null,null,null,null,20,null,null,null,null,null,null,null]
[null,null,null,null,null,null,-1,null,19,17,null,-1,null,null,null,-1,null,-1,5,-1,12,null,null,3,5,5,null,null,1,null,-1,null,30,5,30,null,null,null,-1,null,-1,24,null,null,18,null,null,null,null,-1,null,null,18,null,null,-1,null,null,null,null,null,18,null,null,-1,null,4,29,30,null,12,-1,null,null,null,null,29,null,null,null,null,17,22,18,null,null,null,-1,null,null,null,20,null,null,null,-1,18,18,null,null,null,null,20,null,null,null,null,null,null,null]
"""
if __name__ == '__main__':
    obj = None
    lst1 = ["LRUCache","put","put","get","put","get","put","get","get","get"]
    lst2 = [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
    lst1 = ["LRUCache","put","put","put","put","get","get"]
    lst2 = [[2],[2,1],[1,1],[2,3],[4,1],[1],[2]]
    for i in range(len(lst1)):
        if lst1[i] == 'LRUCache':
            obj = LRUCache(int(lst2[i][0]))
        elif lst1[i] == 'put':
            obj.put(*lst2[i])
            print(f'put {lst2[i]}: ', {each.key: each.value for each in obj.cache.values()})
        elif lst1[i] == 'get':
            print(f'get {lst2[i][0]}: ', obj.get(lst2[i][0]))
