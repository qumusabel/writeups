## Secure Admin \[40 pts.\]
>This is an introduction to SQL injection. If you don't know what SQLi is, we recommend checking out a tutorial here (https://ctf101.org/web-exploitation/sql-injection/what-is-sql-injection/).
>
>This admin panel seems secure?

![Login form](img/Secure-Admin.png)

First I tried `admin` / `'OR 1=1;--`, but that didn't work.
Then I read the article in the task desc., and there was a simple `'--` payload, and sure enough, `'--` / `'--` worked.
