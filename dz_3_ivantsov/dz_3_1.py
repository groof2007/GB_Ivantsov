def num_translate(value: str):
    dict_nums = {
      'one': 'один',
      'two': 'два',
      'three': 'три',
      'four': 'четыре',
      'five': 'пять',
      'six': 'шесть',
      'seven': 'семь',
      'eight': 'восемь',
      'nine': 'девять',
      'ten': 'десять'
   }
    str_out = dict_nums.get(value)
    return str_out
print(num_translate('one'))
print(num_translate('ten'))