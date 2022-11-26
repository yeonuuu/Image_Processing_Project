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

If you have allowed your GPU inside docker, just build the container

```
docker-compose build --no-cache
```

and launch it, it will by default try to open the file named 'test.png' at root.

```
docker-compose up
```
