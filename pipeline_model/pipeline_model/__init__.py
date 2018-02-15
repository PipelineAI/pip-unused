import numpy as np
from grpc.beta import implementations
import asyncio
import tensorflow as tf
# These are generated from the TF serving source.
from . import model_pb2, predict_pb2, prediction_service_pb2

__version__ = "1.0.4"

class TensorFlowServingModel():
    
    def __init__(self,
                 host: str,
                 port: int,
                 model_name: str,
                 timeout: int):

        self._host = host
        self._port = port
        self._model_name = model_name
        self._timeout = timeout


    def predict(self,
                input_str_nparray_dict):

        channel = implementations.insecure_channel(self._host,
                                                   self._port)

        stub = prediction_service_pb2.beta_create_PredictionService_stub(channel)
       
        # Transform input str::nparray dict into TensorFlow PredictRequest/tensors
        tf_request = predict_pb2.PredictRequest()
        tf_request.model_spec.name = self._model_name
        # We assume only a single version per model is running in this model server.
        # tf_request.model_spec.version.value = ...

        for input_str_key, _ in input_str_nparray_dict.items():
            input_tensor = tf.make_tensor_proto(input_str_nparray_dict[input_str_key],
                                                dtype=tf.float32)
            tf_request.inputs[input_str_key].CopyFrom(input_tensor)

        # Call TensorFlow Serving Predict
        response = stub.Predict(tf_request, self._timeout)

        # Transform PredictResponse/tensors to output str::nparray dict
        output_str_nparray_dict = {}
        for output_str_key, _ in response.outputs.items():
            output_str_nparray_dict[output_str_key] = tf.make_ndarray(response.outputs[output_str_key])

        return output_str_nparray_dict
