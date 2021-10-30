# setup_tpu.py

import os
import tensorflow as tf
from tensorflow import keras

def setup_tpu() -> tf.distribute.TPUStrategy:
    """
    Sets up TPU for usage in Google Colab. Returns a TPU strategy.

    :return: A TPU strategy.
    :rtype: tf.distribute.TPUStrategy
    """
    TF_MASTER = f"grpc://{os.environ['COLAB_TPU_ADDR']}"

    resolver = tf.distribute.cluster_resolver.TPUClusterResolver(TF_MASTER)
    tf.config.experimental_connect_to_cluster(resolver)
    tf.tpu.experimental.initialize_tpu_system(resolver)

    return tf.distribute.TPUStrategy(resolver)
