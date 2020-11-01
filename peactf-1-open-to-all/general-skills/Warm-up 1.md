## Warm-up 1 \[15 pts.\]
>Log into the ssh service with username peactf and password peactf2020.
>
>Hmm... how to I search for a string recursively on Linux?

SSH into the machine, then run

`grep -Rn "peaCTF" warm-up-1`

which gives us the flag:

`peaCTF{3f50bb70-5e42-45c2-9cb3-52dbcf26de20}`