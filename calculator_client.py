from __future__ import print_function

import grpc

import calculator_pb2
import calculator_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = calculator_pb2_grpc.CalculatorStub(channel)
        
        #get input values from the user
        number1 = input(" Please Enter the First Number: ")
        number2 = input(" Please Enter the Second number: ")
        
        #receive response
        response = stub.add(calculator_pb2.AddRequest(a=int(number1),b=int(number2)))
        
        #printing received response
        print("Client received: " + response.sum)


if __name__ == '__main__':
    run()
