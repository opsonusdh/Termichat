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
apt install python git 
git clone https://github.com/opsonusdh/Termichat
cd Termichat
```

### Important
Paste your GitHub username and token in the `gists` file, with the following code:
```bash
nano gists.json
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