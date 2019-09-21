# encoding: utf-8

import sys
import argparse

def main():
    args = argparse.ArgumentParser(description='Test argparse function')
    # 添加一个参数用于获取姓名
    args.add_argument('name', type=str, help='你的名字')
    # 添加一个参数用于获取年龄
    args.add_argument('age', type=int, help='你的年龄')
    # 添加一个参数用于获取身份证号
    args.add_argument('-i', "--id", type=str, dest='id', help='身份编码')
    # 添加一个参数用于获取性别，并限制选择范围
    args.add_argument("--sex", type=str, help='性别', default='男', choices=['男', '女'])
    # 添加一个参数用户获取其他参数，不要求存在，参数个数不限制
    args.add_argument('-o', '--other', type=str, dest='other', help='其他参数', required=False, nargs='*')
    # 解析参数
    args = args.parse_args()

    print('args.name = ', args.name)
    print('args.age = ', args.age)
    print('args.id = ', args.id)
    print('args.sex = ', args.sex)
    print('args.other = ', args.other)


if __name__ == '__main__':
    main()
