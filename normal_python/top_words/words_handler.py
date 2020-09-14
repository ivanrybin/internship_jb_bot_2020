from top_words.requester import get_response


# Сбор сообщений из json ответа
def get_messages_from_response(json_response):
    messages = []
    for commit in json_response:
        if 'commit' in commit and 'message' in commit['commit']:
            messages.append(commit['commit']['message'])
    return messages


# Сбор топ 30 слов с учетом регистра и без (пропускаем символы и цифры)
def get_top_30_words(messages):
    bad_signs = ['.', ',', '!', '/', '\\', "#", '$', '%', '^', '*', '(', ')', '@', '>', '<', ' ']
    all_words = [word for message in messages for word in message.split(' ') if word]
    all_words = [word.strip() for word in all_words if word not in bad_signs and not word.isdigit()]

    words_any_case = dict()
    words_lower_case = dict()

    for word in all_words:
        if word not in words_any_case:
            words_any_case[word] = 0
        if word.lower() not in words_lower_case:
            words_lower_case[word.lower()] = 0

        words_any_case[word] += 1
        words_lower_case[word.lower()] += 1

    words_any_case = {k: v for k, v in list(
        sorted(words_any_case.items(), reverse=True, key=lambda item: item[1])
    )[:30]
                      }
    words_lower_case = {k: v for k, v in list(
        sorted(words_lower_case.items(), reverse=True, key=lambda item: item[1])
    )[:30]
                        }
    return words_any_case, words_lower_case


def pretty_print(words):
    print("{: <15} {}".format("words", "count"))
    for word, cnt in words.items():
        print("{: <15} {}".format(word, cnt))


def find_top_words(user=None, token=None):
    # берем первые 100 коммитов с проекта Kotlin
    url = 'https://api.github.com/repos/JetBrains/kotlin/commits?per_page=100'
    response = get_response(url, user, token)
    content = response.json()
    messages = get_messages_from_response(content)
    words_any_case, words_lower_case = get_top_30_words(messages)
    return words_any_case, words_lower_case
