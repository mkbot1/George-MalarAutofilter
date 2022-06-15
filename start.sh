if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Jeolpaul/Doctor-Strange-Autofilter /Doctor-Strange-Autofilter
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Doctor-Strange-Autofilter
fi
cd /Doctor-Strange-Autofilter
pip3 install -U -r requirements.txt
echo "Starting BETA Botz💫...."
python3 bot.py
