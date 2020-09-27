board=" "*9
moves = list(board)
#print(moves)
default = [['1', '1'], ['1', '2'], ['1', '3'],
           ['2', '1'], ['2', '2'], ['2', '3'],
           ['3', '1'], ['3', '2'], ['3', '3']]
choice = []
print("---------")
print("| " + " ".join(moves[:3]) + " |")
print("| " + " ".join(moves[3:6]) + " |")
print("| " + " ".join(moves[6:]) + " |")
print("---------")

def current_board():
    turn = input("Input your coordinates: ").split()
    if turn in default:
        location = default.index(turn)
        if moves[location] != ' ':
            print("This cell is occupied! Choose another one!")
            return current_board()
        else:
            choice.append(turn)
            if i%2==0:
                moves[location] = 'X'
            else:
                moves[location] = 'O'
            return moves
    else:
        try:
            if all(int(x) for x in turn):
                print("Coordinates should be from 1 to 3!")
                return current_board()
        except ValueError:
                print("You should enter numbers!")
                return current_board()
li,li_n=[],[]
win_lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [6, 4, 2]]
for i in range(9):
    current_board()
    print("---------")
    print("| " + " ".join(moves[:3]) + " |")
    print("| " + " ".join(moves[3:6]) + " |")
    print("| " + " ".join(moves[6:]) + " |")
    print("---------")
    s=[]
    # print(moves.count(" "))
    if moves.count(" ")<4:
        for j,k in enumerate(moves):
            if k=='X':
                li.append(j)
            if k=='O':
                li_n.append(j)
        for i in win_lines:
            if set(i).issubset(set(li)):
                s.append("X wins")
                break
            if set(i).issubset(set(li_n)):
                s.append("O wins")
                break
            else:
                if moves.count(" ")==0:
                    s.append("Draw")
        if len(s)>=1 and s[0]=="X wins":
            print(s[0])
            break
        if len(s)>=1 and s[0]=="O wins":
            print(s[0])
            break
        if len(s)>1:
            print(s[len(s)-1])