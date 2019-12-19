def printboard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    return

#改变下一次打印的信息
def switch(trun_tmp):
    if trun_tmp == 'x':
        trun_tmp = 'o'
    else:
        trun_tmp = 'x'
    return trun_tmp

def main():
    board = {
        '1': ' ', '2': ' ', '3': ' ',
        '4': ' ', '5': ' ', '6': ' ',
        '7': ' ', '8': ' ', '9': ' ',
    }
    printboard(board)
    board_use = board.copy()
    count = 0
    turn = 'x'
    begin = True
    print('x先手，o后手')
    while begin:
        begin = False
        while count < 9:
            move = input('轮到%s,请输入对应棋盘对应序号:' % turn)
            #输入棋子信息
            if board_use[move] == ' ':
                board_use[move] = turn
            else:
                print('输入错误，请重新输入')
                continue
            printboard(board_use)
            # 改变下一次出手信息
            turn = switch(turn)
            count += 1
        choice = input('再玩一局?(yes|no)')
        begin = choice == 'yes'


if __name__ == '__main__':
    main()