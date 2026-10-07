# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 10:00:25 2026

@author: Z-xuan
"""

#5.动态规划
#5.1
def Find_expression(target):
    digits = "123456789"   # 固定的数字串，顺序不能变
    results = []           # 存所有符合条件的表达式

    # pos：当前处理到第几个数字（从0开始）
    # expr：当前表达式字符串
    # total：当前表达式算出来的值
    def dfs(pos, expr, total):
        # 边界条件：9个数字都处理完了
        if pos == len(digits):
            # 如果结果等于目标值，就存起来
            if total == target:
                results.append(expr)
            return

        # 从pos开始，尝试取1个、2个、...、直到最后一个数字，拼成一个数
        # 比如pos=1时，end可以是2、3、...、9
        # 对应拼成：2、23、234、...、23456789
        for end in range(pos + 1, len(digits) + 1):
            num_str = digits[pos:end]   # 取出数字字符串
            num = int(num_str)          # 转成整数

            if pos == 0:
                # 第一个数字，前面没有运算符，直接拼
                dfs(end, num_str, num)
            else:
                # 选择1：前面加 +
                dfs(end, expr + "+" + num_str, total + num)
                # 选择2：前面加 -
                dfs(end, expr + "-" + num_str, total - num)

    # 从第0个数字开始搜
    dfs(0, "", 0)

    # 打印所有结果
    for line in results:
        print(f"{line}={target}")

    return results

print("=== Find_expression(50) 的结果 ===")
Find_expression(50)


#5.2
from collections import defaultdict
import matplotlib.pyplot as plt

# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False


def count_all_solutions():
    digits = "123456789"
    count = defaultdict(int)   # key是数字，value是有多少种表达式能算出它

    def dfs(pos, expr, total):
        if pos == len(digits):
            count[total] += 1   # 每走完一种完整的表达式，计数+1
            return

        for end in range(pos + 1, len(digits) + 1):
            num_str = digits[pos:end]
            num = int(num_str)

            if pos == 0:
                dfs(end, num_str, num)
            else:
                dfs(end, expr + "+" + num_str, total + num)
                dfs(end, expr + "-" + num_str, total - num)

    dfs(0, "", 0)
    return count


# ========== 主程序 ==========
print("正在统计所有方案...")
count = count_all_solutions()

# 提取1~100的方案数，存入 Total_solutions 列表
Total_solutions = []
for target in range(1, 101):
    Total_solutions.append(count.get(target, 0))

print(f"统计完成！一共 {len(count)} 个不同的数字可以被表示出来。")

# ========== 找最大值和最小值 ==========
max_count = max(Total_solutions)
min_count = min(Total_solutions)

max_targets = [i + 1 for i, c in enumerate(Total_solutions) if c == max_count]
min_targets = [i + 1 for i, c in enumerate(Total_solutions) if c == min_count]

print(f"\n最多方案数：{max_count} 种")
print(f"  对应数字：{max_targets}")
print(f"\n最少方案数：{min_count} 种")
print(f"  对应数字：{min_targets}")

# ========== 画图 ==========
plt.figure(figsize=(12, 6))
plt.plot(range(1, 101), Total_solutions, 'b-', linewidth=1)

# 标出最大值
first_max = True
for target in max_targets:
    if first_max:
        plt.scatter(target, Total_solutions[target - 1], 
                    c='red', s=50, zorder=5, label='Maximum')
        first_max = False
    else:
        plt.scatter(target, Total_solutions[target - 1], 
                    c='red', s=50, zorder=5)

# 标出最小值
first_min = True
for target in min_targets:
    if first_min:
        plt.scatter(target, Total_solutions[target - 1], 
                    c='green', s=50, zorder=5, label='Minimum')
        first_min = False
    else:
        plt.scatter(target, Total_solutions[target - 1], 
                    c='green', s=50, zorder=5)

plt.xlabel('Target integer')
plt.ylabel('Number of solutions')
plt.title('Expression solutions for targets 1 to 100')
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()