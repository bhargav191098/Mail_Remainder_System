# Mail_Remainder_System
The python code sends a mail to the user if the date in the sql table matches the today's date. So this program must be run everyday. So running them using cron tabs is the best way to do the job. For example to run it everyday at mid night use the following code:
            1. First , if you are comfortable with vim in terminal, use "export EDITOR =vim " to view the cron tabs in vim 
            2.To open a new cron job , enter "crontab - e " in the terminal 
            3. The cron job opens, follow the instructions present inside. For executing every day at mid-night, use "0 0 * * "             4.Once done , press :+ wq , to save and exit.
