import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import monitor

def row(j, p, age):
    return {"job": j, "printer": p, "age_minutes": str(age)}

class TestQueueAge(unittest.TestCase):
    def test_stuck(self):
        self.assertEqual(monitor([row("J1", "HP-1", 90)])[0][3], "STUCK")
    def test_waiting(self):
        self.assertEqual(monitor([row("J1", "HP-1", 30)])[0][3], "WAITING")
    def test_ok(self):
        self.assertEqual(monitor([row("J1", "HP-1", 5)])[0][3], "OK")
    def test_oldest_first(self):
        r = monitor([row("A", "HP-1", 5), row("B", "HP-1", 90)])
        self.assertEqual(r[0][0], "B")
