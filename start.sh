if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Jeolpaul/George-MalarAutofilter.git /George-Malar-Autofilter
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /George-Malar-Autofilter
fi
cd /George-Malar-Autofilter
pip3 install -U -r requirements.txt
echo "Starting BETA Botz💫...."
python3 botz.py && bot
