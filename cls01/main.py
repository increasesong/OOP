import re
txt = '''我的电子邮件tom@gmail.com。
将什么发送到jerry123@163.com或者3123432@qq.com.
若遇特殊情况打电话给182123445678.'''

email_list = re.findall(r'[a-zA-Z0-9_]+@[a-zA-Z0-9]+\.[a-zA-Z]+', txt)
phone_list = re.findall(r'[0-9]{11,}', txt)
print('email_list:', email_list)
print('phone_list:', phone_list)
