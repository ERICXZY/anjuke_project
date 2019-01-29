# -*- coding=utf-8 -*-
import ipdb


class PySort(object):
    def __init__(self, arr):
        """
        要明确每个算法的含义：根据定义书写代码
        特点：时间复杂度，空间复杂度，算法稳定性
        问题总结：
        1. 当列表实时改变后，正在循环的列表也会发生变化
        2. 大O推导法：
            用常数1取代运行时间中的所有加法常数
            在修改后的运行函数中，只保留最高阶项
            如果最高阶项存在且不是1，则去除与这个项相乘的常数
        3. T(n) = O(f(n)) f(n) 为n规模下操作次数的总和
        4. 等差数列求和公式：Sn=N(A1+An)/2
        5. 最大时间复杂度不一定是逆序情况下产生的
        6. 平均时间复杂度是：sum(pi*f(n)) pi是指某种情况出现的概率，f(n)是该情况的具体的时间复杂度
        7. 稳定：如果a原本在b前面，而a=b，排序之后a仍然在b的前面。
        8. 如果a原本在b的前面，而a=b，排序之后 a 可能会出现在 b 的后面。
        :param arr: int number list
        """
        self.arr = arr

    def bubble_sort(self):
        """
        bubble_sort: 依次比较相邻两个元素，如果乱序，则更换位置
        result:
        1. 比较相邻的元素。如果第一个比第二个大，就交换它们两个；
           对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对，这样在最后的元素应该会是最大的数；
           针对所有的元素重复以上的步骤，除了最后一个；
           重复步骤1~3，直到排序完成。
        2. 最小时间复杂度：在完全有序的情况下
                最外层第一次：n-1 次比较，0次交换位置
                最外层第二次：n-2 次比较，0次交换位置
                最外层第三次：n-3 次比较，0次交换位置
                最外层最后一次：1 次比较，0次交换位置
                综上：最小时间复杂度为 1 + 2 + ... + n-2 + n-1 = (n^2)/2 = O(n^2)
                但是网上说最小时间复杂度为 O(n), 说明可以进行优化，详见optimization_bubble_sort
        :return: order list
        """
        count = 0
        for range_index in range(len(self.arr) - 1):
            for index in range(len(self.arr) - range_index - 1):
                count += 1
                if self.arr[index] > self.arr[index + 1]:
                    self.arr[index], self.arr[index + 1] = self.arr[index + 1], self.arr[index]
                    count += 1
        return self.arr, count

    def optimization_bubble_sort(self):
        """
        优化后的 bubble_sort, 添加一个flag用于标记是否交换位置，如果已经没有位置的交换，就说明有序
        1. 最小时间复杂度：在完全有序的情况下
            最外层第一次：比较 n-1 次，不交换位置，直接退出 最小时间复杂度为 n-1=O(n)
        2. 最大时间复杂度：在逆序情况下
            最外层第一次：比较 n -1 次，交换位置 n - 1 次
            最外层第二次：比较 n -2 次，交换位置 n - 2 次
            ......
            最外层最后一次：比较 1 次，交换位置 1 次
            综上最大时间复杂度为：2（1 + 2 + .. + n -2 + n - 1）= 2 *（n-1）* (1+n-1)/2 = O(n^2)
        3. 平均时间复杂度为：n ^ 2
        4. 稳定排序算法
        :return:
        """
        count = 0
        for range_index in range(len(self.arr) - 1):
            is_sort = True
            for index in range(len(self.arr) - range_index - 1):
                count += 1
                if self.arr[index] > self.arr[index + 1]:
                    self.arr[index], self.arr[index + 1] = self.arr[index + 1], self.arr[index]
                    is_sort = False
                    count += 1
            if is_sort:
                return self.arr, count, "mid"
        return self.arr, count, "end"

    def simple_selection_sort(self):
        """
        选择排序：在乱序区中选择出一个最大或者最小的数字，放在有序区的末尾
        比较次数固定：n*(n-1)/2, 交换次数0-->n-1次，逆序时，交换n/2次，赋值操作0-->3(n-1)
        1.最大时间复杂度：
            哪种情况会到达最大时间复杂度，如何计算，逆序的时间复杂度如何计算
        2.最小时间复杂度：顺序情况下
            最外层第一次：比较 n - 1次，赋值0次，交换0次
            最外层第二次：比较 n - 2次，赋值0次，交换0次
            最小时间复杂度为：T(n) = 1 + 2 + ... + n - 1 = (1+n-1)*(n-1)/2 = O(n^2/2)
        3. 不稳定的排序算法
        4. 平均时间复杂度：O(n^2)
        :return: order list
        """
        for j in range(len(self.arr) - 1):
            # 先假设最小数字的index
            min_index = j
            for i in range(j + 1, len(self.arr)):
                if self.arr[min_index] > self.arr[i]:
                    min_index = i
            self.arr[j], self.arr[min_index] = self.arr[min_index], self.arr[j]
        return self.arr

    def insertion_sort(self):
        """
        insertion sort: 假设第一个元素有序，从第二个元素开始，如果第二个元素小于第一个元素，
                        就插到第一个元素前面。第三个元素和第二个，第一个元素分别比较，如果
                        比某个元素小，就放到某个元素之前。
        1.最小时间复杂度：顺序
                        第一次循环：比较1次，交换0次
                        第二次循环：比较1次，交换0次
                        第n-1次循环：比较1次，交换0次
                        最小时间复杂度：O(n) = n - 1
        2. 最大时间复杂度：逆序
                        第一次循环：比较1次，交换1次
                        第二次循环：比较2次，交换1次
                        第n-1次循环：比较 n - 1次，交换 n - 1 次
                        最大时间复杂度：O(n) = 2*(1 + 2 + ... + n - 1) = (n-1)(n-1+1)=n(n-1)=O(n^2)
        :return: order list
        """
        for j in range(1, len(self.arr)):
            for i in range(j, 0, -1):
                if self.arr[i] < self.arr[i-1]:
                    self.arr[i], self.arr[i - 1] = self.arr[i - 1], self.arr[i]
                else:
                    break
        return self.arr

if __name__ == '__main__':
    """
    python py_sort.py
    """
    li_mid = [5, 1, 2, 6, 8, 4, 5, 3, 9, 0]
    li_min = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    li_max = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    sort_instance = PySort(li_mid)
    # sort_instance = PySort(li_min)
    # sort_instance = PySort(li_max)
    # print(sort_instance.bubble_sort())
    # print(sort_instance.optimization_bubble_sort())
    # print(sort_instance.simple_selection_sort())
    print(sort_instance.insertion_sort())
