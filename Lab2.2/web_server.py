from flask import Flask
import glob
import re

FOLDER = 'config_files\\'
CONFIG_FILES = FOLDER + '*'
PATTERN = 'ip address'

file_list = glob.glob(CONFIG_FILES)
host_list = {}
for filename in file_list:
    #print(filename)
    s = re.match(FOLDER + "\(.*)_.*", filename)
    if bool(s): host_list[s.group(1)] = filename
    #print(str(bool(s)) + ': ' + filename)
    #print(s.group(1))


app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "Справка об использовании"

@app.route('/configs')
def configs():
    host_list1 = ""
    for host in host_list.keys():
        host_list1 += host + '<br>'
        print(host)
    return host_list1

@app.route('/config/<hostname>')
def config_hostname(hostname):
    if hostname in host_list.keys():
        filename = host_list[hostname]
        addresses = ""
        with open(filename, 'r') as file:
            for line in file:
                if line.find(PATTERN) != -1:
                    addresses += line.strip() +"<br>"
        return addresses
    return ""




if __name__ == '__main__': app.run(debug=True)