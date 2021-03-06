from channels.routing import route
from course_apps.course_page.channels.consumers import ws_connect, ws_message, ws_disconnect

channel_routing = [
    route("websocket.connect", ws_connect),
    route("websocket.receive", ws_message),
    route("websocket.disconnect", ws_disconnect),
]

# channel_routing = {
#     # This makes Django serve static files from settings.STATIC_URL, similar
#     # to django.views.static.serve. This isn't ideal (not exactly production
#     # quality) but it works for a minimal example.
#     'http.request': StaticFilesConsumer(),

#     # Wire up websocket channels to our consumers:
#     # example:
#     # 'websocket.connect': consumers.ws_connect,
#     # 'websocket.receive': consumers.ws_receive,
#     # 'websocket.disconnect': consumers.ws_disconnect,
#     'websocket.receive': consumers.receive_n_return,
# }