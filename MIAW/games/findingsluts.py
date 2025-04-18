import random
import MIAW.tools.main as main

def start():
      while True :
            box_shapes = " [   ] "
            empty_boxes = [box_shapes] * 4
            
            bitch = random.randint(1, 4)
            
            output_empty_boxes = "".join(empty_boxes)
            boxes = empty_boxes.copy()
            boxes[bitch - 1] = " [💋 ] "

            output = "".join(boxes)

            print(f"eiyo nigga, which box is the hottest girl in this brothel hiding, if you're right she's yours👇\n\n{output_empty_boxes}\n")

            userchoice = int(input ("BOX [1 / 2 / 3 / 4] ?  :"))

            if userchoice == bitch:
                  print(f"{output}\n you're right, having fun with her")
            else:
                  print(f"wrong👎! that bitch in the box {bitch}\n {output}")
                  
            play_again = input("\n\n wanna do it again? [yes/no]: ")
            if play_again == "no":
                  print("okay game over, fvck off pussy")
                  main.menu()

if __name__=='__main__':
       start()
