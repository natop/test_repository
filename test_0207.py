import urllib.request
import urllib.parse
import urllib.error
import json


class ZabbixApi:
    def __init__(self):
        self.url = 'http://192.168.50.128:8080/api_jsonrpc.php'
        self.user = 'Admin'
        self.password = 'zabbix'
        self.header = {"Content-Type": "application/json"}
        self.token_id = self.UserLogin()

    def UserLogin(self):
        data = {
            "jsonrpc": "2.0",
            "method": "user.login",
            "params": {
                "user": self.user,
                "password": self.password
            },
            "id": 0,
        }
        return self.PostRequest(data)

    def PostRequest(self, data):
        conte = json.dumps(data).encode('utf-8')
        request = urllib.request.Request(self.url, conte, self.header)
        result = urllib.request.urlopen(request)
        response = json.loads(result.read().decode('utf-8'))
        try:
            return response['result']
        except KeyError:
            raise KeyError

    def HostGet(self):
        data = {
            "jsonrpc": "2.0",
            "method": "host.get",
            "params": {
                "output": ["hostid"],
                "filter": {
                    "host": [
                        "Zabbix server 02"
                    ]
                }
            },
            "auth": self.token_id,
            "id": 1
        }
        return self.PostRequest(data)

    def HostUpdate(self):
        data = {
            "jsonrpc": "2.0",
            "method": "host.update",
            "params": {
                "hostid": "10379",
                "groups": [
                    {
                        "groupid": "4",
                        "name": "Zabbix servers"
                    },
                    {
                        "groupid": "2",
                        "name": "Linux servers"
                    }
                ]
            },
            "auth": self.token_id,
            "id": 0,
        }
        return self.PostRequest(data)

    def UserCreate(self):
        data = {
            "jsonrpc": "2.0",
            "method": "user.create",
            "params": {
                "alias": "Golfeng",
                "passwd": "198417us",
                "roleid": "2",
                "usrgrps": [
                    {
                        "usrgrpid": "7"
                    }
                ],
                "user_medias": [
                    {
                        "mediatypeid": "1",
                        "sendto": [
                            "support@company.com"
                        ],
                        "active": 0,
                        "severity": 63,
                        "period": "1-7,00:00-24:00"
                    }
                ]
            },
            "auth": self.token_id,
            "id": 2
        }
        return self.PostRequest(data)


def main():
    zapi = ZabbixApi()
    # hostupdate = zapi.HostUpdate()
    # hostget = zapi.HostGet()
    # userlogin = zapi.UserLogin()
    usercreate = zapi.UserCreate()
    print(usercreate)


if __name__ == '__main__':
    main()
