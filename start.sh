if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/lazyindu/test1.git /CutePrincess
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /CutePrincess
fi
cd /CutePrincess
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
