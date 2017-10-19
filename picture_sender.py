import paho.mqtt.client as mqtt
import socket
import io

def on_log(client, userdata, level, buf):
    print("log: ",buf)


def on_publish(client, userdata, mid):
    print("on publish mid:" + str(mid))

# send the picture to a q

def sendPicture(pathToPic):
    print("sending pic")
    byteArray = None
    with io.FileIO(pathToPic, 'rb') as file:
        byteArray = file.readall()
    
    #mqttc = mqtt.Client(getMyClientIdHostName)
    mqttc = mqtt.Client()
    mqttc.on_log = on_log
    mqttc.on_publish = on_publish
    mqttc.connect("192.168.1.114", 1883)
    # retain messages so on restart clients get last message
    midValue = mqttc.publish("picture/pics", payload=byteArray,qos=0,retain=True) 
    print("midValue=" + str(midValue)) 
    mqttc.loop_start() #timeout = 2s
    #mqttc.loop_stop() #timeout = 2s
    print("published")
    
def getMyClientIdHostName():
    clientId = "raspi"
    try:
        clientId += str(socket.gethostbyname(socket.gethostname()))
    except BaseException as ex:
        # don't really do anything other than log error
        print("Couldn't get hostname:" + ex.message )

    return clientId


if __name__ == "__main__":
    sendPicture("/home/pi/pictures/test.jpg")
