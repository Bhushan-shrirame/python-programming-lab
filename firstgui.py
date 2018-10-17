from easygui import *
import sys
while 1:
    msgbox("welcome")
    msg ="from where you want to buy"
    title = "top shopping website"
    choices = ["flipkart", "amazon", "ebay"]
    choice = choicebox(msg, title, choices)
    if choices== flipkart:
      msg="shop by category"
      choices1=["shirts","jeans","t-shrirts"]
      choice = choicebox(msg, choices)
      msgbox("You chose: " + str(choice), "cart")
      msg = "Do you want to continue?"
      title = "Please Confirm"
    elif choices== amazon:
      msg="shop by category" 
      choices1=["shirts","jeans","t-shrirts"]
      choice = choicebox(msg,  choices)
      msgbox("You chose: " + str(choice), "cart")
      msg = "Do you want to continue?"
      title = "Please Confirm"
    if choices== ebay:
      msg="shop by category" 
      choices1=["shirts","jeans","t-shrirts"]
      choice = choicebox(msg, choices)
      msgbox("You chose: " + str(choice), "cart")
      msg = "Do you want to continue?"
      title = "Please Confirm"

    # note that we convert choice to string, in case
    # the user cancelled the choice, and we got None.
    msgbox("You chose: " + str(choice), "cart")

    msg = "Do you want to continue?"
    title = "Please Confirm"
    if ccbox(msg, title):     # show a Continue/Cancel dialog
        pass  # user chose Continue
    else:
        sys.exit(0)


