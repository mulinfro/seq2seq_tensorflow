
import tensorflow as tf

def save_mode(sess):

def load_model(sess):
    pass
    
def learning_rate_decay():
    pass

def get_learning_optimizer(opt):
    if opt == "adam":
        optfn = tf.train.AdamOptimizer
    elif opt == "rmsprop":
        optfn = tf.train.RMSPropOptimizer
    elif opt == "adadelta":
        optfn = tf.train.AdadeltaOptimizer
    else:
        optfn = tf.train.GradientDescentOptimizer
    
    return optfn

# RNN CELLS, Layers

def build_single_cell(cell_type, num_units, train_phase=True, keep_prob = 0.75, residual_connection = False, residual_fn=None):
    if cell_type == "gru":
        cell = tf.contrib.rnn.GRUCell(num_units)
    elif cell_type == "lstm":
        cell = tf.contrib.rnn.LSTMCell(num_units)
    else:
        cell = tf.contrib.rnn.BasicRNNCell(num_units)

    if train_phase and keep_prob < 1:
        cell = tf.contrib.rnn.DropoutWrapper(cell,  
                                    input_keep_prob  = keep_prob, 
                                    output_keep_prob = keep_prob)

    if residual_connection:
        cell = tf.contrib.rnn.ResidualWapper(cell,  residual_fn= residual_fn)

    # device warpper ??
    return cell

def multi_cells(num_layers, cell_type, num_units, train_phase=True, keep_prob = 0.75, num_residual_layers = False, residual_fn=None):
    cell_list = []
    for i in range(num_layers):
        single_cell = build_single_cell(cell_type, num_units, 
                                        train_phase=train_phase,
                                        keep_prob = keep_prob,
                                        residual_connection = (i >= (num_layers - num_residual_layers)),
                                        residual_fn=residual_fn)
        cell_list.append(single_cell)

    if num_layers == 1:
        return cell_list[0]
    return tf.contrib.rnn.MultiRNNCell(cells=cell_list)


def bidirction_rnn_cell(num_layers, cell_type, num_units, train_phase, keep_prob, sequence_length, inputs):
    fw_cell = multi_rnn_cell(num_layers, cell_name, num_units, train_phase, keep_prob )
    bw_cell = multi_rnn_cell(num_layers, cell_name, num_units, train_phase, keep_prob,  num_bi_layers)

    outputs, states = tf.nn.bidirectional_dynamic_rnn(
    cell_fw = fw_cell, 
    cell_bw=bw_cell,
    dtype=tf.float32,
    sequence_length=sequence_length,
    inputs=inputs,
    swap_memory = True
    )

    outputs_concat = tf.concat(outputs, -1)
    return outputs_concat, states


