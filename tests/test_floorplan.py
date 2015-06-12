from unittest import TestCase
from src.floorplan import Floorplan

__author__ = 'pawel'


class TestFloorplan(TestCase):
    def setUp(self):
        self.floorplan = Floorplan(140, 140)

    def test_addNewTerm(self):
        for term_num in range(120):
            name = ''
            if term_num < 10:
                name = '00{}'.format(term_num)
            elif term_num < 100:
                name = '0{}'.format(term_num)
            else:
                name = str(term_num)

            print name
            params = {
                'name': name,
                'index': term_num,
                'type': 'RO7'
            }
            self.floorplan.addNewTerm(params)

        for term_num, term_name in enumerate(sorted(self.floorplan.therms)):
            self.assertEqual(int(term_name), term_num)


    def test_addTermUnit(self):
        pass

    def test_sortTherms(self):
        pass