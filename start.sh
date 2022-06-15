if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Jeolpaul/KC-Films-Bot /KC-Films-Bot
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /KC-Films-Bot
fi
cd /KC-Films-Bot
pip3 install -U -r requirements.txt
echo "Starting BETA Bot...."
python3 bot.py
