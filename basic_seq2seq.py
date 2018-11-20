
import tensorflow as tf
import argparse


class Basic_seq2seq():

    def __init__(self, config):
        self.config = config
        self.mode = config.mode



    def bulid_model(self, ):
        print("Begin building model")
        self.global_step = tf.Variable(0, trainable=False)
        self.init_input_placeholders()
        self.build_encoder()
        self.build_decoder()

    def init_input_placeholders(self, ):
        self.source_tokens = tf.placeholder(tf.int32, shape=[None, None])
        self.source_length = tf.placeholder(tf.int32, shape=[None, ])
        # dynamic size
        self.batch_size = tf.shape(self.source_tokens)[0]
        self.embding = 
        self.
        if self.mode == "train":
            self.target_tokens = tf.placeholder(tf.int32, shape=[None, None])
            self.target_length = tf.placeholder(tf.int32, shape=[None, ])

    def build_encoder(self):
        pass


    def build_decoder(self):
        pass


    def save_mode(self):

    def load_model(self):
        pass
