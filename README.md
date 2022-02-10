# dank-memer-farmer

This simple discord script will farm dank memer currency for you passively as long as you have it running.

# DISCLAIMER

BE CAREFUL, THIS COULD GET YOUR DISCORD ACCOUNT TERMINATED AS BOTTING A DISCORD ACCOUNT THAT IS NOT FLAGGED AS A BOT ACCOUNT IS AGAINST TOS. USE AN ALT AND TRANSFER THE DANK MEMER CURRENCY FROM THERE.

# config

First, install the requests pip module with the `pip install requests` command.

Then, create a `config.json` in the root directory of this project and put your discord accounts token as well as the channelid of the channel you want to spam in like this:

```json
{
  "token": "DISCORD ACCOUNT TOKEN",
  "channel-id": "CHANNEL ID",
  "pause_timer": int(time in seconds)
}
```

Make sure you own the server you're going to do this in as spamming this much will result in a ban in most servers.
