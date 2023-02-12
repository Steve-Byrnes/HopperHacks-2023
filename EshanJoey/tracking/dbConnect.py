import requests

class dbConnect:

    @staticmethod
    def getSwings():
        x = requests.get('http://172.24.196.228:8080/api/swings')
        return x.text

    @staticmethod
    def setSwing(body_dic):
        # body_dic = {
        #         'user': user,
        #         'start_x': start_x,
        #         'start_y': start_y,
        #         'end_x': end_x,
        #         'end_y': end_y,
        #         'duration': duration,
        #         'angle': angle,
        #         'power': power
        #     }
        x = requests.post('http://172.24.196.228:8080/api/swings', json=body_dic)
        return x.text

    @staticmethod
    def updateSwing(id, update_dic):
        # update_dic = {
        #         'user': user,
        #         'start_x': start_x,
        #         'start_y': start_y,
        #         'end_x': end_x,
        #         'end_y': end_y,
        #         'duration': duration,
        #         'angle': angle,
        #         'power': power
        #     }
        x = requests.put('http://172.24.196.228:8080/api/swings/' + id, json=update_dic)
        return x.text

    @staticmethod
    def deleteSwing(id):
        body = {
            'id': id
        }
        x = requests.delete('http://172.24.196.228:8080/api/swings/' + id, json=body)
        return x.text