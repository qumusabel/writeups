## MadVillainy \[45 pts.\]
>An evil villain dubbed the “Triplet Lock” has recently been going around and messing with everyone’s audio files! A detective managed to find out his true identity but Triplet Lock was able to encrypt it before he was caught, can you find out what his true name is?
>
>The flag starts with "Mr." and is case-insensitive.
_files: haveyouheardofthisman.mp3_

Simple challenge. We can open this in Audacity and listen. Sounds like it's reversed. So, we do `Effects > Reverse`. Now we can try to recognize what the voice says. I used Google Translator's voice input for that. It won't recognize the voice right away because the pitch is too low. We can either speed it up or just change the pitch. `Effects > Change Speed` didn't help much, but `Effects > Change Pitch` (150%) made the recording recognizable by the Google Translator.

The flag is `Mr. Hartwell`