#!/usr/bin/python3
"""queries the Reddit API, parses the title of all hot articles, and prints a
sorted count of given keywords(case-insensitive, delimited by spaces.
Javascript should count as javascript, but java should not).
"""
import requests
import operator


def count_words(subreddit, word_list=[], word_dict={}, after=None):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) Apple' +
        'WebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }
    r = requests.get('https://www.reddit.com/r/{:}/hot.json?after={:}'.format(
        subreddit, after), headers=headers, allow_redirects=False)
    if r.status_code == 200:
        json = r.json()
        data_dict = json.get('data')
        post_list = data_dict.get('children')
        for post in post_list:
            post_data_dict = post.get('data')
            for word in word_list:
                title = post_data_dict.get('title').split()
                title_copy = []
                for j in title:
                    title_copy.append(j.upper())
                count = title_copy.count(word.upper())
                if word_dict.get(word):
                    word_dict[word] += count
                else:
                    word_dict[word] = count
        after = data_dict.get('after')
        if data_dict.get('after') is None:
            sorted_list = sorted(word_dict.items(), key=operator.itemgetter(1),
                                 reverse=True)
            for i in range(len(sorted_list) - 1):
                if sorted_list[i][1] == sorted_list[i+1][1]:
                    if sorted_list[i][0] > sorted_list[i+1][0]:
                        sorted_list[i], sorted_list[i+1] = sorted_list[
                            i+1], sorted_list[i]
            for item in sorted_list:
                if item[1] > 0:
                    print("{:}: {:}".format(item[0], item[1]))
            return
        return count_words(subreddit, word_list, word_dict, after)
    else:
        return
