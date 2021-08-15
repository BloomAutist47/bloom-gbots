import os 

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# How to use quick follower generator by Bloom
# 1. Place your follower .gbot in the same directory as this .py script
# 2. place in the FOLLOWER_BOT your template follower gbot
# 2. place in the REPLACE_CODE the target player name
# 3. Place in the followers a list of your alt names
# 4. Run

REPLACE_CODE = "<Target Player Name>"
FOLLOWER_BOT = "Bloom_DeluxeFollower_v4_rev.gbot"
FOLLOWERS = [
	"ACrolous",
	"Kyrea",
	"Yurea",
	"Melisia",
	"Tirea",
	"Khasandra",
	"Soulerousxx",
	"BloomAutist47",
	"Luprehia",
	"Euphridiates",
	"Thalesius",
	"jerime1234567890"
]

# edit this aabove.










# Don't think about this one
f = open(f"{FOLLOWER_BOT}", "r")
item = f.read()

for name in FOLLOWERS:
	f = open(f"{name}.gbot", "w")
	f.write(item.replace(REPLACE_CODE, name))
	print(f"> Done saving {name}.gbot")
	f.close()