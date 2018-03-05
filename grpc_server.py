from concurrent import futures
import time

import grpc

import rfid_pb2
import rfid_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class GRPC_Server(rfid_pb2_grpc.RFID_SERVICEServicer):

    def RFID_Change(self, request, context):
        print "Received RFID Change."
        print request
        return rfid_pb2.RFID_RESPONSE()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    rfid_pb2_grpc.add_RFID_SERVICEServicer_to_server(GRPC_Server(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
