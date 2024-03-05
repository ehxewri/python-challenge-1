# Python Challenge 1 - The journey begins
Code is in M2_My_Code

**This needs my_menu.json in the same dir as menu.py**
```
To run this please clone the repo
      python menu.py
      my_menu.json   **this needs my_menu.json in the same dir as menu.py**


      The program will output a file called my_order.json. 
      I want to play around with saving the orders so we can pull them back up if needed
      i used.gitignore to keep this file out of the github repo. It changes everytime i run the code and I did want to have to deal with that file changing
```


I'm using this command so it has to be run

    script_dir = (Path(__file__).resolve()).parent
    
This lets you run menu.py from any directory and it still finds my_menu.json as long as it is is the same dir as menu.py

The following modules are imported to help make the output cleaner and keep the lenght shorter

        import locale
        
        import json
        
        from pathlib import Path

Additional modules i am playing with but not part of the assignment are

  OrderPrintFunction.py - new order print function work in progress
  
  loadmenu.py           - reset of first real lab Was used to develop the import on the menu from JSON
  
  makemenu.py           - Creates the Json file to load in. this was another. 
