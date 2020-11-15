import os
import unittest

from dotenv import load_dotenv
from hydra.experimental import initialize, compose

from core_lib.helpers.generate_data import generate_email, generate_random_string
#import pymysql
#pymysql.install_as_MySQLdb()

from rating_core_lib.rating_core_lib import RatingCoreLib


path = os.path.join(os.path.dirname(__file__), "data")
load_dotenv(dotenv_path=os.path.join(path, '.env'))
initialize(config_path=os.path.join('data', 'config'), caller_stack_depth=1)
config = compose('config.yaml')

rating_core_lib = RatingCoreLib(config)
rating_core_lib.start_core_lib()


class TestRatingCoreLib(unittest.TestCase):

    def test_1(self):
        user_id = 1
        target_id = 1  # GAME ID 1
        target_type_id = 1  # TYPE GAME
        rating = 100
        rating_core_lib.rating.rate(user_id, target_type_id, target_id, rating)

        ratings = rating_core_lib.rating.all_user(user_id)
        self.assertEqual(len(ratings), 1)

        rating = 200
        rating_core_lib.rating.rate(user_id, target_type_id, target_id, rating)

        ratings = rating_core_lib.rating.all_user(user_id)
        self.assertEqual(len(ratings), 1)

        rating_core_lib.rating.rate(user_id, target_type_id, target_id+1, rating)

        ratings = rating_core_lib.rating.all_user(user_id)
        self.assertEqual(len(ratings), 2)
