from shapes import area_of_triangle

def test_area_of_triangle():
    # Test case 1: Regular triangle with integer base and height
    assert area_of_triangle(4, 6) == 12.0

    # Test case 2: Regular triangle with float base and height
    assert round(area_of_triangle(3.5, 8.2), 2) == 14.35

    # Test case 3: Triangle with base 0 should have area 0
    assert area_of_triangle(0, 10) == 0.0

    # Test case 4: Triangle with height 0 should have area 0
    assert area_of_triangle(7, 0) == 0.0

    # Test case 5: Negative base and height should still yield positive area
    assert area_of_triangle(-5, -6) == 15.0

    # Test case 6: Large base and height
    assert area_of_triangle(1000, 500) == 250000.0

    # Test case 7: Base and height of 1
    assert area_of_triangle(1, 1) == 0.5

    # Test case 8: Base and height of 10
    assert area_of_triangle(10, 10) == 50.0

    print("All test cases passed!")

# Run the test function
test_area_of_triangle()
