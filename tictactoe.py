class tictactoe():
        print("Tic Tac Toe Game")
        print("written by: Nik Nak")
        print("have Fun! \U0001f600")
        print(40 * '=')
        print('\n')
current_player = 'X'
                        
field = [" ",
        "1","2","3",
        "4","5","6",
        "7","8","9"]

def gamefield():
        print ( field[1] + "|" + field[2] + "|" + field[3] )
        print ( field[4] + "|" + field[5] + "|" + field[6] )
        print ( field[7] + "|" + field[8] + "|" + field[9] )


def playerinput():       
        while(True):
                
                inputplayer = input("Choose a Field:")               
                inputplayer = int(inputplayer) 
                field[inputplayer] = current_player
                                
                
                
                
                if 0 <= inputplayer <= 9:   
                        break
  
                print("the number is too high, you idiot")
                                                  
                  
                                 
def control_win():
          
                if field[1] == field[2] == field[3]:
                        return field[1]
        
                if field[4] == field[5] == field[6]:
                        return field[4]
        
                if field[7] == field[8] == field[9]:
                        return field[7]
    
                if field[1] == field[3] == field[7]:
                        return field[1]
    
                if field[2] == field[5] == field[8]:
                        return field[2]
    
                if field[3] == field[6] == field[9]:
                        return field[3]
                
                if field[1] == field[4] == field[7]:
                        return field[1]
                
                if field[1] == field[5] == field[9]:
                        return field[1]
    
                if field[3] == field[5] == field[7]:
                        return field[3]
    
def control_draw():
        
                if (field[1] == 'X' or field[1] == 'O')\
                and (field[2] == 'X' or field[2] == 'O')\
                and (field[3] == 'X' or field[3] == 'O')\
                and (field[4] == 'X' or field[4] == 'O')\
                and (field[5] == 'X' or field[5] == 'O')\
                and (field[6] == 'X' or field[6] == 'O')\
                and (field[7] == 'X' or field[7] == 'O')\
                and (field[8] == 'X' or field[8] == 'O')\
                and (field[9] == 'X' or field[9] == 'O'):
      
                        return("Draw")
      
                            

while(True):
        if(playerinput):
                
                print(f"Player {current_player} it's your turn !")
                gamefield() 
                playerinput()
                
                
                if current_player == 'X':
                        current_player = 'O'
                else:
                        current_player = 'X'  
                         
                
        if control_win():
                print("You won !!!")
                break
                
        if control_draw():
                print("Draw!")
                break

