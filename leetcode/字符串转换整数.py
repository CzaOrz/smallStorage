import re
"""
����'(^[\-\+]?\d+)'
���[0:1]��get���ˡ�����Ҫ��if�ж�
"""
class Solution:
    def myAtoi(self, s: str) -> int:
        return max(min(int(*re.findall('(^[\+\-]?\d+)', s.strip())[0:1] or '0'), 2**31 - 1), -2**31)