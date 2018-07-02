function update {
    where=`pwd`
    cd /home/pi/ceefax
    python update.py
    cd "$where"
}

export FAXFILE="/home/pi/.fax/FAX_status"

if $(ps aux | grep "./run.py" | grep -v "grep" > /dev/null); then
    echo "FAX running already."
    run_kl="0"
else
    run_kl="1"
fi

while [ $run_kl = "1" ]
do
    run_kl="0"
    echo "0" > $FAXFILE
    cd /home/pi/ceefax
    ./run.py
    run_kl=`cat $FAXFILE`
done
