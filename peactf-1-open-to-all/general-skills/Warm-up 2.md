## Warm-up 2 \[30 pts.\]

>Log into the ssh service with username peactf and password peactf2020.
>
>Hmm... how to I search for a string recursively on Linux?

Once again, we ssh into the machine


```
peactf@b1141ba8db02:~$ ls
readme.txt  warm-up-2
peactf@b1141ba8db02:~$ cat readme.txt
A legit flag is in the format of peaCTF{}
```
Ok, now we try to `grep -Rn "peaCTF" warm-up-2`, which produces a ton of output with fake flags. They don't match the format because they don't end with `}`. So, let's try to `grep -Rn "}" warm-up-2`

And now it finds just one file with a legit flag in it (still a lot of fake flags, but thanks to grep for highlighting `}`!)

`peaCTF{27137da9-b3d4-4628-a669-5a3cf8bc47a9}`