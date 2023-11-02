from ft_filter import ft_filter

if __name__ == '__main__':
    tests = [('Hello the World', 4, ["Hello", "World"]),
             ("Las Vegas Nevada", 4, ["Vegas", "Nevada"]),
             ("Salut les amis", 2, ["Salut", "les", "amis"]),
             ("", 0, []),
             ("abc def", 5, [])
    ]
    for text, n, result in tests:
        filtered_words = list(ft_filter(lambda word: len(word) > n, text.split()))
        if filtered_words == result:
            print('\033[32m  OK  \033[0m')
        else:
            print(f'\033[31m  NOK for ({text}, {n})[0m')