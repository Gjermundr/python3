#!#/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser(description='Lots of dumb stuff')
parser.add_argument('-f', '--file', type=str, help='Cat a file to output')
parser.add_argument('-p', '--pikachu', action='store_true', help='Do you want a Pikachu?')
args = parser.parse_args()


def d_pikachu():
    print('''
█▀▀▄░░░░░░░░░░░▄▀▀█
░█░░░▀▄░▄▄▄▄▄░▄▀░░░█
░░▀▄░░░▀░░░░░▀░░░▄▀
░░░░▌░▄▄░░░▄▄░▐▀▀
░░░▐░░█▄░░░▄█░░▌▄▄▀▀▀▀█
░░░▌▄▄▀▀░▄░▀▀▄▄▐░░░░░░█
▄▀▀▐▀▀░▄▄▄▄▄░▀▀▌▄▄▄░░░█
█░░░▀▄░█░░░█░▄▀░░░░█▀▀▀
░▀▄░░▀░░▀▀▀░░▀░░░▄█▀
░░░█░░░░░░░░░░░▄▀▄░▀▄
░░░█░░░░░░░░░▄▀█░░█░░█
░░░█░░░░░░░░░░░█▄█░░▄▀
░░░█░░░░░░░░░░░████▀
░░░▀▄▄▀▀▄▄▀▀▄▄▄█▀
    ''')



def main():
    if args.file:
        file = open(args.file)
        print(file.read())

    if args.pikachu:
        d_pikachu()


if __name__ == '__main__': main()