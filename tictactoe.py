import tkinter

def set_title(row,column):
    global curr_player
    if (game_over):
        return

    if board[row][column]['text']!='':
        return
    
    board[row][column]['text']=curr_player
    if curr_player==playerO:
        curr_player=playerX
    else:
        curr_player=playerO

    label['text']=curr_player+"'s turn"
    check_winner()

def check_winner():
    global turns, game_over
    turns+=1

    for row in range(3):
        if (board[row][0]['text']==board[row][1]['text']==board[row][2]['text'] and board[row][0]['text']!=''):
            label.config(text=board[row][0]['text']+"'s winner!" , foreground=cyellow)
            for column in range(3):
                board[row][column].config(foreground=cyellow , background=clightgray )
            game_over=True
            return
        
        for column in range(3):
            if (board[0][column]['text']==board[1][column]['text']==board[2][column]['text'] and board[0][column]['text']!=''):
                label.config(text=board[0][column]['text']+"'s winner!" , foreground=cyellow)
                for row in range(3):
                    board[row][column].config(foreground=cyellow , background=clightgray )
                game_over=True
                return
            
        if (board[0][0]['text']==board[1][1]['text']==board[2][2]['text'] and board[0][0]['text']!=''):
            label.config(text=board[0][0]['text']+"'s winner!" , foreground=cyellow)
            for i in range(3):
                board[i][i].config(foreground=cyellow , background=clightgray )
            game_over=True
            return

        if (board[0][2]['text']==board[1][1]['text']==board[2][0]['text'] and board[0][2]['text']!=''):
            label.config(text=board[0][2]['text']+"'s winner!" , foreground=cyellow)
            board[0][2].config(foreground=cyellow , background=clightgray )
            board[1][1].config(foreground=cyellow , background=clightgray )
            board[2][0].config(foreground=cyellow , background=clightgray )
            game_over=True
            return

    if turns==9:
        game_over=True
        label.config(text='Tie!', foreground=cyellow)

def new_game():
    global turns,game_over
    turns=0
    game_over=False

    label.config(text=curr_player+"'s turn", foreground='white')
    for row in range(3):
        for column in range(3):
            board[row][column].config(text='' , foreground=cblue, background=cgray)


playerX='X'
playerO='O'
curr_player=playerX
board=[[0 , 0 , 0 ],
       [0 , 0 , 0 ],
       [0 , 0 , 0 ]]
cblue="#0b73c8"
cyellow="#e2b80f"
cgray='#343434'
clightgray='#646464'
turns=0
game_over=False

window=tkinter.Tk()
window.title('TIC TAC TOE')
window.resizable(False,False)

frame=tkinter.Frame(window)
label=tkinter.Label(frame, text=curr_player+"'s turn", font=('Consolas',20), background=cgray,foreground='white')
label.grid(row=0,column=0,columnspan=3,sticky='we')


for row in range(3):
    for column in range(3):
        board[row][column]=tkinter.Button(frame,text='' , font=('Consolas',50,'bold'), background=cgray , foreground=cblue , width=4 , height=1,
                                            command=lambda row=row , column=column: set_title(row,column))

        board[row][column].grid(row=row+1,column=column)

button=tkinter.Button(frame , text='Restart', font=('Consolas',20,), background=cgray, foreground='white',command=new_game)
button.grid(row=4,column=0,columnspan=3,sticky='we')

frame.pack()

window.update()
window_width=window.winfo_width()
window_height=window.winfo_height()
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()

window_x=int((screen_width/2)-(window_width/2))
window_y=int((screen_height/2)-(window_height/2))

window.geometry(f'{window_width}x{window_height}+{window_x}+{window_y}')

window.mainloop()