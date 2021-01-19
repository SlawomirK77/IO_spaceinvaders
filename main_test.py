import main
import unittest
"""
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)
"""


class ShipTest(unittest.TestCase):
    def setUp(self):
        self.ship = main.Ship(400, 400)

    def test_health(self):
        self.assertEqual(self.ship.health, 100)

    def test_ship_img(self):
        self.assertIsNone(self.ship.ship_img)

    def test_laser_img(self):
        self.assertIsNone(self.ship.laser_img)


class PlayerTest(unittest.TestCase):
    def setUp(self):
        self.player = main.Player(600, 300, 500)

    def test_health(self):
        self.assertEqual(self.player.health, self.player.max_health, 500)

    def test_width(self):
        self.assertEqual(self.player.get_width(), 100)

    def test_height(self):
        self.assertEqual(self.player.get_height(), 90)


class EnemyTest(unittest.TestCase):
    def setUp(self):
        self.enemy1 = main.Enemy(main.WIDTH - 70 - main.ENEMY_VEL, 50, "red")
        self.enemy2 = main.Enemy(main.ENEMY_VEL - 1, 200, "red")

    def test_width(self):
        self.assertEqual(self.enemy1.get_width(), 70)

    def test_right(self):
        self.assertFalse(main.right([self.enemy1]))
        self.assertTrue(main.right([self.enemy2]))

    def test_left(self):
        self.assertTrue(main.left([self.enemy1]))
        self.assertFalse(main.left([self.enemy2]))

    def test_jump_height(self):
        h1, h2 = self.enemy1.y, self.enemy2.y
        main.jump([self.enemy1, self.enemy2])
        self.assertEqual(self.enemy1.y, h1 + 10 + self.enemy1.get_height())
        self.assertEqual(self.enemy2.y, h2 + 10 + self.enemy2.get_height())


class LaserTest(unittest.TestCase):
    def setUp(self):
        self.laser1 = main.Laser(50, 50, main.RED_LASER)
        self.laser2 = main.Laser(50, -10, main.RED_LASER)
        self.laser3 = main.Laser(50, 1500, main.RED_LASER)

    def test_off_screen(self):
        self.assertFalse(self.laser1.off_screen(main.HEIGHT))
        self.assertTrue(self.laser2.off_screen(main.HEIGHT))
        self.assertTrue(self.laser3.off_screen(main.HEIGHT))


class LostTest(unittest.TestCase):
    def test_is_lost(self):
        self.assertTrue(main.is_lost(0, 10))
        self.assertTrue(main.is_lost(4, 0))
        self.assertTrue(main.is_lost(3, -50))
        self.assertTrue(main.is_lost(-1, 100))
        self.assertTrue(main.is_lost(-5, -10))
        self.assertFalse(main.is_lost(1, 10))


class CollideTest(unittest.TestCase):
    def setUp(self):
        self.player = main.Player(100, 100, 20)
        self.laser1 = main.Laser(100 + int(self.player.get_width()/2),
                                 100 + int(self.player.get_height()/2), main.RED_LASER)
        self.enemy = main.Enemy(500, 500, "red")
        self.laser2 = main.Laser(500, 500, main.YELLOW_LASER)
        self.player.lasers.append(self.laser2)
        self.enemy.lasers.append(self.laser1)

    def test_collide(self):
        self.assertIn(self.laser2, self.player.lasers)
        self.assertIn(self.laser1, self.enemy.lasers)
        self.assertFalse(main.collide(self.player, self.laser2))
        self.assertFalse(main.collide(self.enemy, self.laser1))
        self.assertIsNotNone(main.collide(self.player, self.laser1))
        self.assertIsNotNone(main.collide(self.enemy, self.laser2))


if __name__ == '__main__':
    unittest.main()
