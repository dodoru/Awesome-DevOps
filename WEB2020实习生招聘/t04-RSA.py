# 你听过非对称加密吗?
# 你了解过 RSA 吗?
# 不了解也没关系, 我们只需要学习理解使用算法, 就能站在巨人的肩膀上.
# 现在, 请你实现以下函数, 业务场景常见于ssh登录
# 温馨提示: 你可以自己实现算法, 也可以使用标准库或第三方库


def back(strs):

    strs = strs[::-1]

    return strs


def rsa_encode(message, public_key=back):
    """
    :param message: 明文消息
    :param public_key: 公钥
    :return: 密文消息
    """
    return public_key(str(message))


def rsa_decode(cipher_text, private_key=back):
    """
    :param cipher_text: 密文消息
    :param private_key: 密钥
    :return: 明文消息
    """
    return private_key(str(cipher_text))


print(rsa_encode("abc"))
print(rsa_decode(rsa_encode("abc")))