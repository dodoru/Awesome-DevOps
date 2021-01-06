"""
* 题目1: （要点：代码风格，请注意可维护性）

1: 请实现以下函数，输入错误码，返回错误信息，比如：
规则如下：

40000：输入的数据有误
40001 - 40019： 参数类型错误
40020 - 40039： 参数值格式错误
40040 - 40049： 参数值超出限制范围
40050 - 40079： 需要补充指定的参数值
40080 - 40099： URL的查询条件
QueryString无效

40100: 用户未登录
40104: 用户已注销

40300 - 40319：用户未授权
40320 - 40399: 用户权限不足

40500: http请求方法错误
"""


# python3
def get_error_msg(code):

    if code == 40000:
        return "输入的数据有错误"
    elif code in range(40001, 40020):
        return "参数类型错误"
    elif code in range(40020, 40040):
        return "参数值格式错误"
    elif code in range(40040, 40050):
        return "参数值超出限制范围"
    elif code in range(40050, 40080):
        return "需要补充指定的参数值"
    elif code in range(40080, 40100):
        return "URL的查询条件QueryString无效"
    elif code == 40100:
        return "用户未登录"
    elif code == 40104:
        return "用户已注销"
    elif code in range(40300, 40320):
        return "用户未授权"
    elif code in range(40320, 40400):
        return "用户权限不足"
    elif code == 40500:
        return "http请求方法错误"


num = int(input())
print(get_error_msg(num))