import os
import sys

# sys.path.insert(0, os.path.abspath("../"))
sys.path.insert(0, os.path.dirname(__file__))


# Please don't modify the class name
class {{cookiecutter.module_name}}(object):

    def __init__(self, conf={}):
        '''

        :param input:
        '''
        self.checkpoint_dir = os.path.dirname(__file__) + "/results"
        pass

    def train(self, conf={}):
        '''
        training/fitting code for your model
        :param conf:
        :return:
        '''
        # Please write your parameters and return values following the pattern bellow
        param1 = conf['param1']  # value_type: str # description: some description
        param2 = conf['param2']  # value_type: str # description: some description
        # add your code
        return {'ret1': 'cat', 'ret2': 'dog'}

    def predict(self, conf={}):
        '''
        predict/inference code for your model
        :param conf:
        :return:
        '''
        # Please write your parameters and return values following the pattern bellow
        param1 = conf['param1']  # value_type: str # description: some description
        param2 = conf['param2']  # value_type: str # description: some description
        # add your code
        return {'ret1': 'cat', 'ret2': 'dog'}

    def load_model(self):
        '''
        load your trained model weight and structure
        :param conf:
        :return: model instance
        '''
        pass
 
