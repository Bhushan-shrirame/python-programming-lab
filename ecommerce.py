from easygui import *
import sys
list1 =[]
sum1 = 0
while 1:
    msgbox("namaste")

    msg ="Which site do you prefer?"
    title = "Online Shopping"
    choices = ["Amazon", "Flipkart", "Snapdeal", "Myntra"]
    choice = choicebox(msg, title, choices)

    # note that we convert choice to string, in case
    # the user cancelled the choice, and we got None.
    
    if choice=="Amazon":
      msg="What do you want to buy?"
      title="Shop items"
      choices=["Electronics","Clothing","Furniture"]
      choice = choicebox(msg, title, choices)
      if choice=="Electronics":
          msg="What do you want to buy?"
          title="Shop electronics"
          choices=["Dell","Lenovo","Apple"]
          choice=choicebox(msg, title, choices)
          if choice=="Dell":
            msg1="What is the price of your desired laptop?"
            title1="price"
            choices1=["Dell - 40,000rs\n","Dell - 60,000rs\n","Dell - 1,00,000rs"]
            choice = choicebox(msg1, title1, choices1)
	    list1.append(choice)
          elif choice=="Lenovo":
            msg1="What is the price of your desired laptop?"
            title1="price"
            choices1=["40,000rs","60,000rs","1,00,000rs"]
            choice = choicebox(msg1, title1, choices1)
	    list1.append(choice)
          elif choice=="Apple":
            msg1="What is the price of your desired laptop?"
            title1="price"
            choices1=["40,000rs","60,000rs","1,00,000rs"]
            choice = choicebox(msg1, title1, choices1)
      elif choice=="Clothing":
          msg="What do you want to buy?"
          title="Shop clothing"
          choices=["Forever 21","UCB","Zara"]
          choice=choicebox(msg, title, choices)
          if choice=="Forever 21":
            msg1="What is the price of your desired clothing?"
            title1="price"
            choices1=["400rs","600rs","1000rs"]
            choice = choicebox(msg1, title1, choices1)
          elif choice=="UCB":
            msg1="What is the price of your desired laptop?"
            title1="price"
            choices1=["400rs","6000rs","1000rs"]
          elif choice=="Zara":
            msg1="What is the price of your desired laptop?"
            title1="price"
            choices1=["4000rs","6000rs","1000rs"]          
      elif choice=="Furniture":
          msg="What do you want to buy?"
          title="Shop furniture"
          choices=["Sofa","bed","table"]
          choice=choicebox(msg, title, choices)
          if choice=="Sofa":
            msg1="What is the price of your desired furniture?"
            title1="price"
            choices1=["4000rs","6000rs","10000rs"]
            choice = choicebox(msg1, title1, choices1)
          elif choice=="bed":
            msg1="What is the price of your desired laptop?"
            title1="price"
            choices1=["40000rs","60000rs","10000rs"]
            choice = choicebox(msg1, title1, choices1)
          elif choice=="table":
            msg1="What is the price of your desired laptop?"
            title1="price"
            choices1=["40000rs","60000rs","10000rs"]
            choice = choicebox(msg1, title1, choices1)
    elif choice=="Flipkart":
      msg="What do you want to buy?"
      title="Shop items"
      choices=["Electronics","Clothing","Furniture"]
      choice = choicebox(msg, title, choices)
      if choice=="Electronics":
          msg="What do you want to buy?"
          title="Shop electronics"
          choices=["Dell","Lenovo","Apple"]
          choice=choicebox(msg, title, choices)
          if choice=="Dell":
            msg1="What is the price of your desired laptop?"
            title1="price"
            choices1=["40,000rs","60,000rs","1,00,000rs"]
            choice = choicebox(msg1, title1, choices1)
          elif choice=="Lenovo":
            msg1="What is the price of your desired laptop?"
            title1="price"
            choices1=["40,000rs","60,000rs","1,00,000rs"]
            choice = choicebox(msg1, title1, choices1)
          elif choice=="Apple":
            msg1="What is the price of your desired laptop?"
            title1="price"
            choices1=["40,000rs","60,000rs","1,00,000rs"]
            choice = choicebox(msg1, title1, choices1)
      elif choice=="Clothing":
          msg="What do you want to buy?"
          title="Shop clothing"
          choices=["Forever 21","UCB","Zara"]
          choice=choicebox(msg, title, choices)
          if choice=="Forever 21":
            msg1="What is the price of your desired clothing?"
            title1="price"
            choices1=["400rs","600rs","1000rs"]
            choice = choicebox(msg1, title1, choices1)
          elif choice=="UCB":
            msg1="What is the price of your desired laptop?"
            title1="price"
            choices1=["400rs","6000rs","1000rs"]
            choice = choicebox(msg1, title1, choices1)
          elif choice=="Zara":
            msg1="What is the price of your desired laptop?"
            title1="price"
            choices1=["4000rs","6000rs","1000rs"]
            choice = choicebox(msg1, title1, choices1)
      elif choice=="Furniture":
          msg="What do you want to buy?"
          title="Shop furniture"
          choices=["Sofa","bed","table"]
          choice=choicebox(msg, title, choices)
          if choice=="Sofa":
            msg1="What is the price of your desired furniture?"
            title1="price"
            choices1=["4000rs","6000rs","10000rs"]
            choice = choicebox(msg1, title1, choices1)
          elif choice=="bed":
            msg1="What is the price of your desired laptop?"
            title1="price"
            choices1=["40000rs","60000rs","10000rs"]
            choice = choicebox(msg1, title1, choices1)
          elif choice=="table":
            msg1="What is the price of your desired laptop?"
            title1="price"
            choices1=["40000rs","60000rs","10000rs"]
            choice = choicebox(msg1, title1, choices1)
    elif choice=="Snapdeal":
      msg="What do you want to buy?"
      title="Shop items"
      choices=["Electronics","Clothing","Furniture"]
      choice = choicebox(msg, title, choices)
      if choice=="Electronics":
          msg="What do you want to buy?"
          title="Shop electronics"
          choices=["Dell","Lenovo","Apple"]
          choice=choicebox(msg, title, choices)
          if choice=="Dell":
            msg1="What is the price of your desired laptop?"
            title1="price"
            choices1=["40,000rs","60,000rs","1,00,000rs"]
            choice = choicebox(msg1, title1, choices1)
          elif choice=="Lenovo":
            msg1="What is the price of your desired laptop?"
            title1="price"
            choices1=["40,000rs","60,000rs","1,00,000rs"]
            choice = choicebox(msg1, title1, choices1)
          elif choice=="Apple":
            msg1="What is the price of your desired laptop?"
            title1="price"
            choices1=["40,000rs","60,000rs","1,00,000rs"]
            choice = choicebox(msg1, title1, choices1)
      elif choice=="Clothing":
          msg="What do you want to buy?"
          title="Shop clothing"
          choices=["Forever 21","UCB","Zara"]
          choice=choicebox(msg, title, choices)
          if choice=="Forever 21":
            msg1="What is the price of your desired clothing?"
            title1="price"
            choices1=["400rs","600rs","1000rs"]
            choice = choicebox(msg1, title1, choices1)
          elif choice=="UCB":
            msg1="What is the price of your desired laptop?"
            title1="price"
            choices1=["400rs","6000rs","1000rs"]
            choice = choicebox(msg1, title1, choices1)
          elif choice=="Zara":
            msg1="What is the price of your desired laptop?"
            title1="price"
            choices1=["4000rs","6000rs","1000rs"]
            choice = choicebox(msg1, title1, choices1)
      elif choice=="Furniture":
          msg="What do you want to buy?"
          title="Shop furniture"
          choices=["Sofa","bed","table"]
          choice=choicebox(msg, title, choices)
          if choice=="Sofa":
            msg1="What is the price of your desired furniture?"
            title1="price"
            choices1=["4000rs","6000rs","10000rs"]
            choice = choicebox(msg1, title1, choices1)
          elif choice=="bed":
            msg1="What is the price of your desired laptop?"
            title1="price"
            choices1=["40000rs","60000rs","10000rs"]
            choice = choicebox(msg1, title1, choices1)
          elif choice=="table":
            msg1="What is the price of your desired laptop?"
            title1="price"
            choices1=["40000rs","60000rs","10000rs"]
            choice = choicebox(msg1, title1, choices1)
    elif choice=="Myntra":
      msg="What do you want to buy?"
      title="Shop items"
      choices=["Electronics","Clothing","Furniture"]
      choice = choicebox(msg, title, choices)
      if choice=="Electronics":
          msg="What do you want to buy?"
          title="Shop electronics"
          choices=["Dell","Lenovo","Apple"]
          choice=choicebox(msg, title, choices)
          if choice=="Dell":
            msg1="What is the price of your desired laptop?"
            title1="price"
            choices1=["40,000rs","60,000rs","1,00,000rs"]
            choice = choicebox(msg1, title1, choices1)
          elif choice=="Lenovo":
            msg1="What is the price of your desired laptop?"
            title1="price"
            choices1=["40,000rs","60,000rs","1,00,000rs"]
            choice = choicebox(msg1, title1, choices1)
          elif choice=="Apple":
            msg1="What is the price of your desired laptop?"
            title1="price"
            choices1=["40,000rs","60,000rs","1,00,000rs"]
            choice = choicebox(msg1, title1, choices1)
      elif choice=="Clothing":
          msg="What do you want to buy?"
          title="Shop clothing"
          choices=["Forever 21","UCB","Zara"]
          choice=choicebox(msg, title, choices)
          if choice=="Forever 21":
            msg1="What is the price of your desired clothing?"
            title1="price"
            choices1=["400rs","600rs","1000rs"]
            choice = choicebox(msg1, title1, choices1)
          elif choice=="UCB":
            msg1="What is the price of your desired laptop?"
            title1="price"
            choices1=["400rs","6000rs","1000rs"]
            choice = choicebox(msg1, title1, choices1)
          elif choice=="Zara":
            msg1="What is the price of your desired laptop?"
            title1="price"
            choices1=["4000rs","6000rs","1000rs"]
            choice = choicebox(msg1, title1, choices1)
      elif choice=="Furniture":
          msg="What do you want to buy?"
          title="Shop furniture"
          choices=["Sofa","bed","table"]
          choice=choicebox(msg, title, choices)
          if choice=="Sofa":
            msg1="What is the price of your desired furniture?"
            title1="price"
            choices1=["4000rs","6000rs","10000rs"]
            choice = choicebox(msg1, title1, choices1)
          elif choice=="bed":
            msg1="What is the price of your desired laptop?"
            title1="price"
            choices1=["40000rs","60000rs","10000rs"]
            choice = choicebox(msg1, title1, choices1)
          elif choice=="table":
            msg1="What is the price of your desired laptop?"
            title1="price"
            choices1=["40000rs","60000rs","10000rs"]
            choice = choicebox(msg1, title1, choices1)


    if ccbox(msg, title):     # show a Continue/Cancel dialog
        pass  # user chose Continue
    else:
	textbox('Purchase Memo','Bill Desk',text = list1)
sys.exit(0)
