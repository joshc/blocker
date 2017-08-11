# blocker
First, you need to make the python and shell scripts executable, if they are not already. To do so, run the following command and insert appropriate file name:

    $ chmod +x [file name]

Then, setup automatic running of cronjobs to block and unblock and specific
times. In the following example, the cronjob to block will run daily at 09:00 until 17:54 every 6 minutes. At 18:00, the cronjob to unblock will run.

    $ env EDITOR=nano crontab -e

This opens up crontab (where cronjobs are installed). Simply running crontab -e
should theoretically open it up in the default editor, but for me, my default
editor didn't work since it was Vim and Vim does something strange when saving
files. Instead, the above command opens it up in nano, another command-line text
editor.

In the file, add the following lines:

    */6 9-18 * * * cd [path to directory] && sudo ./block.sh
    0   18   * * * cd [path to directory] && sudo ./unblock.sh

To save and exit, enter <CTRL>+<O>, then <RETURN>, then <CTRL>+<X>. It should
say something like cronjob installed.

The last thing you need to do is to make sure that the block and unblock files
can be run from a cronjob. Because they edit the /etc/hosts file, you need to
allow the files sudo access. To do so, enter the following command:

    $ sudo visudo

which opens up the file that controls sudo commands in Vim. Move your cursor to
the bottom of the file and enter the following two lines:

    [user] ALL = NOPASSWD: [path to directory]/block.sh
    [user] ALL = NOPASSWD: [path to directory]/unblock.sh

To save and quit, enter <ESC>, then <:wq>.

You're all set! Remember, everything in brackets [] should be replaced by the
corresponding text relevant to your system.


To edit which websites to block, look into block.py and unblock.py. There should
be a list of websites, which include domain.tld. Insert or delete websites that
you would like to block.

Use with caution (make a backup of your hosts file).
