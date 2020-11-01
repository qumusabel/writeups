## Warm-up 0 \[10 pts.\]

>These are a series of introductory problems on basic Linux skills.
>
>Log into the ssh service with username peactf and password peactf2020. What's on the server?

Simple challenge, once we are connected we can
```sh
grep -Rn "{" warm-up-1
```

Which shows a lot of files with the same correct flag in it.
