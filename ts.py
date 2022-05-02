import argparse
import time


def _parse(v):
    print(int(time.mktime(time.strptime(v, "%Y-%m-%d %H:%M:%S"))))


def _format(v):
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(v)))


def _now():
    now = time.time()
    print(int(now))
    print(int(now * 1000))
    print(int(now * 1000000))
    _format(now)


if __name__ == '__main__':
    HELP = "ts [-h] [-p PARSE] [-f FORMAT] [-n]"
    parser = argparse.ArgumentParser(description='时间戳与时间字符串转换工具')
    parser.add_argument(
        '-p', '--parse',
        help='parse formated str to timestamp',
        metavar='FORMATED_STR',
        nargs=1,
        required=False)
    parser.add_argument(
        '-f', '--format',
        help='format timestamp to str',
        metavar='TIMESTAMP',
        nargs=1,
        required=False)
    parser.add_argument(
        '-n',
        '--now',
        help='get now info',
        action='store_true',
        required=False)

    args = parser.parse_args()
    # print(args)

    if args.now is True:
        _now()
    elif args.parse is not None:
        _parse(args.parse[0])
    elif args.format is not None:
        _format(int(args.format[0]) / 1000 if len(args.format[0]) == 13 else int(args.format[0]))
    else:
        print(parser.format_help())
