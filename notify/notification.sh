API="o.Lbh01ptuz6NS0TDmDYdrVWhQEdXnWsvW"

MSG="$1"
curl -u $API: https://api.pushbullet.com/v2/pushes -d type=note -d title="You Have A New Message" -d body="$MSG"