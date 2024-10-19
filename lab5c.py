from lab5b import pixel_constraint, generator_from_image, combine_images

def test_pixel_constraint():
    """
    Test the function pixel_constraints with diffrent edgecases and other values.
    """
    # Checks the code with 255 as high and 0 as low values, values inannför intervallet
    result = pixel_constraint(0,255,0,255,0,255)((5,5,5))
    assert(result == 1)

    # Checks the code with 255 as high and 0 as low values.
    result = pixel_constraint(255,0,255,0,255,0)((5,5,5))
    assert(result == 0)

     # Checks the code with 255 as high and 255 as low values. Values utanför intervallet
    result = pixel_constraint(255,255,255,255,255,255)((5,5,5))
    assert(result == 0)

     # Checks the code with 0 as high and 0 as low values. Values utanför intervallet
    result = pixel_constraint(0,0,0,0,0,0)((5,5,5))
    assert(result == 0)

     # Checks the code with 200 as high and 100 as low values. Values utanför intervallet
    result = pixel_constraint(100,200,100,200,100,200)((5,5,5))
    assert(result == 0)

    try:
        result = pixel_constraint(100,200,100,200,100,200)("hej")
        raise AssertionError
    except TypeError:
        pass
    except AssertionError:
        print("Test Failed. Excpected TypeError")
    

    try:
        result = pixel_constraint(100,200,100,200,100,200)(5,5)
        raise AssertionError
    except TypeError:
        pass
    except AssertionError:
        print("Test Failed. Excpected ValueError")


def test_generator_from_image():
    """
    Tests the function generator_from_image if its able to retrive
    elements in a list from functionscalls.
    """
    #  Checks the code with different data
    data = [(2,4,6),(100,20,"b",5),"hejsans",(1.0,9,4.6)]
    result = generator_from_image(data)
    assert(result(-1) == (1.0,9,4.6))
    assert(result(0) == (2,4,6))
    assert(result(1) == (100,20,"b",5))
    assert(result(2) == "hejsans")

    #Checks with error handling
    try:
        result("hej")
        raise AssertionError
    except TypeError: 
        pass
    except AssertionError:
        print("Test failed. Expected TypeError")

    try:
        result(100)
        raise AssertionError
    except IndexError:
        pass  
    except AssertionError:
        print("Test failed. Excpected IndexError")


def test_combine_images():
    """
    Tests the function combine_images by checking if it catches an error
    message if the lists that it uses are different lenghts, and if it works
      if it should work.
    """
    # The function gets the correct arguments. Same size list.
    condition = pixel_constraint(100, 150, 50, 200, 100, 255)
    hsv_list = [(1,1,1), (1,1,1),(1,1,1)]
    generator1 = generator_from_image([[2,2,2],[2,2,2],[2,2,2]])
    generator2 = generator_from_image([[2,2,2],[2,2,2],[2,2,2]])
    result = combine_images(hsv_list,condition,generator1,generator2)
    assert(result == [(2, 2, 2), (2, 2, 2),(2,2,2)])

    # The function gets the incorrect arguments. Diffrent size list.
    condition = pixel_constraint(100, 150, 50, 200, 100, 255)
    hsv_list = [(1,1,1), (1,1,1),(1,1,1)]
    generator1 = generator_from_image([[2,2,2],[2,2,2],[2,2,2]])
    generator2 = generator_from_image([[2,2,2],[2,2,2]])
    result = combine_images(hsv_list,condition,generator1,generator2)
    assert(result == None)


def run_free_spans_tests():
    test_pixel_constraint()
    test_generator_from_image()
    test_combine_images()
    print("All tests passed")


if __name__ == "__main__":
    run_free_spans_tests()