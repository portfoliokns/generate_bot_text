import random
import pickle
import re
from tqdm import tqdm
from janome.tokenizer import Tokenizer
from collections import Counter
from collections import defaultdict

BEGIN = '__BEGIN__'
END = '__END__'

def clear_text(text):
    """入力された文章データから不必要な文字を消す"""
    text = text.replace('|', '').replace('　', '')
    text = re.sub('《\w+》', '', text)
    text = re.sub(' [＃\w+]', '', text)
    text = text.replace('\r', '').replace('\n', '')
    text = re.sub('[、「」？]', '', text)
    text = re.sub('（\w+）', '', text)
    text = re.sub('［\w+］', '', text)

    return text

def generate_text(first_words, first_weights, markov_dict):
    """入力されたデータをもとに文章を生成する"""
    first_word = random.choice(first_words) 
    generate_words = [BEGIN, first_word]
    while True:
        pair = tuple(generate_words[-2:])
        words = markov_dict[pair]['words']
        weights = markov_dict[pair]['weights']
        next_word = random.choices(words, weights=weights)[0]
        if next_word == END:
            break
        generate_words.append(next_word)

    return ''.join(generate_words[1:])

def get_three_words_list(sentence):
    t = Tokenizer()
    words = list(t.tokenize(sentence, wakati=True))
    words = [BEGIN] + words + [END]
    three_words_list = []
    for i in range(len(words) - 2):
        three_words_list.append(tuple(words[i:i+3]))
    return three_words_list

def generate_markov_dict(three_words_count):
    """マルコフ連鎖での文章生成用の辞書データを生成する"""
    markov_dict = {}
    for three_words, count in three_words_count.items():
        two_words = three_words[:2]
        next_word = three_words[2]
        if two_words not in markov_dict:
            markov_dict[two_words] = {'words': [], 'weights': []}
        markov_dict[two_words]['words'].append(next_word)
        markov_dict[two_words]['weights'].append(count)
    return markov_dict

def get_first_words_weights(three_words_count):
    first_word_count = get_first_word_and_count(three_words_count)
    words = []
    weights = []
    for word, count in first_word_count.items():
        words.append(word)
        weights.append(count)
    return words, weights

def get_first_word_and_count(three_words_count):
    """最初の単語を選択するための辞書データを作成する"""
    first_word_count = defaultdict(int)

    for three_words, count in three_words_count.items():
        if three_words[0] == BEGIN:
            next_word = three_words[1]
            first_word_count[next_word] += count
    return first_word_count

def calc_markov(text):
    text = clear_text(text)
    sentences = text.split('。')
    print('生成に使用する文の数はおおよそ', len(sentences), '個あります。')

    three_words_list = []
    for sentence in tqdm(sentences):
        three_words_list += get_three_words_list(sentence)
    three_words_count = Counter(three_words_list)

    markov_dict = generate_markov_dict(three_words_count)
    first_words, first_weights = get_first_words_weights(three_words_count)

    results = []
    for _ in range(5):
        sentence = generate_text(first_words, first_weights, markov_dict)
        results.append(sentence)

    #print(results)
    return results

