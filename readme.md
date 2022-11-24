# How to use outside docker


## Training

```
python ./src/main.py --train
```

## Emotion detection

```
python ./src/main.py [filepath]
```

# How to use inside docker

Not working because cuda using GPU into docker and docker does not allow using GPU if you don't configure it for it.





UPDATE FILTERS:

[OK] Angry
[KO] Fear
[OK] Happy
[KO] Neutral
[KO] Sad
[KO] Surprise