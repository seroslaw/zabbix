import requests
import json

def zabbix_api_token(url, login, password):

    api_login = requests.post(
    url, json={
                "jsonrpc": "2.0",
                "method": "user.login",
                "params": {
                    "username": login,
                    "password": password
                },
                "id": 1
            }
    )

    AUTHTOKEN = api_login.json()["result"]
    return AUTHTOKEN
    
def host_get(token, url):
    
    host_get = requests.post(
    url, json={
                "jsonrpc": "2.0",
                "method": "host.get",
                "params": {
                    "output": ["hostid", "host"],
                    "selectInterfaces": ["ip", "type"]
                },
                "auth": token,
                "id": 1
                }
    )

    hosts_list = host_get.json()["result"]

    print("Hosts list before filtering:")
    print("\n")
    print(hosts_list)
    print("\n")
    print(type(hosts_list))
    print(len(hosts_list))

    print("\n\n")
    #print(type(hosts_list)) <--- list type

    return hosts_list

    '''
    i = 0

    # view list of objects
    for item in hosts_list:
        host_id = item["hostid"]
        host_name = item["host"]
        interfaces = item["interfaces"]

        print(f"Index id: {i}")
        print(f"host_id = {host_id}")
        print(f"host_name = {host_name}")
        print(f"interface = {interfaces}")

        i=i+1
    '''        

def filter_hosts_list(hosts):
    new_hosts_list = []
    filter = ["NFK"]

    for item in hosts:
        host_name = item["host"]

        '''if filter[0] == host_name:
            pass
        else:
            new_hosts_list.append(item)
        '''
        if filter[0] in host_name:
            pass
        else:
            new_hosts_list.append(item)

    print("Hosts list after filtering:")
    print("\n")
    print(new_hosts_list)
    print("\n")
    print(type(new_hosts_list))
    print(len(new_hosts_list))





    

def main():

    ZABBIX_API_URL = "http://192.168.64.2/zabbix/api_jsonrpc.php" #Type your Zabbix endpoint
    UNAME = "zabbix_api" #Type your user login in Zabbix
    PWORD = "test123$" #Type your Zabbix API user pass

    #Let's download a list of hosts from our Zabbix server
    hosts_list = host_get(zabbix_api_token(ZABBIX_API_URL, UNAME, PWORD), ZABBIX_API_URL)
    #print(type(hosts_list)) <--- still list type

    #Let's filter our list
    filter_hosts_list(hosts_list)

    


if __name__ == '__main__':
    main()

