# DANTE
A helpful desktop virtual assistant that can answer your queries.

![alt text](https://github.com/MilesWJ/DANTE/blob/0406e5f415e7e3b7ae53eae1042db001f4f54e47/DANTE/Assets/DANTE%20Square%20Text%201.png)

# Required Packages
- wolframalpha 5.0.0 —— https://pypi.org/project/wolframalpha/
- PySimpleGUI 4.44.0 —— https://pypi.org/project/PySimpleGUI/
- wikipedia 1.4.0 —— https://pypi.org/project/wikipedia/

# How To Use?
Execute the main.py file, and enter a query into the popup GUI. Take care of your grammar and phrasing, as it uses the exact question you input. Once you enter your question, press ask. Anticipate a 5 to 10 second wait. During this time, the program is sending your question to WolframAlpha and Wikipedia. The program will return a result found from both. If one cannot be found, it will return a "not found" message.

- Step #1: Input your question!
![alt text](https://github.com/MilesWJ/DANTE/blob/780da4759c77e9623a8b1e3e33e5867d471d8389/DANTE/Assets/Use1.png)

- Step #2: Press the "Ask" button!
![alt text](https://github.com/MilesWJ/DANTE/blob/780da4759c77e9623a8b1e3e33e5867d471d8389/DANTE/Assets/Use2.png)

# Additional Notes
You will need to create a WolframAlpha API account. This is an essential step, without it, the program will fail to operate. Once you create your account, set up an personal API account. Use the API key WolframAlpha provides, and insert it into the Client variable.
- WolframAlpha API: https://products.wolframalpha.com/api/
