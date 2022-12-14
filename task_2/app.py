
# uvicorn --reload app:app
import socketio
sio = socketio.AsyncServer(async_mode='asgi')
app = socketio.ASGIApp(sio, static_files={
    '/':'./public/'
})

@sio.event
async def connect(sid, enviornment):
    print(sid, 'connected')

@sio.event
async def disconnect(sid):
    print(sid, 'disconnected')

@sio.event
async def sum(sid, data):
    result = data['numbers'][0] + data['numbers'][1]
    print(sid, data, result)
    return {'result':result}
    