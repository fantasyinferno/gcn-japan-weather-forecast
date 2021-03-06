#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Parse input command to hyper-parameters


import argparse

parser = argparse.ArgumentParser()
arg_list = []

def str2bool(v):
    return v.lower() in ('true', '1')

def add_argument_group(name):
    arg = parser.add_argument_group(name)
    arg_list.append(arg)
    return arg


# Data
data_arg = add_argument_group('Data')
data_arg.add_argument('--data_dir', type=str, default='datasets/') #data_dir : '/usr/dataset/ptb/'

# Training/Test param
train_arg = add_argument_group('Training')
train_arg.add_argument('--task', type=str, default='japan',
                       choices=['ptbchar', 'swissmt', "japan"], help='')
train_arg.add_argument('--num_epochs', type=int, default=100, help='')
train_arg.add_argument('--batch_size', type=int, default=20, help='')
train_arg.add_argument('--random_seed', type=int, default=123, help='')
train_arg.add_argument('--max_step', type=int, default=1000000, help='')
train_arg.add_argument('--is_train', type=str2bool, default=False, help='')
train_arg.add_argument('--classif_loss', type=str,
                       default='l2_norm', choices=['cross_entropy', 'l2_norm'], help='')
train_arg.add_argument('--learning_rate', type=float, default=1e-4, help='')
train_arg.add_argument('--max_grad_norm', type=float, default=-1, help='')
train_arg.add_argument('--optimizer', type=str,
                       default='adam', choices=['adam_wgan', 'adam', 'sgd', 'rmsprop'], help='')
train_arg.add_argument('--checkpoint_secs', type=int, default=300, help='')

# Model args
model_arg = add_argument_group('Model')
model_arg.add_argument('--model_type', type=str, default='gbasicrnn',
                        choices=['lstm', 'glstm', 'gbasicrnn'], help='')

# Hyperparams for graph
graph_arg = add_argument_group('Graph')
graph_arg.add_argument('--num_node', type=int, default=20, help='')
graph_arg.add_argument('--feat_in', type=int, default=1, help='') # max_tp and seasonal features
graph_arg.add_argument('--feat_out', type=int, default=1, help='')
graph_arg.add_argument('--num_hidden', type=int, default=50, help='')
graph_arg.add_argument('--num_kernel', type=int, default=3, help='')
train_arg.add_argument('--num_time_steps', type=int, default=5, help='')

# Miscellaneous (summary write, model reload)
misc_arg = add_argument_group('Misc')
misc_arg.add_argument('--log_step', type=int, default=20, help='')
misc_arg.add_argument('--log_dir', type=str, default='logs')
misc_arg.add_argument('--load_path', type=str, default="grnn;k=3;knn=4")
misc_arg.add_argument('--gpu_memory_fraction', type=float, default=1.0)


def get_config():
    config, unparsed = parser.parse_known_args()
    return config, unparsed
