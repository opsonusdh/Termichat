# Termichat
A program to chat with people in terminal with a own personal server

## Supported platforms
• Linux
• Kali Linux
• Ubuntu
• Termux
• And other terminals
## How to use
### Run the commands in the terminal:


```bash
apt update -y && apt upgrade -y
apt install python git -y
git clone https://github.com/opsonusdh/Termichat
cd Termichat
nano gists.json
```

### Important
#### • If you want your own server change the `username` and `token` with yours,
#### • If you want to chat in our server, clear everything in `gists.json` and paste this: 
```json
{"username": "Rajdeep-the-coder","token":"ghp_v9UTEajhWJUigw6Hr30jcEYlQzmG2a58Wo","idinfo":"ff1cbad1182e8a20ede404f95e1ed57d","roomserver":"bb9da035c1079abeba0f181dd33514ae"}
```
After pasting that you are good to go.
Then run the main script:
```bash
python termichat.py
```
or
```bash
python3 termichat.py
```
#### If there is any problem while importing or installing modules:
You can run in terminal:
```bash
pip install -r requirements.txt
```
or
```bash
pip3 install -r requirements.txt
```
