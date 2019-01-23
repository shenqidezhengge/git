# number = input('>:')
#
#
# def phone(number):
#     if len(number) == 11 and number.startswith('1') and number.isdigit():
#         return True
#     else:
#         return False
#
#
# print(phone(number))


# import re
#
# a = '12345678901'
# number = re.match('1\d{10}', a)
# b = re.search('1\d{10}', a)
# print(number)
# print(b)

import re
# print(re.search('a', 'abc'))
# print(re.search('.', 'ab.c'))
# print(re.search(r'\ba\b', 'abc a abc'))  # 匹配单词头或单词尾
# print(re.search(r'\bhello\b', 'abchello hello helloabc'))

# print(re.search(r'.', '\tab.c'))  # 匹配任意字符，除了\n
# print(re.search(r'\d', '\rabc a 23456abc'))  # 匹配0-9数字
# print(re.search(r'\s', '\nabc a 23456abc'))  # 空白，制表符，换行
# print(re.search(r'\S', '\nabc a 23456abc'))  # 空白，制表符，换行
# print(re.search(r'\w', '\n_1abc a 23456abc'))
# print(re.search(r'\.', '\n_1abc. a 23456abc'))
# print(re.search(r'\D', '_\n_1abc. a 23456abc'))
# print(re.search(r'\ba\b', 'abc a abc'))  # 匹配单词头或单词尾
# print(re.search(r'\Ba\B', 'abc bab abc'))  # 匹配单词头或单词尾

# print(re.search(r'^ab', 'ab\n_1ab&c a 23456abc'))
# print(re.search(r'c$', 'ab\n_1ab&c a 23456abc'))
# print(re.findall(r'\d{0,1}', '123abc, a 234566abc1234jk;mn.23456'))
# print(re.findall(r'\d+', '123abc, a 234566abc1234jk;mn.23456'))
# print(re.findall('\d+', '123abc, a 234566abc1234jk;mn.23456'))
# print(re.findall('\d+?', '123abc, a 234566abc1234jk;mn.23456'))

# st = '<html>aaaa</html><td>bbb</td>'
# print(re.findall('<.*>', st))
# print(re.findall('<.*?>', st))
# print(re.findall('<.+?>', st))

# print(re.findall(r'(ab)?(cd)', '/123|abc,:; a 2345661abe|c1234jk 1abcde;mn.23456'))
# print(re.findall('[\w]', '123|abc, a 234566ab|c1234jk;mn.23456'))
# print(re.findall('\w', '123|abc, a 234566ab|c1234jk;mn.23456'))

# command = re.compile(r'\d')
# msg = command.findall('1234567890asdfghjkl;')
# print(msg)
#
# s = re.search('a', 'abc')
# print(s.group())
# print(s.start())
# print(s.end())
# print(s.span())
# print(re.split(r'[\s|c]', 'acss c ee'))


# nu = input('please input phone number: ')
#
#
# def phone_number(st):
#     st = str(st)
#     if len(st) == 11 and st.isdigit() and st.startswith('1'):
#         return True
#     else:
#         print('Phone Number Error')
#         return False
#
#
# print(phone_number(nu))


# import re
# nu = input('please input phone number: ')
# r = re.match(r'1\d{10}', nu)
# print(r)
# # print('\n'.join(dir(r)))
# print(r.span())


# print(re.search('a', 'abc'))
# print(re.search('.', 'ab.cd.de'))
# print(re.search('\.', 'ab.cd.de'))
# print(re.search('^ab', 'ab.cd.de'))
# print(re.search('de$', 'ab.cd.de'))
# print(re.search('a{2}', 'aab.cd.de'))
# print(re.findall('a+', 'aab.cd.de'))
# print(re.findall('a*', 'aab.cd.de'))
# print(re.findall('a?', 'aab.cd.de'))
# print(re.findall('[abcd]', 'aab.cd.de'))
# print(re.findall(r'.(ab)', 'aab.abcd.de'))
# print(re.findall('a|b', 'aab.abcd.de'))
# print(re.search('\bs\b', 'sabcsd s w'))
# print(re.search(r'\bs\b', 'sabcsd s w'))
# print(re.search(r'.', 'hc'))
# print(re.search(r'.', '\nhc'))
# print(re.search(r'.', '\rhc'))
# print('abcdefghijk\r\r\r\r\r\r\r\r\r\r')
# print('*' * 8)
# print(re.search(r'\d', 'ab12'))


# fp = open('1.txt', 'w')
# print('aaaaa\taaaa\taaa\taa\ta')
# print('abc def')
# print('abc\tdef')
# print('abc\ndef')
# print('abc\rdef')
# print('abc\fdef', file=fp)
# print('abc\vdef')

import re
# print(re.A)
# # decimal digit: [0-9]
# print(re.search(r'\d', '１ab12', flags=re.A))
# # whitespace characters, [ \t\n\r\f\v]
# print(re.search(r'\s', 'ab 12'))
# # word characters: characters, numbers and underscore
# print(re.search(r'\w', '_ab 12'))
# print(re.search(r'\.', 'adc.123'))
# print(re.search(r'\D', 'adc123'))
# print(re.search(r'^a', 'adc 123'))
# print(re.search(r'3$', 'adc 123'))
# print(re.findall(r'\d{1,3}', '12ab23344'))
# print(re.findall(r'\d*', '12ab23344'))
# print(re.findall(r'\d*?', '12ab23344'))
# print(re.findall(r'\d+', '12ab23344'))
# print(re.findall(r'\d+?', '12ab23344'))
# print(re.findall(r'\d?', '12ab23344'))
# st = "<html>aaaa</html><td>bbbb</td>"
# print(re.findall(r'<.*>', st))
# print(re.findall(r'<.*?>', st))
# print(re.findall(r'[\d]', '12ab23344'))
# print(re.findall(r'[ab]', '12ab23344'))
# print(re.findall(r'[a|b]', '12ab23344'))
# print(re.findall(r'(2|3)', '12ab.?*(){}23344'))
# print(re.findall(r'(\d)', '21abc323'))
# print(re.findall(r'(^2)', '21abc323'))
# # ['2']

# r = re.compile(r'\d')
# print(r.findall('123ab12'))
# print(re.sub('i', 'o', 'pythin', 1))
# print(re.split(r'\s', 'agg bbw cee'))
# print('agg bbw cee'.split(' '))
# print(re.split(r'[\s]', 'egg bbw cee'))
# print(re.split(r'\s', 'cee'))
# print(re.split(r'[\s,]', 'egg bbw,a cee'))


# r = re.match(r'\d', '1223ag')
# print(r)
# print(re.match(r'\d', 'ad1223ag'))
# print(re.search(r'\d', 'ad1223ag'))
# print(r.group())
# print(r.start())
# print(r.end())
# print(r.span())
# print(re.findall(r'[.?*(){}]', '.?*(){}'))
# print(re.findall(r'[0-9]', 'asdfghjklqwertyuiopzxcvbnm1234567890'))
# print(re.findall(r'[\d]', 'asdfghjkl12345'))
# print(re.findall(r'[a-z]', 'qwertyuiop12345'))
# print(re.findall(r'[^a-z]', 'zxcvbnm12345'))
# print(re.findall(r'z|x|c|v|b|n|m', 'zxcvbnm'))
# print(re.findall(r'(2|3)', '12ab.?*(){}23344'))
# print(re.findall(r'(\d)', '21abc323'))
# print(re.findall(r'(^2)', '21abc323'))

class A:
    def show(self):
        print('base show')


class B(A):
    def show(self):
        print('B show')


obj = B()
obj.show()
