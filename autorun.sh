function update {
    where=`pwd`
    cd /home/pi/ceefax
    python update.py
    cd "$where"
}

export KLBFILE="/home/pi/.klb/KLBFAX_status"

if $(ps aux | grep "./run.py" | grep -v "grep" > /dev/null); then
    echo "KLBFAX running already."
    run_kl="0"
else
    run_kl="1"
fi

while [ $run_kl = "1" ]
do
    run_kl="0"
    echo "0" > $KLBFILE
    cd /home/pi/ceefax
    ./run.py            # uncomment this for KLBFAX
    # SLAVE=1 ./run.py  # uncomment this for 28JHFAX
    # EMF=1 ./run.py    # uncomment this for EMFFAX
    run_kl=`cat $KLBFILE`
done
