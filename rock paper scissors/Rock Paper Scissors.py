from tkinter import *
from tkinter import Toplevel
import random
from PIL import Image, ImageTk
def game():
    root=Tk()
    root.title("Rock Paper Scissors")
    root.geometry("500x430+225+100")
    root.config(bg='#1F1F3D')
    root.resizable(False,False)
    root.iconbitmap("image/rock-paper-scissors.ico")
    root.focus_set()

    root2 = None
    user=""

    def Exit():
        root.destroy()

    def Start():
        root.destroy()
        root1=Tk()
        root1.title("Rock Paper Scissors")
        root1.geometry("615x430+190+100")
        root1.config(bg='#1F1F3D')
        root1.resizable(False,False)
        root1.iconbitmap("image/rock-paper-scissors.ico")
        root1.focus_set()
        
        img_rock = ImageTk.PhotoImage(
            Image.open("image/rock.png")
            )
        img_paper = ImageTk.PhotoImage(
            Image.open("image/paper.png")
            )
        img_scissors = ImageTk.PhotoImage(
            Image.open("image/scissors.png"))
        
        def Enter_a_paper():
            global user
            user="paper"
            End_play()
            
            
        def Enter_a_scissors():
            global user
            user="scissors"
            End_play()
            
        def Enter_a_rock():
            global user
            user="rock"
            End_play()        
        
        
        def End_play():
        
            choose = ["rock","paper","scissors"]
            #CPU = random.choice(choose)
            CPU = "rock"
            print(user)
            
            root1.destroy()
            root3=Tk()
            root3.title("Rock Paper Scissors")
            root3.geometry("615x430+190+100")
            root3.config(bg='#1F1F3D')
            root3.resizable(False,False)
            root3.iconbitmap("image/rock-paper-scissors.ico")
            root3.focus_set()

            imge_rock = PhotoImage(file="image/rock.png")
        
            imge_paper = PhotoImage(file="image/paper.png")
            
            imge_scissors = PhotoImage(file="image/scissors.png")
      ########### label _ user######      
            lab_paper_user = Label(
                root3,
                image=imge_paper,
                width=190,
                height=170,
                bg='#F0F8FF'
                )
            lab_scissors_user = Label(
                root3,
                image=imge_scissors,
                width=190,
                height=170,
                bg='#F0F8FF'  
                )
            lab_rock_user = Label(
                root3,
                image=imge_rock,
                width=190,
                height=170,
                bg='#F0F8FF')
        ########### label _ user######
            lab_paper_CPU = Label(
                root3,
                image=imge_paper,
                width=190,
                height=170,
                bg='#F0F8FF'
                )
            lab_scissors_CPU = Label(
                root3,
                image=imge_scissors,
                width=190,
                height=170,
                bg='#F0F8FF'  
                )
            lab_rock_CPU = Label(
                root3,
                image=imge_rock,
                width=190,
                height=170,
                bg='#F0F8FF')


        #### CPU (if)############
            if CPU == "rock":
                lab_rock_CPU.place(x=30,y=30)
                
            if CPU == "paper":
                lab_paper_CPU.place(x=30,y=30)
                
            if CPU == "scissors":
                lab_scissors_CPU.place(x=30,y=30)
                
        #### user (if)###########
            if user == "rock":
                lab_rock_user.place(x=395,y=30)
                
            if user == "paper":
                lab_paper_user.place(x=395,y=30)
                
            if user == "scissors":
                lab_scissors_user.place(x=395,y=30)
            
            
            lab_vs = Label(
                root3,
                text="vs",
                bg="#1F1F3D",
                fg="#FFD700",
                font=("Impact",60),
                )
            lab_vs.place(x=270,y=60)
            
            lab_CPU = Label(
                root3,
                text=" CPU ",
                bg="#1F1F3D",
                fg=" #FF6B6B",
                font=("Impact",25)
                )
            lab_CPU.place(x=85,y=210)
            
            lab_you = Label(
                root3,
                text=" YOU ",
                bg="#1F1F3D",
                fg="#32CD32",
                font=("Impact",25)
                )
            lab_you.place(x=460,y=210)        
            if user=="paper" and CPU=="rock" or user=="rock" and CPU=="scissors" or user=="scissors" and CPU=="paper" :
                lab_win = Label(
                    root3,
                    text=" YOU WIN ",
                    bg="#1F1F3D",
                    fg="#32CD32",
                    font=("Impact",25)
                    )
                lab_win.place(x=245,y=220)

            if user=="paper" and CPU=="scissors" or user=="rock" and CPU=="paper" or user=="scissors" and CPU=="rock" :
                lab_lose = Label(
                    root3,
                    text=" YOU LOSE ",
                    bg="#1F1F3D",
                    fg="#FF6B6B",
                    font=("Impact",25)
                    )
                lab_lose.place(x=245,y=220)
            
            
            if user=="paper" and CPU=="paper" or user=="rock" and CPU=="rock" or user=="scissors" and CPU=="scissors" :
                lab_tow_equals = Label(
                    root3,
                    text=" TOW EQUALS ",
                    bg="#1F1F3D",
                    fg="#FFD700",
                    font=("Impact",25)
                    )
                lab_tow_equals.place(x=220,y=220)
            
            def Continuation():
                Start()
                #root3.destroy()
                
            
            def menu():
                root3.destroy()
                game()
            def Exit1():
                root3.destroy()
            
            continuation = Button(root3,
                   text=" Continuation ",
                   width=15,
                   height=1,
                   bg="#32CD32",
                   fg="#000000",
                   font=("Impact", 15),
                   command=Continuation
                   )
            continuation.place(x=230,y=285)


            button_menu = Button(root3,
                   text=" MENU ",
                   width=15,
                   height=1,
                   bg="#87CEEB",
                   fg="#FFFFFF",
                   font=("Impact", 15),
                   command=menu
                   )
            button_menu.place(x=140,y=335)
            
            button_exit = Button(root3,
                         text=" Exit ",
                         width=15,
                         height=1,
                         bg="#87CEEB",
                         fg="#FFFFFF",
                         font=("Impact", 15),
                         command=Exit1
                         )
            button_exit.place(x=320,y=335)
            
            root3.mainloop()
        

        
        button_paper = Button(
            root1,
            image=img_paper,
            width=190,
            height=170,
            activebackground="#FFE873",
            bg='#F0F8FF',
            command=Enter_a_paper
            )
        button_paper.place(x=10,y=30)

        button_scissors = Button(
            root1,
            image=img_scissors,
            width=190,
            height=170,
            activebackground="#FFE873",
            bg='#F0F8FF',
            command=Enter_a_scissors
            )
            
        button_scissors.place(x=210,y=30)
        
        button_rock = Button(
            root1,
            image=img_rock,
            width=190,
            height=170,
            activebackground="#FFE873",
            bg='#F0F8FF',
            command=Enter_a_rock
            )
        button_rock.place(x=410,y=30)
        

        lab_choose = Label(
            root1,
            text=" Choose yuor move .... ",
            bg="#1F1F3D",
            fg="#FFFFFF",
            font=("Impact",30)
            )
        lab_choose.place(x=120,y=260)
        
        
        
        
        root1.mainloop()


    def How_to_play(event=None):
        global root2
        
        if root2 is not None :
            root2.destroy() 
        root2 = Toplevel()
        root2.title("Rock Paper Scissors")
        root2.geometry("500x430+225+100")
        root2.config(bg='#1F1F3D')
        root2.resizable(False,False)
        root2.iconbitmap("image/rock-paper-scissors.ico")
        root2.focus_set()
        
        
        root2.mainloop()


        


    lab_rock_paper_scissors = Label(root,
                                    text=" Rock Paper Scissors ",
                                    fg="#FFD700",bg='#1F1F3D',
                                    font=("Impact", 40)
                                    )
    lab_rock_paper_scissors.place(x=20,y=20)

    how_to_play = Button(root,
                         text=" How To Play ",
                         width=15,height=1,
                         bg="#87CEEB",
                         fg="#FFFFFF",
                         font=("Impact", 15),
                         command=How_to_play
                         )
    how_to_play.place(x=178,y=230)

    button_exit = Button(root,
                         text=" Exit ",
                         width=15,
                         height=1,
                         bg="#87CEEB",
                         fg="#FFFFFF",
                         font=("Impact", 15),
                         command=Exit
                         )
    button_exit.place(x=178,y=295)
     
    start = Button(root,
                   text=" Start Game ",
                   width=20,
                   height=2,
                   bg="#32CD32",
                   fg="#000000",
                   font=("Impact", 15),
                   command=Start
                   )
    start.place(x=150,y=140)

    root.mainloop()
game()
