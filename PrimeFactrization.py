# -*- coding: utf-8 -*-


def prime_factorization(n: int) -> dict[int, int]:
    '''
    Factorize a natural number n.
    >>> prime_factorization(1991)
    {11: 1, 181: 1}
    >>> prime_factorization(25)
    {5: 2}
    '''
    assert isinstance(n, int)
    assert n > 1

    res: dict[int, int] = {}
    for i in range(2, int(n ** .5) + 1):
        while n % i == 0:
            res[i] = res.get(i, 0) + 1
            n //= i
    if n != 1:
        res[n] = 1
    return res


if __name__ == '__main__':

    import doctest

    doctest.run_docstring_examples(prime_factorization, globals())
