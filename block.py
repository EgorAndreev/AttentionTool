#Block sites
sites = []
localhost = '127.0.0.1'
winhost = 'C:\\Windows\\System32\\drivers\\etc\\hosts'

def init():
    with open(winhost, 'r') as hosts:
        hostsText = hosts.readlines()
        for string in hostsText:
            if ( not string.startswith('#')):
                strR = string.replace('127.0.0.1', '')
                strR = strR.strip()
                sites.append(strR)
    print(sites)
def block():
    addr = input('Enter site domain name (ex.-www.youtube.com): ')
    sites.append(addr)
    with open(winhost, 'a+') as hosts:
        hosts.write('\n{localhost}\t{addr}'.format(localhost=localhost, addr=addr))
    print('Successful')

def unblock():
    while True:                     #select site
        print('Select site:\n')
        number = 1
        for i in sites:
            print(str(number) + ': ' + i)
            number += 1
        select = input()
        try:
            selectSite = sites[int(select)-1]
            break
        except Exception as ex:
            print(ex)
            continue
    with open(winhost, 'w+') as hosts:  #remove site
        hostsText = hosts.readlines()
        for string in hostsText:
            if ( not string.startswith('#')) and (selectSite in string):
                hostsText[hostsText.index(string)] = ''
                
                break
        hosts.writelines(hostsText)
    sites.pop(int(select)-1)
    print('Successful')
def main():
    init()
    while True:
        print('Please enter operation:\n1. block\n2. unblock\n3. exit\n')
        op = input()
        if op == '1':
            block()
        elif op == '2':
            unblock()
        elif op == '3':
            exit()
        else: continue


if __name__ == "__main__":
    main()