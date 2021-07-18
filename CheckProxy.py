
import os,time, requests, sys, threading
version = str(sys.version)
def cls():
    linux = 'clear'
    windows = 'cls'
    os.system([linux,windows][os.name == 'nt'])
cls()
sitelog = input(str("Your site url for check with http/https: "))

def xx(PROXY, url):
    try:
        sess = requests.session()
        sess.proxies = {'http': PROXY}
        sess.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                                      ' (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
        aa = sess.get(url, timeout=5, proxies={'http': PROXY})
        if (aa.status_code == 200):      	
            with open('OKproxy.txt', 'a') as xx:
                xx.write(PROXY + '\n')
        else:
            pass 
    except:
        pass
    
def main():
    try:
        if ('3.' in version):
            try:
               print("proxy in proxy.txt")
               fileproxy = ('proxy.txt')
            except:
                print('  [-] Error : Enter Your Proxy!')
                sys.exit()
        elif ('2.' in version):
            try:
                print ("proxy in proxy.txt")
                fileproxy = open('proxy.txt' , 'r')
            except:
                print ('  [-] Error : Enter Your Proxy!')
                sys.exit()
        else:
            print('!')
    except:
        pass
        sys.exit()
    with open(fileproxy, 'r') as x:
        prox = x.read().splitlines()
    thread = []
    for proxy in prox:
        t = threading.Thread(target=xx, args=(proxy, sitelog ))
        t.start()
        thread.append(t)
        time.sleep(0.1)
    for j in thread:
        j.join()

main()