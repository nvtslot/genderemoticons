# genderemoticons
A script to determine the total usage of certain emoticons for men and women.

# Example usage
zless /net/corpora/twitter2/Tweets/2018/03/*.out.gz | /net/corpora/twitter2/tools/tweet2tab user text | python get-gender.py | python genderemoticons.py
