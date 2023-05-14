
How to configure Spark with iCloud+ custom domain so that DKIM works

For Spark, when setting up the account:

1. do not chose iCloud as the “account type”. Choose “setup manually”.
2. On the next screen, Select “advanced settings” .
3. For email, use your custom domain email address (it will be [something@yourcustom.domain](mailto:something@yourcustom.domain)) - this **DOES NOT** end in icloud.com.
4. For imap username, use your primary icloud *username*. your primary icloud email always will be of the format [foobar@icloud.com](mailto:foobar@icloud.com) (this **DOES ALWAYS** end in icloud.com); hence your primary icloud username  is “foobar”  (without the icloud.com). 
   1. To clarify, even if you think your icloud id is custom domain (that does not end in icloud.com) - there is an icloud.com id tied to it nonetheless. you can look it up on appleid.apple.com
5. Password is an app-specific password that [you already created](https://support.apple.com/en-us/HT204397).
6. Server, port and security are standard (imap.mail.me.com, 993 and SSL) .
7. For smtp username, its not the same as 4. just to keep things interesting, this time it will be [foobar@icloud.com](mailto:foobar@icloud.com). (With the icloud.com).
8. For smtp password, its same as what you used in step 5 .
9. Server, port and security are smtp.mail.me.com, 587 and STARTTLS respectively Press login.
10. Hurray you have DKIM configured.[](<How to configure Spark with iCloud+ custom domain so that DKIM works

For Spark, when setting up the account:

1. do not chose iCloud as the “account type”. Choose “setup manually”.
2. On the next screen, Select “advanced settings” .
3. For email, use your custom domain email address (it will be [something@yourcustom.domain](mailto:something@yourcustom.domain)) - this **DOES NOT** end in icloud.com.
4. For imap username, use your primary icloud *username*. your primary icloud email always will be of the format [foobar@icloud.com](mailto:foobar@icloud.com) (this **DOES ALWAYS** end in icloud.com); hence your primary icloud username  is “foobar”  (without the icloud.com). 
   1. To clarify, even if you think your icloud id is custom domain (that does not end in icloud.com) - there is an icloud.com id tied to it nonetheless. you can look it up on appleid.apple.com
5. Password is an app-specific password that [you already created](https://support.apple.com/en-us/HT204397).
6. Server, port and security are standard (imap.mail.me.com, 993 and SSL) .
7. For smtp username, its not the same as 4. just to keep things interesting, this time it will be [foobar@icloud.com](mailto:foobar@icloud.com). (With the icloud.com).
8. For smtp password, its same as what you used in step 5 .
9. Server, port and security are smtp.mail.me.com, 587 and STARTTLS respectively Press login.
10. Hurray you have DKIM configured.>)