import os
import sys

# sys.path.insert(0, os.path.abspath("../"))
sys.path.insert(0, os.path.dirname(__file__))


class {{cookiecutter.module_name}}(object):

    def __init__(self, conf={}):
        '''

        :param input:
        '''
        self.checkpoint_dir = os.path.dirname(__file__) + "/results"
        pass

    def train(self, conf={}):
        '''

        :param conf:
        :return:
        '''
        param1 = conf['param1']  # value_type: str # description: some description
        param2 = conf['param2']  # value_type: str # description: some description
        # add your code
        return {'ret1': 'cat', 'ret2': 'dog'}

    def predict(self, conf={}):
        '''

        :param conf:
        :return:
        '''
        param1 = conf['param1']  # value_type: str # description: some description
        param2 = conf['param2']  # value_type: str # description: some description
        # add your code
        return {'ret1': 'cat', 'ret2': 'dog'}

    def load_model(self):
        '''

        :param conf:
        :return:
        '''
        pass


## Note: Uncomment this block before creating a crowdsourcing task
# if __name__ == '__main__':
#     func_name = sys.argv[0]
#     instance = {{cookiecutter.module_name}}()
#     getattr(instance, func_name)()
