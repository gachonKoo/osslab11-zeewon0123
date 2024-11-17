from geo.utils import circle_area

def run_tests():
    try:
        assert abs(circle_area(5) - 78.53981633974483) < 1e-6, "Test failed for radius 5"
        assert abs(circle_area(0) - 0) < 1e-6, "Test failed for radius 0"
        try:
            circle_area(-1)
        except ValueError:
            pass  # Expected exception
        else:
            raise AssertionError("Test failed for negative radius")
        print("All tests passed!")
    except AssertionError as e:
        print(e)

if __name__ == "__main__":
    run_tests()
