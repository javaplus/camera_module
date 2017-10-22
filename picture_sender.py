import paho.mqtt.client as mqtt
import socket
import io

# send the picture to a q

def sendPicture(pathToPic):
    byteArray = None
    with io.FileIO(pathToPic, 'rb') as file:
        byteArray = file.readall()
    
    #mqttc = mqtt.Client(getMyClientIdHostName)
    mqttc = mqtt.Client("test")
    #mqttc.connect("10.0.0.1", 1883)
    mqttc.connect("192.168.1.114", 1883)
    #mqttc.connect("localhost", 1883)
    # retain messages so on restart clients get last message
    mqttc.publish("picture/pics", payload=byteArray,qos=0,retain=True) 
    mqttc.loop(2) #timeout = 2s
    
def getMyClientIdHostName():
    clientId = "raspi"
    try:
        clientId += str(socket.gethostbyname(socket.gethostname()))
    except BaseException as ex:
        # don't really do anything other than log error
        print("Couldn't get hostname:" + ex.message )

    return clientId


if __name__ == "__main__":
    sendPicture("c:/temp/hay.jpg")