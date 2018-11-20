
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--dropout', type=float, default=0., help='dropout rate at each non-recurrent layer')

parser.add_argument('--embding_size', type=int, default=100, help='word embedding dimension')
parser.add_argument('--hidden_size', type=int, default=100, help='hidden layer dimension')
parser.add_argument('--num_layers', type=int, default=1, help='number of hidden layers')
parser.add_argument('--bidirectional', action='store_true', help='Whether to use bidirectional RNN (default is unidirectional)')

parser.add_argument('--max_norm', type=float, default=5, help="threshold of gradient clipping (2-norm)")
parser.add_argument('--lr', type=float, default=0.01, help='learning rate')
parser.add_argument('--lr_decay', type=float, default=0.6, help='the decay rate of learning rate')
parser.add_argument('--min_lr', type=float, default=0.00005, help='the minimum learning rate')
parser.add_argument('--batchSize', type=int, default=64, help='input batch size')

parser.add_argument('--epoch_num', type=int, default=50, help='max number of epochs to train for')

parser.add_argument('--model_name', required=False, help='model out_path')
