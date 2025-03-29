# 3x3 틱택토 보드 초기화
board = [[' ' for _ in range(3)] for _ in range(3)]

def print_board():
    """게임 보드를 출력하는 함수"""
    for r in range(3):
        print(f" {board[r][0]} | {board[r][1]} | {board[r][2]} ")
        if r < 2:
            print("---|---|---")

def check_winner(player):
    """플레이어가 승리했는지 검사하는 함수"""
    for i in range(3):
        # 가로 또는 세로 검사
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    # 대각선 검사
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full():
    """보드가 꽉 찼는지 확인하는 함수"""
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

while True:
    print_board()

    # 사용자 입력 받기
    while True:
        try:
            x = int(input("다음 수의 x 좌표를 입력하시오 (0~2): "))
            y = int(input("다음 수의 y 좌표를 입력하시오 (0~2): "))
            if 0 <= x < 3 and 0 <= y < 3 and board[x][y] == ' ':
                break
            else:
                print("잘못된 위치입니다. 다시 입력하세요.")
        except ValueError:
            print("숫자를 입력하세요!")

    board[x][y] = 'X'

    # 사용자가 이겼는지 확인
    if check_winner('X'):
        print_board()
        print("사용자가 승리했습니다!")
        break

    # 무승부 체크
    if is_full():
        print_board()
        print("무승부입니다!")
        break

    # 컴퓨터 차례 (첫 번째 빈칸 찾기)
    done = False
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                done = True
                break
        if done:
            break

    # 컴퓨터가 이겼는지 확인
    if check_winner('O'):
        print_board()
        print("컴퓨터가 승리했습니다!")
        break

    # 무승부 체크
    if is_full():
        print_board()
        print("무승부입니다!")
        break