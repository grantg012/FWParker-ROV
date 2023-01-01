import unittest


def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)


class TranslateTest(unittest.TestCase):
    def test_valid(self):
        """Test some basic math to check that the function works as intended"""
        cases = [
            (0.5, 0, 1, 0, 2, 1),
            (0, 0, 1, 0, 2, 0),
            (1, 0, 1, 0, 2, 2),
            (0, -1, 1, 0, 1, 0.5),
            (0.5, 0, 1, -1, 1, 0)
        ]
        for (v, lMin, lMax, rMin, rMax, exp) in cases:
            self.assertAlmostEqual(exp, translate(v, lMin, lMax, rMin, rMax))

    def test_invalid(self):
        """Test some invalid cases"""
        cases = [
            (1.5, 0, 1, 0, 2),
            # (10, 0, 0, 0, 2),  # uncommenting this will find a failure when it runs due to a range being 0
        ]
        for (v, lMin, lMax, rMin, rMax) in cases:
            try:
                translate(v, lMin, lMax, rMin, rMax)
            except Exception as e:
                self.fail(str(e))

    def test_rov_situ(self):
        """Test some values that are actually used on the ROV."""
        cases = [
            (0.5, -1, 1, 1400, 1600, 1550),
            (-0.5, -1, 1, 1600, 1400, 1550),
            (0.5, -1, 1, 1600, 1400, 1450),
        ]
        for (v, lMin, lMax, rMin, rMax, exp) in cases:
            self.assertAlmostEqual(exp, translate(v, lMin, lMax, rMin, rMax))


if __name__ == "__main__":
    unittest.main()
