import cifar10
import tensorflow as tf

FLAGS = tf.app.flags.FLAGS
FLAGS.data_dir = "cifar10_data/"

cifar10.maybe_download_and_extract()
