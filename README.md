# Easypass 🍤

## About Easypass
- Easypass is a module made with python that automates the process of getting the LAUSD [Dailypass](https://pap.lausd.net/en-US/).
- This module uses other few modules to interact with the [Dailypass](https://pap.lausd.net/en-US/) website, it uses modules such as [selenium](https://pypi.org/project/selenium/) and [email](https://docs.python.org/3/library/email.html).
- The code is completely open-sourced and I give you complete permission to take the code and figure out how it works or make it better.

## Requirements
- Alternate Gmail Account
- [Github](https://github.com/) Account
- [Replit](https://replit.com/) Account
- [UptimeRobot](https://uptimerobot.com/) Account
- A phone number where you can receive your dailypass

## Is this allowed?
- Yes this is very much allowed, The browser is automated, and google chrome flags it as automated, and the [Dailypass](https://pap.lausd.net/en-US/)  doesn't do anything to avoid automated browsers so it's totally safe to use this.

## How to use it
1. I'm going to assume that you already have an alternate Gmail account, [Github](https://github.com/), [Replit](https://replit.com/) and [UptimeRobot](https://uptimerobot.com/)  setup already. If you are unaware of how to do so, here are some videos that will help you out. 
	- [Gmail Account Creation Video](https://www.youtube.com/watch?v=Q9Z1Os3jLOU)
	- [Github Account Creation Video](https://www.youtube.com/watch?v=-Di-ZfcBDXU)
	- [Replit Account Creation Video](https://www.youtube.com/watch?v=EnTcdgyan0o)
	- [UptimeRobot Account Creation Link](https://uptimerobot.com/signUp)
2. Now that you have all your accounts set up first we will need to set up 2-Step on your Gmail account. Here is a detailed video on how to do so.
	- [Stepup 2-Step](https://www.youtube.com/watch?v=jJKWDDj1Wgw)
3. Now we will have to create an app password that Google will allow you to login with on your bot. To do so go to [App passwords in the security tab or the manage page of your account or click on this link.](http://myaccount.google.com/apppasswords)
	- You should see something like this:![](https://github.com/workframes/Easypass-Replit/blob/main/Images/app_password_v1.png?raw=true)
	- For `Select app` choose the option as `Other(Custom name)`. 
	- For the textbox put in `PC` . ![](https://github.com/workframes/Easypass-Replit/blob/main/Images/app_password_v2.png?raw=true)
	-  Then proceed to click `GENERATE`, this will generate a password. Please save this password on a notepad as you will use this later on. ![](https://github.com/workframes/Easypass-Replit/blob/main/Images/app_password_v3.png?raw=true)
4. Now you are going to want to go to the Github repository of [Easypass](https://github.com/workframes/Easypass-Replit). At the top right corner there is going to be a button called `Fork`, click it to clone the repository.
	- ![](https://github.com/workframes/Easypass-Replit/blob/main/Images/github_fork_v1.png?raw=true)
5. Now that you have everything clone, go on to your replit dashboard. 
	- Click create to the `+` icon under `Create` to create a new replit. ![](https://github.com/workframes/Easypass-Replit/blob/main/Images/create_replit_v1.png?raw=true)
	- Select the language as `Python`
	- Set a title to your project
	- Now click `Import from github`, If you haven't connected your github account to your replit account you will have an option to do so.
	- Set the `GitHub URL` as `[YOUR-GITHUB-USERNAME]/Easypass-Replit`
	- Now go on and click `+ Import from GitHub` ![](https://github.com/workframes/Easypass-Replit/blob/main/Images/import_github_v1.png?raw=true)
6. If you did everything correctly you should be redirected to edit your replit project.
	- At the bottom right of your screen you should see a tab, with information, on that tab click `Shell` ![](https://github.com/workframes/Easypass-Replit/blob/main/Images/edit_replit_v1.png?raw=true)
	- Now go and type `pip install flask selenium schedule`![](https://github.com/workframes/Easypass-Replit/blob/main/Images/install_dep_v1.png?raw=true)
	-  Click `Enter` on your keyboard and you will see some magic happening!
	-  After everything has run switch the tab to `Console`
7. Now we get to some coding, Using the tab on your left double click on the file that says `main.py`![](https://github.com/workframes/Easypass-Replit/blob/main/Images/switch_file_v1.png?raw=true)
8. The file should look something like this ![](https://github.com/workframes/Easypass-Replit/blob/main/Images/example_file_v1.png?raw=true)
9. Now we are going to replace the placeholder information with yours.
	- For `BOT_EMAIL` replace it with the email to your alternate Gmail account.
	- For `BOT_PASSWORD` replace it with the auto-generated password we got earlier.
	- For `LAUSD_EMAIL` replace it with your `@mymail.lausd.net` email.
	- For `LAUSD_PASSWORD` replace it with your password to your `@mymail.lausd.net` email.
10. Now for the `MMS_PHONE_NUMBER` field, this will depend on your phone provider, Read the chart below to figure your MMS number. 

	| | Provider | Extenstion | 
	| -------       | ---  | 
	| | AT&T | @mms.att.net |
	| | Boost Mobile | @myboostmobile.com |
	| | Cricket Wireless | @mms.cricketwireless.net |
	| | Google Project Fi | @msg.fi.google.com |
	| | Metro PCS | @mymetropcs.com |
	| | Page Plus | @mypixmessages.com |
	| | Sprint | @pm.sprint.com |
	| | Straight Talk | @mypixmessages.com |
	| | T-Mobile | @tmomail.net |
	| | Tracfone | @mmst5.tracfone.com |
	| | U.S. Cellular | @mms.uscc.net |
	| | Verizon| @vzwpix.com |
	| | Virgin Mobile | @vmpix.com |
	| | Xfinity Mobile | @mypixmessages.com |
	
	- Now that you found your extension format it with your number first ending with your extension, for example `7472960595@tmomail.net`
11. Now the files  `Images`, `README.md` from the tab to your left. To delete just click the file and right then click `Delete`
12. Open the `.replit` file and edit it to this `run="python3 main.py`
13. Now click the green button that says `▶Run`
14. A new window should have popped up, It should include a link, an example of the link `https://Easypass-Replit.workframes.repl.co` ![](https://github.com/workframes/Easypass-Replit/blob/main/Images/get_linke_v1.png?raw=true)
15. Now we move on to your [UptimeRobot dashboard](https://uptimerobot.com/dashboard.php)
	- First, log in with your credentials if you haven't already.
	- Click `+ Add New Monitor`
	- Set `Monitor Type` as `HTTP(s)`
	- Set `URL(or IP)` as the link you copied earlier
	- Set `Monitoring Interval` as every 30 minutes
	- Set `Friendly Name` as any name you wish to call it
	-  Here is what it should look like when it's done ![](https://github.com/workframes/Easypass-Replit/blob/main/Images/example_monitor_v1.png?raw=true)
	- Scroll down and check your email as true for contact, they will email you if your bot does go down. ![](https://github.com/workframes/Easypass-Replit/blob/main/Images/example_monitor_v2.png?raw=true)
	- Scroll down and click `Create Monitor`

# Tips
- For the first few hours I would keep an eye on the monitor to see if the bot does go down.
- Make sure all the information you provided the bot is accurate.

# Conclusion
- Enjoy the bot!
- If you do need help with setting up the bot, join my discord server at [shrmp.io](http://shrmp.io/) or add my discord `frames#4888`

	
