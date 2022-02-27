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


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cache_sort = []
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache_sort.remove(key)
            self.cache_sort.insert(0, key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.cache_sort.remove(key)
            self.cache_sort.insert(0, key)
        else:
            if len(self.cache) < self.capacity:
                self.cache[key] = value
            else:
                r_key = self.cache_sort.pop(-1)
                del self.cache[r_key]
                self.cache[key] = value
            self.cache_sort.insert(0, key)


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
            print(f'put {lst2[i]}: ', obj.cache, obj.cache_sort)
        elif lst1[i] == 'get':
            print(f'get {lst2[i][0]}: ', obj.get(lst2[i][0]))
