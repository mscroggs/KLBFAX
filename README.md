# KLBFAX

If you want to add to KLBFAX, the easiest thing is to add files into the pages folder.

Look at the files in that folder for examples.

For a list of current pages, see `PAGES.md`.

## Dependencies
```shell
pip install -r requirements.txt
```

## Running in production
```shell
./run.py
```

## Running in development
```shell
DEVELOP=1 ./run.py
```

## Disable screen blanking
To disable screen blanking, make the command
```shell 
echo -ne "\033[13]" > /dev/tty1
```
run every minute using `cron`.
